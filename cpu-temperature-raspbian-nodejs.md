Read CPU Temperature Raspbian in 1000 (C degree)

$ cat /sys/class/thermal/thermal_zone0/temp

Read it in Node.js

```js
var http = require("http");
var fs =  require("fs");

var server = http.createServer(function(request, response) {

    var temp = fs.readFileSync("/sys/class/thermal/thermal_zone0/temp");
    var temp_c = temp/1000;

    response.writeHead(200, {"Content-Type": "text/plain"});
    response.write("Raspberry Pi cpu temperature: ");
    response.write("\n" + temp);
    response.write("\n" + temp_c);
    response.end();
});
server.listen(8080);
```
