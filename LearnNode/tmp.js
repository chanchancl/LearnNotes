'use strict';

var fs = require('fs');
var url = require('url');
var path = require('path');
var pug = require('pug');

var host = 'http://www.baidu.com:8000';
var item = 'Game\\233.jpg';

console.log(url.resolve(host,item));

console.log(path.join('d:\\', '123'));

var fun = pug.compile('p #{name}');

console.log(fun({
    "name":233
}));


console.log(decodeURI('/Game/[th10]%20%E4%B8%9C%E6%96%B9%E9%A3%8E%E7%A5%9E%E5%BD%95%20(%E6%B1%89%E5%8C%96%E7%89%88+%E6%97%A5%E6%96%87%E7%89%88)'));
console.log( url.domainToUnicode('/Game/[th10]%20%E4%B8%9C%E6%96%B9%E9%A3%8E%E7%A5%9E%E5%BD%95%20(%E6%B1%89%E5%8C%96%E7%89%88+%E6%97%A5%E6%96%87%E7%89%88)'));
console.log('/Game/[th10]%20%E4%B8%9C%E6%96%B9%E9%A3%8E%E7%A5%9E%E5%BD%95%20(%E6%B1%89%E5%8C%96%E7%89%88+%E6%97%A5%E6%96%87%E7%89%88)');


var arr = [
    {'name':'D:\\360Downloads'},
    {'name':'D:\\360极速浏览器下载'},
    {'name':'D:\\django'},
    {'name':'D:\\Game'}
];

console.log(arr);

arr = arr.sort( function(a,b) {
    console.log(a['name'] > b['name']);
    return a['name'] > b['name'];
});

console.log(arr);