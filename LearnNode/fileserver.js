'use strict';

var fs = require('fs'),
    http = require('http'),
    url = require('url'),
    path = require('path'),
    pug = require('pug'),
    events = require('events');

var RootDirectory = 'D:\\';
var ResourceDirectory = '.\\res\\';

//prepare template

var IndexTemplate = pug.compileFile(path.join(ResourceDirectory, 'index.pug'), {pretty:true});

console.log('Static root dir:' + RootDirectory);

var server = http.createServer(function (request, response) {
    // 收到 http 请求
    //console.log(request.headers['host']);
    var pathname = decodeURI(url.parse(request.url).pathname);
    var localpath = path.join(RootDirectory, pathname);
    var host = request.headers['host'];
    console.log(host);
    if (pathname == '/favicon.ico'){
        response.writeHead(403);
        response.end();
        return;
    }
    if (true) {
        localpath = path.join(RootDirectory, pathname);
        console.log(localpath);
        fs.stat(localpath, function (err, stat) {
            if (err) {
                console.log('404' + err);
                response.writeHead(403);
            } else if (stat.isDirectory()) {
                var dir = localpath;
                fs.readdir(dir, function (err, files) {
                    var event = new events.EventEmitter();
                    event.count = 0;
                    event.end   = files.length;
                    event.items = {
                        "files": [],
                        "dirs": []
                    };

                    for (var i = 0; i < files.length; ++i) {
                        var filepath = path.join(dir, files[i]);
                        var relativepath = path.join(pathname, files[i]);
                        //console.log('A :' + filepath);

                        (function (filepath,relativepath) {
                            fs.stat(filepath, function (err, stat) {
                                //console.log('    B : ' + filepath);
                                if (err) {
                                    console.warn(err);
                                } else if (stat.isFile()) {
                                    //console.log(filepath);
                                    event.items['files'].push({
                                        "href": url.resolve('/', relativepath),
                                        "path": relativepath
                                    });
                                } else if (stat.isDirectory()) {
                                    //console.log(filepath);
                                    event.items['dirs'].push({
                                        "href": url.resolve('/', relativepath),
                                        "path": relativepath
                                    });
                                } 
                                event.emit('onfile');
                            });
                        })(filepath,relativepath);
                    }

                    event.on('onfile', function () {
                        this.count += 1;
                        if (this.count == this.end) {

                            this.items['dirs'].sort();
                            this.items['files'].sort();
                            console.log(this.items.dirs);


                            response.writeHead(200, {
                                "Content-Type": "text/html"
                            });
                            response.write(IndexTemplate({
                                "items": this.items,
                            }));
                            response.end();
                            this.removeAllListeners('onfile');
                        }
                    });

                });
            } else if (stat.isFile()) {

            }
        });
    }

});

server.listen(8000);