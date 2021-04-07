const defaultResult = 0;
let currentResult = defaultResult;
let logEntries = [];

// Get input from input field
function getUserInput(){
  return parseInt(userInput.value);
}

// Generate and write calculation log
function createAndWriteOutput(operator, resultBeforeCalc, calcNumber){
  const calcDescription = `${resultBeforeCalc} ${operator} ${calcNumber}`;
  outputResult(currentResult, calcDescription); // from vendor file
}

function calculateResult(calculationType){
  const enteredNumber = getUserInput();
  const initialResult = currentResult;
  let mathOperator;
  if (calculationType === 'ADD'){
    currentResult += enteredNumber;
    mathOperator = '+';
  } else if (calculationType === 'SUBTRACT') {
    currentResult -= enteredNumber;
    mathOperator = '-';
  }
  currentResult += enteredNumber;
  createAndWriteOutput(mathOperator, initialResult, enteredNumber);
  //writeToLog(calculationType, initialResult, enteredNumber);
}

// ADD

function add() {
  /*
  //const enteredNumber = parseInt(userInput.value);
  const enteredNumber = getUserInput();
  const initialResult = currentResult;
  //const calcDescription = `${currentResult} + ${userInput.value.toString()}`

  //currentResult = currentResult + enteredNumber;
  currentResult += enteredNumber;
  createAndWriteOutput('+', initialResult, enteredNumber);
  const logEntry = {
    operation: 'ADD',
    prevResult: initialResult,
    number: enteredNumber,
    result: currentResult

   */
  calculateResult('ADD');

  //logEntries.push(logEntry);
  //console.log(logEntries);
}

// SUBSTRACT

function subtract(){
  /*const enteredNumber = getUserInput();
  const initialResult = currentResult;
  //currentResult = currentResult - enteredNumber;
  currentResult -= enteredNumber;
  createAndWriteOutput('-', initialResult, enteredNumber);
  const logEntry = {
    operation: 'SUBSTRACT',
    prevResult: initialResult,
    number: enteredNumber,
    result: currentResult
  };
  logEntries.push(logEntry);
  console.log(logEntries);*/
  calculateResult('SUBTRACT');
}

// MUTIPLY

function multiply(){
  const enteredNumber = getUserInput();
  const initialResult = currentResult;
  //currentResult = currentResult * enteredNumber;
  currentResult *= enteredNumber;
  createAndWriteOutput('*', initialResult, enteredNumber);
  const logEntry = {
    operation: 'MULTIPLY',
    prevResult: initialResult,
    number: enteredNumber,
    result: currentResult
  };
  logEntries.push(logEntry);
  console.log(logEntries);
}

// DIVIDE

function divide() {
  const enteredNumber = getUserInput();
  const initialResult = currentResult;
  //const calcDescription = `${currentResult} + ${userInput.value.toString()}`
  //currentResult = currentResult / enteredNumber;
  currentResult /= enteredNumber;
  createAndWriteOutput('/', initialResult, enteredNumber);
  const logEntry = {
    operation: 'DIVIDE',
    prevResult: initialResult,
    number: enteredNumber,
    result: currentResult
  };
  logEntries.push(logEntry);
  console.log(logEntries);
}


//That's when you don't directly call the function but when you instead just provide JavaScript with the name of the function.

//=> someButton.addEventListener('click', add);

//This snippet would tell JavaScript: "Hey, when the button is clicked, go ahead and execute add.".

// !!! someButton.addEventListener('click', add()); would be wrong.
addBtn.addEventListener('click', add);
subtractBtn.addEventListener('click', subtract);
multiplyBtn.addEventListener('click',multiply);
divideBtn.addEventListener('click', divide);


// DATA TYPES
//*numbers
//*strings(text)
//*booleans
//*objects: {name:'Max', age: 31} (key:value) --- hepl you with organizing data
//*arrays:

// logEntries
// for each operation: logEntries.push(enteredNumber);

// OBJECTS

//A couple of important things:

// 1. You use {} to "group the data" - a semicolon (;) is used after the closing }. On functions, we didn't do that. As a rule of thumb, you can keep in mind that a semicolon is used after {} if the {} are on the right side of the equal sign!

// 2. key-value pairs are separated via a comma (,), NOT via a semicolon. Using a semicolon inside of an object (i.e. between {}), would be a syntax error!

// 3. Values are assigned to keys/ properties via a colon (:), NOT via an equal sign (=). Using an equal sign inside of an object (i.e. between {}), would be a syntax error!


// CONTROL STRUCTURES

// attack function

// const ATTACK_VALUE = 10;
// let chosenMaxLife = 100;
// let currentMonsterHealth = chosenMaxLife;

// adjustHealthBars(chosenMaxLife);
// function attackHandler(){
// const damage = dealMonsterDamage(ATTACK_VALUE;
// currentMonsterHealth -= damage;
// }

// attackBtn.addEventListener('click', attackHandler);

// switch case statement

// introducing loops
// *for loop --> execute code for certain amount of time
// *for-of loop --> execute code for every element in array
// *for-in loop --> execute for every key in an object
// *while loop --> execute code as long as a condition is true

// ! control loops with BREAK