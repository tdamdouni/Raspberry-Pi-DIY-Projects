/**
 * Created by massi on 27/07/15.
 */
var config=new (require(__dirname+'/index.js'))();
var configB=new (require(__dirname+'/index.js'))();


config.loadFile(__dirname+'/testConfig.json');

console.log(config.get("callback.b"));
config.set("callback.b","ACCITUA");
config.save();
configB.loadFile(__dirname+'/testConfig.json');
console.log("THIS SHOULD BE DIFFERENT FROM BBB   "+config.get("callback.b"));
console.log("THIS SHOULD BE DIFFERENT FROM BBB   "+configB.get("callback.b"));



console.log("KEYS: "+config.getKeys());
console.log("KEYS: "+config.getKeys('keys'));

var keys=config.getKeys('keys.fifth');
console.log("KEYS: "+keys);

for( var i in keys)
    console.log(keys[i]);

console.log("VALUE "+config.get('debug'));
console.log("VALUE "+config.get('env'));
console.log("VALUE "+config.get('structured.a'));
console.log("VALUE "+config.get('structured.b'));

config.set('debug',true);
config.set('env',"PRODUCTION");
config.set('structured.a',500);
config.set('structured.b',1000);

console.log("VALUE "+config.get('debug'));
console.log("VALUE "+config.get('env'));
console.log("VALUE "+config.get('structured.a'));
console.log("VALUE "+config.get('structured.b'));



console.log("VALUE "+config.get('music_services.dirble.enabled'));
config.addConfigValue('music_services.dirble.enabled','boolean',false);
console.log("VALUE "+config.get('music_services.dirble.enabled'));


console.log("THIS VALUE SHALL BE FALSE: "+config.has('not.existing.key'));
config.delete('delete.fifth.sub-key-1');
console.log("VALUE "+config.get('delete.fifth.sub-key-2'));

config.print();





config.registerCallback('callback.a',function(value)
{
    console.log("This is callabck A #1. New value is "+value);
});

config.registerCallback('callback.b',function(value)
{
    console.log("This is callabck B. New value is "+value);
});


config.set('callback.a','New value');

config.registerCallback('callback.a',function(value)
{
    console.log("This is callabck A #2. New value is "+value);
});
config.set('callback.a','Asganau');

config.delete('callback.a');
config.addConfigValue('callback.a','string',"PIPPO");
config.set('callback.a','AAAA');
config.print();

config.registerCallback('callback.a',function(value)
{
    console.log("You should see only this callback. Value: "+value);
});
config.set('callback.a','########');
config.print();

config.set('callback.b','BBB');