/*
//const p = Promise.resolve({id: 1});
const p = Promise.reject(new Error('reason for rejection...'));
//p.then(result => console.log(result));
p.catch(error => console.log(error));
*/


// running parallel promises
const p1 = new Promise((resolve) => {
    setTimeout(() => {
        console.log('Async operation 1...');
        resolve(1);
    }, 2000);
});

const p2 = new Promise((resolve) => {
    setTimeout(() => {
        console.log('Async operation 2...');
        resolve(2);
    }, 2000);
});

Promise.all([p1,p2])
    .then(result => console.log(result));