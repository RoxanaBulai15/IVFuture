const numbers = [1,2,3];
console.log(numbers);

const moreNumbers = Array(5,2);
console.log(moreNumbers);

const yetMoreNumbers = Array.of(1,2);
console.log(yetMoreNumbers);

const moreMoreNumbers = Array.from([1,2,3]);
console.log(moreMoreNumbers);

const listItems = document.querySelectorAll('li');
console.log(listItems);

const array = Array.from("Hi!");
console.log(array);

const hobbies = ['Sports', 'Cooking'];
hobbies.push('Reading'); // adauga la final
hobbies.unshift('Reading'); // adauga la inceput
console.log(hobbies);
hobbies.pop(); //sterge ult element
console.log(hobbies);

// alternative to for loops: forEach()

const data = 'analiza;reala;9';
const transformedData = data.split(';');
console.log(transformedData);

const nameFragments = ['Roxana', 'Bulai'];
const name = nameFragments.join(' ');
console.log(name);

const newName = [...nameFragments];
console.log(newName);

const [firstName, lastName] = nameFragments;
console.log(firstName);
console.log(lastName);

// ARRAYS: store (nested) data of any kind and length
//         iterable, also many special arrays methods available
//         order is guaranteed, duplicates are allowed, zero-based index to access elements

// SETS: store (nested) data of any kind and length
//       iterable, also many special set methods available
//       order is NOT guaranteed, duplicates are NOT allowed, no index-based access
// MAPS: store key-value data of any kind and length, any keys, values are allowed
//       iterable, also many special map methods available
//       order is guaranteed, duplicate keys are not allowed, key-based access

// WeakSet
let person = {name: 'Roxana'};
const persons = new WeakSet();
persons.add(person);

// ... some operations
// person = null;
console.log(persons);

// WeakMap
const personData = new WeakMap();
personData.set(person, 'Extra info!');

person = null;

console.log(personData);