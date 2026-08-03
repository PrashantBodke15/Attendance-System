const tinderUser = new Object()




 tinderUser.id= "123abc"
 tinderUser.name = "prashy"
 tinderUser.isloggedin = false

//console.log(tinderUser);

const regularUser = {
    email:"pras@gmail.com",
    fullname:{
        userfullname:{
            firstname:"prashnt",
            lastname:"bodke"
        }
    }
}

//console.log(regularUser.fullname.userfullname.firstname)

const obj1 = {1:"p",2:"v"}
const obj2 = {3:"prashant", 4:"vaishnavi"}
const obj3 = Object.assign({},obj1,obj2)
//const obj3 = {obj1,obj2}
// console.log(obj3)


// console.log(Object.keys(tinderUser));
// console.log(Object.values(tinderUser));
// console.log(Object.entries(tinderUser))

// console.log(tinderUser.hasOwnProperty('islogged'))



const course = {
    coursename:"js in hindi",
    orice:"999",
    courseInstructor:"hitesh"

} 

const {courseInstructor: patil}=course
console.log(patil);

const navbar =({company})=>{

}
navbar(company = "prashant")
console.log(company);


