var readings = []
var labels = []

var canvas = document.getElementById('myChart').getContext('2d');

$(document).ready( function () {
	// Set the status message to test javascript functionality
	console.log("javascript on");

	// Set default temperature and humidity values
	updateTemperature(0);
	updateHumidity(90);
	updateDoorState("CLOSED");
	drawGraph(readings, labels);

	// Establish connection via socket io
	console.log("Trying to establish connection");
	var socket = io.connect('http://192.168.43.121:5000');

	socket.on('tempUpdate', function(data) {
		updateTemperature(data);
	});

	socket.on('humUpdate', function(data) {
		var humValue = data.value;
		updateHumidity(humValue);
	});

	socket.on('doorUpdate', function(data) {
		var doorStatus = data;
		updateDoorState(doorStatus);
	});

	socket.on('PhotoUpdate', function(data) {
		var photoStatus = data; 
		updatePhotoState(photoStatus);
	});

	socket.on('intrusionUpdate', function(data) {
		var intrusionValue = data.value;
		updateIntrusionState(intrusionValue);
	});

});

function drawGraph(data, labels) {
	var chartData = {
		labels : labels,
		datasets : [
			{
				fillColor : "rgba(172,194,132,0.4)",
				strokeColor : "#ACC26D",
				pointColor : "#fff",
				pointStrokeColor : "#9DB86D",
				data : data
			}
		]
	}
	Chart.defaults.global.responsive = true;
	Chart.defaults.global.animation = false;
	Chart.defaults.global.scaleOverride = true;

    // ** Required if scaleOverride is true **
    // Number - The number of steps in a hard coded scale
    Chart.defaults.global.scaleSteps = 15;
    // Number - The value jump in the hard coded scale
    Chart.defaults.global.scaleStepWidth = 2;
    // Number - The scale starting value
    Chart.defaults.global.scaleStartValue = 0;

	chart = new Chart(canvas).Line(chartData);
}

function updateTemperature(newValue) {
	console.log("New temp value");
	console.log(newValue);

	document.getElementById("temperatureValue").innerHTML = newValue;

	// Update the temperature data base for the chart
	var d = new Date();
	var current_hour = d.getHours();
	var current_min = d.getMinutes();
	var current_sec = d.getSeconds();
	
	// CHeck if we have 100 elements in the array, if so remove the last one
	if(readings.length >= 20) {
		// Remove the last element
		readings.shift();
		readings.push(newValue);
	} else {
		// Ift here are fewer than 100 elements
		readings.push(newValue);
	}

	// Prepare the label to display
	var label = "";
	label += current_hour.toString();
	if(current_hour < 12) {
		label+=":";
		label+=current_min.toString();
		label+=":";
		label+=current_sec.toString();
		label+="AM";
	} else {
		label+=":";
		label+=current_min.toString();
		label+=":";
		label+=current_sec.toString();
		label += "PM";
	}

	// Similar to readings check if we have 100 elements at present
	if(labels.length >= 20) {
		// Remove the last element (Here the first item in the array)
		labels.shift();
		labels.push(label);
	} else {
		labels.push(label);
	}
	
	// Update the graph
	drawGraph(readings, labels);

}

function updateHumidity(newValue) {
	document.getElementById("humidityValue").innerHTML = newValue;
}

function updateDoorState(state) {
	console.log("New door state : ");
	console.log(state);
	document.getElementById("doorState").innerHTML = state;
}

function updatePhotoState(state) {
	console.log("New photo state : ");
	console.log(state);
	document.getElementById("photoState").innerHTML = state; 
}

function updateIntrusionState(state) {
	document.getElementById("intrusionState").innerHTML = state;
}
