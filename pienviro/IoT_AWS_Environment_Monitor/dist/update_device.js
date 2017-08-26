var args = process.argv.slice(2);
var keyPath=args[0];
var certPath=args[1];
var caPath=args[2];
var clientId=args[3];
var region=args[4];
var temperature=args[5];
var humidity=args[6];
var pressure=args[7];
var luminosity=args[8];
var spl=args[9];

console.log("keyPath: "+keyPath);
console.log("certPath: "+certPath);
console.log("caPath: "+caPath);
console.log("clientId: "+clientId);
console.log("region: "+region);
console.log("humidity: "+humidity);
console.log("temperature: "+temperature);
console.log("pressure: "+pressure);
console.log("luminosity: "+luminosity);
console.log("spl: "+spl);

var awsIot = require('aws-iot-device-sdk');

var thingName = clientId;

var thingShadows = awsIot.thingShadow({
   keyPath: keyPath,
  certPath: certPath,
    caPath: caPath,
  clientId: clientId,
    region: region
});

shadowState = {
  "state": {
    "reported": {
      "humidity": "0",
      "temperature": "0",
      "pressure":"0",
      "luminosity":"0",
      "spl":"0"
    }
  }
}


shadowState["state"]["reported"]["humidity"] = humidity;
shadowState["state"]["reported"]["temperature"] =temperature;
shadowState["state"]["reported"]["pressure"] =pressure;
shadowState["state"]["reported"]["luminosity"] =luminosity;
shadowState["state"]["reported"]["spl"] =spl;



thingShadows.on('connect', function() {
  thingShadows.register( thingName );

  setTimeout( function() {
   thingShadows.update(thingName, shadowState);
  }, 2500 );


  thingShadows.on('status',
    function(thingName, stat, clientToken, stateObject) {
       console.log(stat+":"+JSON.stringify(stateObject));
       process.exit();
    });

});
