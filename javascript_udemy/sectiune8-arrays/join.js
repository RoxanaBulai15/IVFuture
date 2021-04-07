const prices = [10.99, 5.99, 3.99, 6.59];
const tax = 0.19;

const taxAdjustedPrices = prices.map((price, idx, prices) => {
    const priceObj = { index: idx, taxAdjPrice: price * (1 + tax) };
    return priceObj;
});

// console.log(prices, taxAdjustedPrices);

const sortedPrices = prices.sort((a, b) => {
    if (a > b) {
        return -1;
    } else if (a === b) {
        return 0;
    } else {
        return 1;
    }
});
// console.log(sortedPrices.reverse());
console.log(sortedPrices);

const filteredArray = prices.filter(p => p > 6);

console.log(filteredArray);

// let sum = 0;

// prices.forEach((price) => {
//   sum += price
// });

// console.log(sum);

const sum = prices.reduce((prevValue, curValue) => prevValue + curValue, 0);

console.log(sum);

const data = 'new york;10.99;2000';

const transformedData = data.split(';');
transformedData[1] = +transformedData[1];
console.log(transformedData);

const nameFragements = ['Max', 'Schwarz'];
const name = nameFragements.join(' ');
console.log(name);