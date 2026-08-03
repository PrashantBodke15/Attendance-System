

const user = {
    username : "prashant",
    price :999,

    welcomeMessege:function (){
        console.log(`${this.username},welcome to website`);
        console.log(this)
    }
    
}
// user.welcomeMessege()
// user.username = "vaishnavi"
// user.welcomeMessege()

//.log(this)


// function chai(){
//     let username = "hitesh"
//     console.log(this.username);
// }
// chai()


// const chai = function(){
//     let username = "hitesh"
//     console.log(this.username);
// }


const chai = ()=>{
    let username = "hitesh"
    console.log(this);
}

//chai()


//  const addTw0=(num1,num2) =>{
//     return num1+num2
//  }

 //const addTw0=(num1,num2) =>  num1+num2
  //const addTw0=(num1,num2) =>  (num1+num2)

   const addTw0=(num1,num2) =>( {username:"hitesh"})
 console.log(addTw0(3,6))


 const myArray = [5,5,6,6,7]
//myArray.forEach()



