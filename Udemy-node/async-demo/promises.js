
//function(resolve, reject) sau (resolve,reject) => { }
// CREATE A PROMISE
const p = new Promise((resolve, reject) =>{
    // KICK OFF some async work
    // ...
    // a value or a error
    setTimeout(() => {
        //resolve(1); //pending a promise => resolved, fulfilled
        reject(new Error('message')); //pending a promise => rejected
    }, 2000);
    //resolve(1);
    //reject(new Error('message'));

});

// CONSUME A PROMISE
//p.then(result => console.log('Result', result)); // for succes
p.catch(err => console.log('Error', err.message)); // for err