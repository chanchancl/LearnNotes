'use strict';

var fs = require('fs');

fs.readFile('sample.txt', function(err, data) {
    console.log('异步文件读取完毕，调用回调函数。');
    if (err) {
        console.log(err);
    } else {
        console.log(data.toString('utf-8'));
    }
});

console.log('异步文件读完了吗？');


var data = fs.readFileSync('sample.txt', 'utf-8');
console.log('同步读文件');
console.log(data)


fs.stat('sample.txt', function(err, stat) {
    if (err) {
        console.log(err);
    } else {
        console.log('isFile : ' + stat.isFile());
        console.log('isDirectory : ' + stat.isDirectory());
        if (stat.isFile()) {
            console.log('size : ' + stat.size);
            console.log('birth time : ' + stat.birthtime);
            console.log('last modify : ' + stat.mtime);
        }
    }
});



var rs = fs.createReadStream('sample.txt', 'utf-8');

rs.on('data', function(chunk) {
    console.log('DATA : ');
    console.log(chunk);
});

rs.on('end', function() {
    console.log('END');
});

rs.on('error', function(err) {
    console.log('ERROR: ' + err);
});


rs =  fs.createReadStream('sample.txt');
var ws = fs.createWriteStream('copied.txt');

rs.pipe(ws);