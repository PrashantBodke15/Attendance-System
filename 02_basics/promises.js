// function AptitudeRound(callback){
//     console.log("Aptitude round completed");
//     callback();
// }

// function TechnicalRound(callback){
//     console.log("Technical  Round completed")
//     callback();

// }

// function HRRound(callback){
//     console.log("HR Round completed");
//     callback();
// }

// function GDRound(callback){
//     console.log("GD round Completed");
// }


// AptitudeRound (function(){
//     TechnicalRound(function(){
//         HRRound(function(){ 
//         GDRound();
//         });
//     });
// });

// console.log("congratulation you have been selected");


let examresult  = new Promise((resolve,reject)=>{
    let marks = 89;
    if (marks >60)
    {
        resolve("comgratulation you are pasaed");
    }
    else{
        reject("sorry, you have failed");
    }
});

examresult
.then(result=>{
    console.log(result);
})

.catch(error=>{
    console.log(error)
})
