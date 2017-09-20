/**
 * Created by Massimiliano Fanciulli on 27/07/15.
 * If you need any information write me at fanciulli@gmail.com
 */
var fs=require('fs-extra');
var Multimap = require('multimap');

module.exports=Config;

function Config()
{
    var self=this;

    self.autosave=true;
    self.autosaveDelay=1000;
    self.saved=true;
    self.data={};

    self.callbacks=new Multimap();
}


/**
 *
 * @param file
 */
Config.prototype.loadFile=function(file)
{
    var self=this;

    self.filePath=file;

    try
    {
        self.data=fs.readJsonSync(file);
    }
    catch(ex)
    {
        self.data={};
        console.log('Error reading configuration. Defaulting to empty configuration');
    }

}

/**
 *
 * @param key
 * @returns {{}|*}
 */
Config.prototype.findProp=function(key)
{
    var self=this;

    if(key==undefined)
        return self.data;
    else
    {
        var splitted=key.split('.');
        var currentProp=self.data;

        while (splitted.length > 0) {
            var k = splitted.shift();

            if(currentProp && currentProp[k]!=undefined)
                currentProp=currentProp[k];
            else
            {
                currentProp=null;
                break;
            }
        }

        return currentProp;
    }
}

/**
 * This method returns true or false depending on the existence of a key in the configuration file
 * @param key Key to check
 * @returns {boolean} True if key exists, false otherwise
 */
Config.prototype.has=function(key)
{
    var self=this;

    return self.findProp(key)!=null;
}


Config.prototype.get=function(key)
{
    var self=this;
    var prop=self.findProp(key);

    if(prop!=undefined)
        return self.forceToType(prop.type,prop.value);
}

Config.prototype.set=function(key,value)
{
    var self=this;
    var prop=self.findProp(key);

    if(prop!=undefined)
    {
        prop.value=self.forceToType(prop.type,value);
        self.scheduleSave();
    }

    self.callbacks.forEach(function (callback, ckey) {
        if(key==ckey)
        {
            callback(value);
        }
    });

}

Config.prototype.scheduleSave=function()
{
    var self=this;

    if(self.filePath!=undefined)
    {
        self.saved=false;

        setTimeout(function()
        {
            self.save();
        },self.autosaveDelay);
    }

}

Config.prototype.save=function()
{
    var self=this;

    if(self.saved==false)
    {
        self.saved=true;
        fs.writeJsonSync(self.filePath,self.data);
    }
}

Config.prototype.addConfigValue=function(key,type,value)
{
    var self=this;

    var splitted=key.split('.');
    var currentProp=self.data;

    while (splitted.length > 0) {
        var k = splitted.shift();

        if(currentProp && currentProp[k]!=undefined)
            currentProp=currentProp[k];
        else
        {
            currentProp[k]={};
            currentProp=currentProp[k];
        }
    }

    var prop=self.findProp(key);
    self.assertSupportedType(type);
    prop['type']=type;


    prop['value']=self.forceToType(type,value);

    self.scheduleSave();
}

Config.prototype.assertSupportedType=function(type)
{
    if(type != 'string' && type!='boolean' && type!='number' && type!='array')
    {
        throw Error('Type '+type+' is not supported');
    }
}

Config.prototype.forceToType=function(type,value)
{
    if(type=='string')
    {
        return ''+value;
    }
    else if(type=='boolean')
    {
        return Boolean(value);
    }
    else if(type=='number')
    {
        var i = Number(value);
        if(Number.isNaN(i))
            throw  Error('The value '+value+' is not a number');
        else return i;
    }
    else return value;

}

Config.prototype.print=function()
{
    var self=this;

    console.log(JSON.stringify(self.data));
}

/**
 * This method searches for the key and deletes it
 * @param key
 */
Config.prototype.delete=function(key)
{
    var self=this;

    if(self.has(key))
    {
        var splitted=key.split('.');

        if(splitted.length==1)
            delete self.data[key];
        else
        {
            var parentKey=self.data;
            for(var i=0;i< splitted.length;i++)
            {
                var k = splitted.shift();
                parentKey=parentKey[k];
            }

            var nextKey=splitted.shift();
            delete parentKey[nextKey];
        }

        self.scheduleSave();
    }

    self.callbacks.delete(key);
}

Config.prototype.getKeys=function(parentKey)
{
    var self=this;

    var parent=self.findProp(parentKey);

    if(parent!=undefined && parent!=null)
        return Object.keys(parent);
    else return Object.keys(self.data);
}

Config.prototype.registerCallback=function(key,callback)
{
    var self=this;

    self.callbacks.set(key,callback);
}
