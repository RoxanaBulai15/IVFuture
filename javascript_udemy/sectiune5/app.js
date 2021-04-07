/*
var name = 'Max';
//let name = "Ana"; // error

//correct
//var name = 'Max';
//var name = 'Anna';

if (name === 'Max'){
    var hobbies = ['Sports', 'Cooking'];
    console.log(hobbies);
}

function greet(){
    var age = 30;
    var name = 'Manuel';
    console.log(name, age);
}

// console.log(name,age); error age
console.log(name);
greet();
*/

// var has global/ function (local) scope
// let and const have block scope

// BLOCK SCOPE
//=variables are created in a block {} and then belong to that block.
// Hence if statements and for-loops can also have their own, scoped variables for example.



/*'use strict';

const userName = 'Max';
var undefined = 5;

console.log(userName);*/

function getName(){
    return prompt('Your name: ', '');
}

function greet(){
    const userName = getName();
    console.log('Hello, ' + userName);
}

greet();


// 1. The JavaScript language
// 2. Browser APIs