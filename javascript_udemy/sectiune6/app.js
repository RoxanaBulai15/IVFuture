const startGameBtn = document.getElementById('start-game-btn');

/*start(); //it s ok
function start(){
    console.log('eeeee');
}*/

/*function startGame(){
    console.log('Game is starting...');
}*/

/*const start = function(){
    console.log('Game is starting...');
}*/
/*start(); error

const start = function startGame(){
    console.log('Game is starting...');
};*/

/*const person = {
    name: 'Max',
    greet: function greet(){
        console.log('Hello there!');
    }
};*/
// name is a property
// greet is a method because it has a function
// person.greet();

//console.log(typeof startGame());
//console.dir(startGame);
// functions are OBJECTS

const ROCK = 'ROCK';
const PAPER = 'PAPER';
const SCISSORS = 'SCISSORS';
const default_ser_choice = ROCK;
const RESULT_DRAW = 'DRAW';
const RESULT_PLAYER_WINS = 'PLAYER_WINS';
const RESULT_COMPUTER_WINS = 'COMPUTER_WINS';

let gameIsRunning = false;

const getPlayerChoice = function(){
    const selection = prompt(`${ROCK}, ${PAPER} or ${SCISSORS}?`, '').toUpperCase();

    if (
        selection !== ROCK &&
        selection !== PAPER &&
        selection !== SCISSORS){
        alert(`Invalid choice! We choose ${default_ser_choice} for you!`);
        return default_ser_choice;
    }
    return selection;
}

const getComputerChoice = function(){
    const randomValue = Math.random();
    if (randomValue < 0.34){
        return ROCK;
    } else if (randomValue < 0.67){
        return PAPER;
    } else {
        return SCISSORS;
    }
};

/*const getWinner = function(cChoice, pChoice){
    if (pChoice === cChoice){
        return RESULT_DRAW;
    } else if(
        cChoice === ROCK && pChoice === PAPER ||
        cChoice === PAPER && pChoice ===SCISSORS ||
        cChoice === SCISSORS && pChoice === ROCK)
    {
        return RESULT_COMPUTER_WINS;
    } else{
        return RESULT_PLAYER_WINS;
    }
}*/


const add = (a, b) => a+b;

const add2 = function(a,b) {
    return a+b;
}

const getWinner = (cChoice, pChoice) =>
    pChoice === cChoice ? RESULT_DRAW: (cChoice === ROCK && pChoice === PAPER ||
        cChoice === PAPER && pChoice ===SCISSORS ||
        cChoice === SCISSORS && pChoice === ROCK) ? RESULT_PLAYER_WINS : RESULT_COMPUTER_WINS;

   /* if (pChoice === cChoice){
        return RESULT_DRAW;
    } else if(
        cChoice === ROCK && pChoice === PAPER ||
        cChoice === PAPER && pChoice ===SCISSORS ||
        cChoice === SCISSORS && pChoice === ROCK)
    {
        return RESULT_PLAYER_WINS;
    } else{
        return RESULT_COMPUTER_WINS;
    }*/

// anonymous function
startGameBtn.addEventListener('click', function(){
    if(gameIsRunning){
        return;
    }

    gameIsRunning = true;

    console.log('Game is starting...');
    const playerSelection = getPlayerChoice();
    const computerChoice = getComputerChoice();
    const winner = getWinner(computerChoice, playerSelection);
    console.log(winner);
}); // indirect execution
//startGame(); // direct execution

