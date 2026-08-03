let score =undefined
console.log( typeof score);
console.log( typeof (score));

let valueInNumber = Number(score)
console.log( typeof score);
console.log( typeof valueInNumber);
console.log(valueInNumber);

//"33"=>33
//"33abc"=>NaN
//true=>1; false=>0


let isLoggedIn = 1

let booleanIsLoggedIn = Boolean(isLoggedIn)
console.log(booleanIsLoggedIn);

let someNumber = 33
let stringSomeNumber = String(someNumber)
console.log(stringSomeNumber); 
console.log(typeof stringSomeNumber); 

//**************operations*******

let value = 3
let negValue = -value
//console.log(negValue);

console.log( 3 + 3); 
console.log( 3 - 3);
console.log( 3 * 3);
console.log( 3 / 3);
console.log( 3 % 3);
console.log( 3 ** 3); //power of 3


let str1 = "Hello"
let str2 = "World"
console.log(str1 + str2);
console.log(str1 + " " + str2);

console.log( 3 + "3"); //33
console.log( "3" + 3); //33
console.log( 3 + 3 + "3"); //63
console.log( "3" + 3 + 3); //333
console.log( 3 + "3" + 3); //333


console.log(+true)
console.log(+"")

let num1, num2, num3 
num1 = num2=num3 = 2+2
let gameCounter = 100
gameCounter++
console.log(gameCounter);

//link to study
// https://tc39.es/ecma262/multipage/abstract-operations.
//html#sec-type-conversion


