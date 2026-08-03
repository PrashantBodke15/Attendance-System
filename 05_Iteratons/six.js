// const coding = ["js","ruby","java","python","cpp"]

//   const values = coding.forEach((item) =>{
//     console.log(item)
//     return item
//  })

 //console.log(values);


 const myNums = [1,2,3,4,5,6,7,8,9,10]

// const newnums = myNums.filter((num)=>{
//    return num>4
// })
// console.log(newnums);


// const newNums = []
// myNums.forEach((num)=>{
//     if (num>4){
//         newNums.push(num)
//     }
// })
// console.log(newNums);


 const books = [
    {title:'Book one', genre:'fiction',publish:1981,
        edition:2004},
    
          {title:'Book one', genre:'fiction',publish:1981,
        edition:2005},

          {title:'Book two', genre:' non fiction',publish:1981,
        edition:2006},

          {title:'Book three', genre:'history',publish:1981,
        edition:2007},

          {title:'Book four', genre:'fiction',publish:1988,
        edition:2004},

          {title:'Book five', genre:'history',publish:1983,
        edition:2001},

          {title:'Book six', genre:'fiction',publish:1986,
        edition:2007},

          {title:'Book seven', genre:'history',publish:1985,
        edition:2004},

          {title:'Book eoght', genre:'fiction',publish:1981,
        edition:2003},

          {title:'Book nine', genre:'fiction',publish:1981,
        edition:2032},


 ];

 let userBooks = books.filter( (bk) => bk.genre === 'history')
  userBooks = books.filter( (bk) =>{
     return bk. publish >= 1900 && bk. genre === "history"
    })
 console.log(userBooks);

