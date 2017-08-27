"use strict"

let express = require('express');

let bodyParser = require('body-parser');

let redis = require('redis');

let app = express();

let client = new redis.createClient({"host": "redis"}); 

let expire = 2;
if(process.env.EXPIRE) {
  expire = Number(process.env.EXPIRE);
}

app.post("/", (req, res) => {
  console.log("Counting event..");
  client.multi().incr("event_pulse").expire("event_pulse", 2).exec((err, replies) => {
    if(err) {
      console.error(err);
      res.sendStatus(500);
    } else {
      res.sendStatus(200);
    }
  });
});

app.listen(3000, () => {
  console.log("Listening on 3000");
});

