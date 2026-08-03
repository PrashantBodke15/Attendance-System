 const coding = ["js","ruby","java","python","cpp"]
// coding.forEach( function (val){
//     console.log(coding)
// })


// coding.forEach((prashant)=>{
//     console.log(prashant)
// })

// function printme(item){
//     console.log(item);
// }
// coding.forEach(printme)

coding.forEach((item, index, arr) =>{
    //console.log(item,index,arr);
})

const mycoding = [
    {
    languageName: "jaVascript",
    languageFilename:"js"
    },

    {
    languageName: "python",
    languageFilename:"py"
    },


   {
    languageName: "java",
    languageFilename:"java"
    },

]

mycoding.forEach((item) =>{
    console.log(item.languageName);
})