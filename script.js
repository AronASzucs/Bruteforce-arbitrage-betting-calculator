X = null;
Y = null;
XCount = 0;
OldPriceX = 0;
OldPriceY = 0;
NewPriceY = 0;
DateSold = null;


function calculate(){
    X = document.getElementById("soldItem").value;
    XCount = document.getElementById("soldCount").value;
    DateSold = document.getElementById("soldDate").value;
    Y = document.getElementById("boughtItem").value;

    

    
    CurrentValue = OldPriceX * XCount / OldPriceY * NewPriceY;
}

document.getElementById("calculateBtn").addEventListener("click", () => {
    calculate();
    console.log("Count: " + XCount);
    console.log("Stock X: " + X);
    console.log("Stock Y: " + Y);
    console.log("Date: " + DateSold);
});
