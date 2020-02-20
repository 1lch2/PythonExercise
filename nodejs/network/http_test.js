var http = require('http');

// Opens an HTTP server on 8888 port.
http.createServer(
    function (request, response){
        response.writeHead(
            200,
            { 
                'content-type': 'text/plain'
            }
        );
        response.end('Hellow world.\n');
    }
).listen(8888);