

function sayMyame(){
console.log("p");
console.log("r");
console.log("a");
console.log("s");
console.log("h");
console.log("a");
console.log("n");
console.log("t");

}
//sayMyame();



function addTwoNumbers(number1,number2){
    console.log(number1+number2)
}
//addTwoNumbers(4,6)




function loginusermessege(username){
    if(username === undefined){
        console.log("please enter a username");
        return
    }
    return`${username} just logged in`
}
 //console.log(loginusermessege("prashnat"))
//console.log(loginusermessege())



function calculatorcarprice(...num1){
    return num1

}
//console.log(calculatorcarprice(434,3434,33,))


const user ={
    username:"prashnat",
    prices:199
}
function handleobject(anyobject){
    console.log(`username is ${anyobject.username} and price is ${anyobject.price} `);

}
handleobject(user)
handleobject({
    username:"pras",
    price:488
})



const myNewArray = [444,545,5454,454]
function returnSecondValue(gerarray){
    return gerarray[1]
}
console.log(returnSecondValue(myNewArray))

