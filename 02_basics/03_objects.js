// singleton \

// objects literals
//Object.create
const mysym =Symbol("key1")

const JSUser = {
    name:"prashant",
    "fullname": "prashant bodke",
    mysym:"mykey1",
    age:22,
    location: "pune",
    email: "praavi18@gmail.com",

}

 //console.log(JSUser.email);
// console.log(JSUser["email"]);
// console.log(JSUser["fullname"])
// console.log(JSUser[mysym])


JSUser.email = "prashant5858@gmail.com"
//Object.freeze(JSUser)
JSUser.email=" prashant5859998@gmail.com"
// console.log(JSUser);


JSUser.greeting = function(){
    console.log("hello js user");

}
JSUser.greetingtwo = function(){
    console.log(`hello js user,${this.email}`);

}


console.log(JSUser.greeting());
console.log(JSUser.greetingtwo());

