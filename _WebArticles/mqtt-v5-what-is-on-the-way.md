# MQTT v5: What Is on the Way?

_Captured: 2017-08-29 at 17:47 from [dzone.com](https://dzone.com/articles/mqtt-v5-what-is-on-the-way?edition=319429&utm_source=Zone%20Newsletter&utm_medium=email&utm_campaign=iot%202017-08-29)_

Cisco IoT makes digital transformation a reality in factories, transportation, and utilities. [Learn how](https://dzone.com/go?i=228254&u=https%3A%2F%2Fdeveloper.cisco.com%2Fsite%2Fdevnet%2Fhome%2F%3Futm_source%3DDZone_bumpertext%26utm_medium%3Dad%26utm_campaign%3Ddnamarketing) to start integrating with Cisco DevNet.

"MQTT is a lightweight protocol for IoT."

"MQTT lacks a lot of features."

How many other sentences have you heard when speaking about MQTT with others developers?

During the last year, the OASIS committee has worked on the new MQTT v5 specification, pushing the protocol to the next level in both directions: A lot of new features are coming and they will fill (part of) the gap that it has with other protocols (my opinion is that, from some points of view, the new MQTT v5 is more AMQP-ish); on the other hand, don't tell me that MQTT is as lightweight as before. Adding features means adding complexity, making it heavier, and maybe this is the reason why, today, a lot of IoT developers have decided to not use AMQP for their projects. But I'm repeating myself. More features mean more complexity and they are very welcome.

(The OASIS committee has opened a public review until September 8. You can find more information [here](https://www.oasis-open.org/news/announcements/invitation-to-comment-on-mqtt-v5-0-ends-sept-8th) if you want to read the entire specification).

## Why From 3.1.1 to 5?

A lot of people have asked me about this "jump" from 3.1.1 to 5. The answer is in the protocol itself!

The CONNECT packet, which brings connection information from the client to the broker, has a "protocol version" byte inside the variable header: It's a single byte that provides the revision level of the protocol used by the client. With version 3.1, it was 3 then. Moving to the current 3.1.1, it became 4. Starting to write the new specification, the committee decided to align the "marketing" version of the protocol with the "internal" representation on the wire: from 3.1.1 to 5… so from "protocol version" 4 to 5!

You can see it as a really "huge" specification change -- as it really is in terms of new features.

## Properties… Not Only Payload

The "variable header" is changing and now contains some properties. Each property is defined as a key-value pair. Some properties are fixed and used in specific packets like, for example, the "content-type", which describes the type of content in the payload (JSON, XML, …) and the "response topic" used in the new supported request/response pattern (as we'll see in the next paragraphs). There is the possibility to add "user properties" as well so that the developer can add more key-value pairs for bringing values meaningful at the application level: It's an interesting feature because, in some IoT solutions, it could be interesting not sending the payload at all, but rather just values using properties. This aspect is confirmed by the fact that the payload for the PUBLISH message is defined as "optional" now, while it's "required" in the current 3.1.1 specification.

AMQP already had this kind of feature: system properties (i.e. content-type, reply-to, TTL, …) and application properties.

## Error Handling: Now I Know What Really Happened

One of the things missing in the current 3.1.1 specification is support for proper "error handling" at the application level: When there is an error, the server just shuts down the connection and the client doesn't have any possibility to know the reason. In the new specification, pretty much all the packets have a single byte "reason code" as part of the "variable header".

Alongside the "reason code", there is a "reason string" that can be used to provide a more human-readable information about the error.

Such a feature is something that HTTP and AMQP already provided.

## Flow Control for QoS 1 and 2

Flow control is the main feature lacking in the current 3.1.1 specification. It's something that AMQP already had even at different levels (i.e. session window and credits on messages).

The new v5 specification adds a simple flow control based on the "receive maximum" property. With this property, the client can limit the number of QoS 1 and 2 messages that it is willing to process concurrently: It defines a limit quota about the number of PUBLISH messages that can be sent without receiving the acknowledge. There is no flow control for QoS 0 messages because as we know, there is no acknowledgment mechanism for that; the acknowledgment mechanism for QoS 1 and 2 is used by the server for avoiding sending messages to the client; so overwhelming a client with QoS 0 publications is still possible.

## Request/Response Pattern, Here We Are!

The MQTT protocol is well-known for its publish/subscribe nature without any built-in support for the request/response pattern. With 3.1.1, there is no "standard" way for a requester to specify the topic where it expects to receive a response from a responder: It's something that could be encoded inside the message payload. The new v5 introduces the "response topic" property (something that AMQP already had with the "reply-to" system property). Using such property, the requester has a "standard" way to specify the subscribed topic on which it expects replies from a responder.

## Shared Subscriptions

The normal way to work for MQTT is that the broker delivers a received message to ALL subscribers for the topic on which the message is published. Today we can call them "non-shared" subscriptions. The v5 specification adds the "shared subscription" concept: A subscription can be shared among different clients, and the message load will be spread across them. It means that the broker doesn't just send the received message to all subscribers, but to only one of them. Effectively, the clients are something like "competing consumers" on the shared subscription.

A shared subscription is identified using a special topic filter with the following format:

`$share/{ShareName}/{filter}`

Where :

  * $share is needed for specifying that the subscription is shared
  * {ShareName} is the name of the subscription used for grouping clients (it sounds to me something like the "consumer group" in Apache Kafka)
  * {filter} is the topic filter. It's already well-known for "non-shared" subscriptions.

For example, imagine we have publisher P sending messages on topic "/foo" and we have two different applications, A1 and A2, which need to get messages published on this topic for executing different actions (i.e. monitoring, logging, …). Using "non-shared" subscriptions, we can just have A1 and A2 subscribed to the topic "/foo" and start to receive messages from that. If the load on the topic increases and we want to leverage the huge potential we have with cloud-native and containerized applications so that we can spread the load across multiple instances of applications A1 and A2, we can use the "shared" subscriptions in the following way.

From the single topic "/foo" we can move to have :

  * $share/A1/foo
  * $share/A2/foo

All the instances of application A1 can subscribe to the first subscription, and the instances of A2 can subscribe to the second one.

In this way, the A1 instances are competing consumers for messages published on "/foo" and the same for A2 instances. We still have all messages published to both applications, but the load is spread across different instances (of the same application) thanks to the "shared" subscription support.

## Session Management

With MQTT, a session is represented by the subscriptions for a client and any queued messages (when the client isn't online). In the 3.1.1 specification, the "clean session" flag is used by the client for specifying that: the server would delete any existing session and would not save the new session (if set to 1), or the server would need to recover any existing session on client re-connection (if set to 0) and save it on disconnection.

In the new v5, the behavior is changed. First of all, the flag was renamed to "clean start" and if set to 1, it means that the broker would discard any previous session (the client is asking for a "clean" start). Otherwise, it will keep the session (the client is asking not to "clean" the current session).

In addition to this change, the "session expiry interval" property was added (in the CONNECT packet). After the client disconnects, the broker should remove session information for that client when this time is elapsed.

## Delete Please, If You Can't Deliver on Time

Another really interesting property is the "publication expiry interval" that can be set into the PUBLISH message by the client. It's something similar a TTL (Time to Live), as seen in the AMQP protocol. It means that if some amount of time, set with this property, has passed and the server, for any reason, can't deliver the message to subscribers, then it MUST delete this copy of the message.

In IoT, it's really common to use this feature for the "command and control" pattern. In order to avoid that, offline devices start to execute "stale" commands when they come back online: If the command isn't executed in a specified amount of time, it should be never executed.

## Enhanced Authentication

Today, with the 3.1.1 specification, the binary value 1111 for the higher nibble of the first byte in the "fixed header" is forbidden/reserved. That's changed in v5 because it represents the new AUTH packet.

Other than using the already available username/password built-in authentication, the AUTH packet provides a way to use a different authentication mechanism between client and server for including a challenge/response style of authentication; it's something that the AMQP protocol supports with the SASL mechanism, for example.

## Let Others Know That I'm Dead, But… Not Immediately

The "Last Will and Testament" (LWT) is a really cool feature that enables interested clients to know that another client is dead (without sending a "clean" disconnection packet). In the new specification, it's possible to specify a "will delay" so that when the server detects a "not clean" disconnection from a client, it doesn't send the "will message" immediately, but after a delay.

## Keep Alive Timeout? Now the Server Can Decide!

With the current 3.1.1 specification, the client sends a "keep alive timeout" value (in seconds) to the server: It represents the maximum amount of time between two packets sent by the client. If it expires, the server can consider the client dead (by sending the related "will message", for example). Today, the client decided this value (disabling keep alive with a 0 value), but with the new v5, the server can provide a "keep alive timeout" value in the CONNACK packet for the client, meaning that the client MUST use this value instead of the one it sent in the CONNECT packet.

## Miscellaneous

### Password… But No Username

It's now possible to send a password in the CONNECT packet without specifying the corresponding username. This allows you to use the "password" field for credentials and not just for a password.

### Maximum Packet Size

Using the corresponding property, the client can now specify the maximum packet size it can accept.

### Pipelining Messages

The client can now start to send other messages before receiving the CONNACK after sending the CONNECT packet. Of course, it means that if the server is sending the CONNACK with a negative reason code, it MUST NOT process any messages already sent by a client.

Pipelining is one of the features already provided by AMQP, but in a much more powerful way.

### What Identifier Have You Assigned to Me?

We know that the client-id provided by the client upon connection is really useful for maintaining the correlation with session information. It's also allowed to connect providing a "zero length" client-id but in this case, the server will assign such an identifier to the client. Today, the client doesn't receive such information from the server, while with v5, the server provides the assigned client-id using the CONNACK packet.

### I Can't Handle a Higher QoS

Using the "maximum QoS" property in the CONNACK packet, the server can provide the maximum QoS level that it can handle for published messages. It means that if the client sends a packet with a higher QoS, the server will disconnect. The cool thing, with the v5 specification, is that it will do that not just by closing the TCP connection, but by providing a specific reason code (QoS not supported) in the DISCONNECT packet.

### From Topic Name to Alias

A lot of people say that MQTT is lightweight, but they don't think that the topic name is specified in every message sent by the client (it's different from AMQP, where the client "attaches" an address after the connection and can publish without specifying it anymore). The v5 specification adds the concept of a "topic alias" through the corresponding property. It seems to be stolen by the MQTT-SN protocol, which provides a way to assign a single byte identifier to a topic name so that in the subsequent PUBLISH packets, the client can avoid specifying the entire topic name -- but can use such identifier instead (it reduces the packet size).

Cisco is a software company. Surprised? Don't be. [Join DevNet](https://dzone.com/go?i=228255&u=https%3A%2F%2Fdeveloper.cisco.com%2Fsite%2Fdevnet%2Fhome%2F%3Futm_source%3DDZone_bumpertext%26utm_medium%3Dad%26utm_campaign%3Ddnamarketing) to explore APIs, tools, and techniques that developers are using to add collaboration, IoT, security, network priority, and more!
