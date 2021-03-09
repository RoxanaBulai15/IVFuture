//Representational State Transfer

// CRUD

// O Companie VIdly pentru inchirierea de filme.
// http://vidly.com/api/customers
// https://vidly.com/api/customers

//HTTP methods: get, post, put, delete

// GET A CUSTOMER

// TO GET THE LIST OF ALL CUSTOMERS
// GET /api/customers --> array of customers

// TO GET A SINGLE CUSTOMER
// GET /api/customers/1 --> { id: 1, name: ''}

// UPDATE A CUSTOMER
// PUT /api/customers/1
// { name: ''}

// DELETE A CUSTOMER
// DELETE /api/customers/1

// CREATE A CUSTOMER
// POST /api/customers
// { name: ''} --> { id: 1, name: ''}

const http = require('http');

const server = http.createServer((req, res) => {
    if(req.url === '/') {
        res.write("Hello World");
        res.end();
    }

    if(req.url === '/api/courses') {
        res.write(JSON.stringify([1, 2, 3]));
        res.end();
    }
});

server.listen(3000);

console.log('Litening on por 3000...');
