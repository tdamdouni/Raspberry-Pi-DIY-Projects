# Don't Pipe to your Shell

_Captured: 2017-08-27 at 11:06 from [www.seancassidy.me](https://www.seancassidy.me/dont-pipe-to-your-shell.html)_

Piping wget or curl to bash or sh is stupid. Like this:
    
    
    wget -O - http://example.com/install.sh | sudo sh
    

[It's](https://github.com/saltstack/salt-bootstrap) [everywhere](https://github.com/isaacs/npm/issues/1641). Sometimes they tell you to ignore certificates as well (looking at you, Salt). That's dumb.

The main reason I think it's dumb (other than running arbitrary commands on your machine that could change based on user agent to trick you) is its failure mode.

What happens if the connection closes mid stream? Let's find out.
    
    
    (echo -n "echo \"Hello\""; cat) | nc -l -p 5555
    

This will send a command to whoever connects, but won't send the newline. Then, it'll hang. Let's connect the client:

At first, nothing happens. Great. What will happen if we kill -9 the listening netcat? Will sh execute the partial command in its buffer?

Yes.

But what about wget, or curl?
    
    
    wget -O - http://localhost:5555 | sh
    --2013-10-31 16:22:38--  http://localhost:5555/
    Resolving localhost (localhost)... 127.0.0.1
    Connecting to localhost (localhost)|127.0.0.1|:5555... connected.
    HTTP request sent, awaiting response... 200 No headers, assuming HTTP/0.9
    Length: unspecified
    Saving to: `STDOUT'
    
        [          <=>                                                  ] 12          --.-K/s   in 8.6s
    
    2013-10-31 16:22:47 (1.40 B/s) - written to stdout [12]
    
    Hello
    

What if that partial command wasn't a harmless echo but instead one of these:
    
    
    TMP=/tmp
    TMP_DIR=`mktemp`
    rm -rf $TMP_DIR
    

Harmless, right? And what if the connection closes immediately after 'rm -rf $TMP' is sent? It'll delete everything in the temp directory, which is certainly harmful.

This might be unlikely, but the results of this happening, even once, could be catastrophic.

Friends don't let friends pipe to sh.

_Update_: I updated the last example because it really made no sense. Thanks to [player2](http://www.reddit.com/r/programming/comments/1pnkxs/dont_pipe_to_your_shell/cd442fz) and [ZackMcAck](http://www.reddit.com/r/programming/comments/1pnkxs/dont_pipe_to_your_shell/cd44pjw) on reddit.
