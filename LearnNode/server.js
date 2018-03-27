'use strict';

var http = require('http');
var fs   = require('fs');


var data = null;
fs.readFile('sample.txt', 'utf-8',function(err, data) {
    global.data = data;
});

var server = http.createServer(function(request, response) {
    console.log(request.method + ' : ' + request.url);
    response.writeHead(200, {'Content-Type': 'text/html'});
    
    response.write('<h1>');
    response.write(global.data);
    response.write('</h1>');

    response.end();
});

server.listen(8000);

console.log('Server is runing at http://localhost:8000');