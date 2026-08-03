const mynums = [1,2,3 ]

const myTotal  = mynums.reduce(function(acc,currval){

    //console.log(`acc:${acc} and currval:${currval}`);
    return acc+currval
}, 6)

//const myTotal = mynums.reduce( (acc, curr)=>acc+curr,0)

//console.log(myTotal);

const shopingcart = [
    {
        itemname:"js course",
        price :3433
    },

       {
        itemname:"js course",
        price :343334
    },


       {
        itemname:"python course",
        price :34433
    },


       {
        itemname:"java course",
        price :35433
    }
]
 const pricetopay = shopingcart.reduce( (acc,item) => acc +item.price,0)
 console.log(pricetopay)