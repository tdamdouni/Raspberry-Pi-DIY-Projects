'use strict';

var libQ = require('kew');
var fs = require('fs-extra');
var Gpio = require('onoff').Gpio;
var io = require('socket.io-client');
var socket = io.connect('http://localhost:3000');
var actions = ["playPause", "volumeUp", "volumeDown", "previous", "next", "shutdown"];

module.exports = GPIOButtons;

function GPIOButtons(context) {
	var self = this;
	self.context=context;
	self.commandRouter = self.context.coreCommand;
	self.logger = self.context.logger;
	self.triggers = [];
}


GPIOButtons.prototype.onVolumioStart = function () {
	var self = this;

	var configFile=this.commandRouter.pluginManager.getConfigurationFile(this.context,'config.json');
	this.config = new (require('v-conf'))();
	this.config.loadFile(configFile);

	self.logger.info("GPIO-Buttons initialized");
	
	return libQ.resolve();	
};


GPIOButtons.prototype.getConfigurationFiles = function()
{
	return ['config.json'];
};


GPIOButtons.prototype.onStart = function () {
	var self = this;
	var defer=libQ.defer();

	self.createTriggers()
		.then (function (result) {
			self.logger.info("GPIO-Buttons started");
			defer.resolve();
		});
	
    return defer.promise;
};


GPIOButtons.prototype.onStop = function () {
	var self = this;
	var defer=libQ.defer();

	self.clearTriggers()
		.then (function (result) {
			self.logger.info("GPIO-Buttons stopped");
			defer.resolve();
		});
	
    return defer.promise;
};


GPIOButtons.prototype.onRestart = function () {
	var self = this;
};

GPIOButtons.prototype.onInstall = function () {
	var self = this;
};

GPIOButtons.prototype.onUninstall = function () {
	var self = this;
};

GPIOButtons.prototype.getConf = function (varName) {
	var self = this;
};

GPIOButtons.prototype.setConf = function(varName, varValue) {
	var self = this;
};

GPIOButtons.prototype.getAdditionalConf = function (type, controller, data) {
	var self = this;
};

GPIOButtons.prototype.setAdditionalConf = function () {
	var self = this;
};

GPIOButtons.prototype.setUIConfig = function (data) {
	var self = this;
};


GPIOButtons.prototype.getUIConfig = function () {
	var defer = libQ.defer();
	var self = this;

	self.logger.info('GPIO-Buttons: Getting UI config');

	//Just for now..
	var lang_code = 'en';

	//var lang_code = this.commandRouter.sharedVars.get('language_code');

        self.commandRouter.i18nJson(__dirname+'/i18n/strings_'+lang_code+'.json',
                __dirname+'/i18n/strings_en.json',
                __dirname + '/UIConfig.json')
        .then(function(uiconf)
        {

			var i = 0;
			actions.forEach(function(action, index, array) {
 				
 				// Strings for config
				var c1 = action.concat('.enabled');
				var c2 = action.concat('.pin');
				
				// accessor supposes actions and uiconfig items are in SAME order
				// this is potentially dangerous: rewrite with a JSON search of "id" value ?				
				uiconf.sections[0].content[2*i].value = self.config.get(c1);
				uiconf.sections[0].content[2*i+1].value.value = self.config.get(c2);
				uiconf.sections[0].content[2*i+1].value.label = self.config.get(c2).toString();

				i = i + 1;
			});

            defer.resolve(uiconf);
		})
        .fail(function()
        {
            defer.reject(new Error());
        });

        return defer.promise;
};


GPIOButtons.prototype.saveConfig = function(data)
{
	var self = this;

	actions.forEach(function(action, index, array) {
 		// Strings for data fields
		var s1 = action.concat('Enabled');
		var s2 = action.concat('Pin');

		// Strings for config
		var c1 = action.concat('.enabled');
		var c2 = action.concat('.pin');
		var c3 = action.concat('.value');

		self.config.set(c1, data[s1]);
		self.config.set(c2, data[s2]['value']);
		self.config.set(c3, 0);
	});

	self.clearTriggers()
		.then(self.createTriggers());

	self.commandRouter.pushToastMessage('success',"GPIO-Buttons", "Configuration saved");
};


GPIOButtons.prototype.createTriggers = function() {
	var self = this;

	self.logger.info('GPIO-Buttons: Reading config and creating triggers...');

	actions.forEach(function(action, index, array) {
		var c1 = action.concat('.enabled');
		var c2 = action.concat('.pin');

		var enabled = self.config.get(c1);
		var pin = self.config.get(c2);

		if(enabled === true){
			self.logger.info('GPIO-Buttons: '+ action + ' on pin ' + pin);
			var j = new Gpio(pin,'in','both');
			j.watch(self.listener.bind(self,action));
			self.triggers.push(j);
		}
	});
		
	return libQ.resolve();
};


GPIOButtons.prototype.clearTriggers = function () {
	var self = this;
	
	self.triggers.forEach(function(trigger, index, array) {
  		self.logger.info("GPIO-Buttons: Destroying trigger " + index);

		trigger.unwatchAll();
		trigger.unexport();		
	});
	
	self.triggers = [];

	return libQ.resolve();	
};


GPIOButtons.prototype.listener = function(action,err,value){
	var self = this;

	var c3 = action.concat('.value');
	var lastvalue = self.config.get(c3);

	// IF change AND high (or low?)
	if(value !== lastvalue && value === 1){
		//do thing
		self[action]();
	}
	// remember value
	self.config.set(c3,value);
};





//Play / Pause
GPIOButtons.prototype.playPause = function() {
  //this.logger.info('GPIO-Buttons: Play/pause button pressed');
  socket.emit('getState','');
  socket.once('pushState', function (state) {
    if(state.status=='play' && state.service=='webradio'){
      socket.emit('stop');
    } else if(state.status=='play'){
      socket.emit('pause');
    } else {
      socket.emit('play');
    }
  });
};

//next on playlist
GPIOButtons.prototype.next = function() {
  //this.logger.info('GPIO-Buttons: next-button pressed');
  socket.emit('next')
};

//previous on playlist
GPIOButtons.prototype.previous = function() {
  //this.logger.info('GPIO-Buttons: previous-button pressed');
  socket.emit('prev')
};

//Volume up
GPIOButtons.prototype.volumeUp = function() {
  //this.logger.info('GPIO-Buttons: Vol+ button pressed');
  socket.emit('volume','+');
};

//Volume down
GPIOButtons.prototype.volumeDown = function() {
  //this.logger.info('GPIO-Buttons: Vol- button pressed\n');
  socket.emit('volume','-');
};

//shutdown
GPIOButtons.prototype.shutdown = function() {
  // this.logger.info('GPIO-Buttons: shutdown button pressed\n');
  this.commandRouter.shutdown();
};
