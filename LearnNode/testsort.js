
log = console.log

intarray = [5,4,3,2,1]

strarray = [
    {'href': '/迅雷下载'},
    {'href': '/$360'},
    {'href': '/360下载'},
    {'href': '/Game'},
]

dictarray = {
    'dict1': intarray.slice(),
    'dict2': strarray.slice(),
}

intarray.sort()
strarray.sort(function(a,b) {
    return a.href < b.href
})
dictarray.dict1.sort()
dictarray.dict2.sort()

log(intarray)
log(strarray)
log(dictarray)

pug = require('pug')
path = require('path')

var template = pug.compileFile(path.join('.', 'res\\sorttemplate.pug'), {pretty:true})

intarray = [5,4,3,2,1]

items = {
    'beforesort':intarray.slice(),
}

intarray.sort()

items['aftersort'] = intarray


http = require('http')

http.createServer( function(request, response) {
    response.writeHead(200)
    response.write(template(items))
    response.end()
}).listen(8000)

