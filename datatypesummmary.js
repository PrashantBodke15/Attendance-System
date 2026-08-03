// ******primitive data types********
// number
// string
// boolean
// null
// undefined
// symbol
// bigint

const { useInsertionEffect } = require("react")

// const score = 100
// const scoreValue = 100.5
// const isLoggedIn = true
// const outsideTemp = null
// let userEmail; //undefined

// const id = Symbol('123')
// const anotherId = Symnbol('124')


// """"reference data types"""(non-primitive data types)
// arrays, objects, functions

// const bigInt = 9007199254740991n

// const heros = ['shaktiman', 'naagraj', 'doga']
// let myObj = {
//     name:"prashant",
//     age: 22,

// }

// const myFunction = function(){
//     console.log("hello world");
// }

// console.log(typeof myFunction)


//https:262.ecma-international.otg/5.1/#sec-11.4.3

//***************************************8 */

// stack (primitive), heap (non-primitive)

let myYoutubename = "prashant"
let anotherName = myYoutubename
anotherName = "prashant kumar"
console.log(myYoutubename)
console.log(anotherName)

let user = {
    email:"prashant@example.com",
    upi: "prashant@upi"

}

let usertwo = user
usertwo.email = "kumar@example.com"
console.log(user.email)
console.log(usertwo.email)
