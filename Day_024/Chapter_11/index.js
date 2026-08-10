



function prntName() {
 console.log('R');
 console.log('a');
 console.log('k');
 console.log('e');
 console.log('s');
 console.log('h');
 var myNumber= 1;
  console.log(myNumber);
}

prntName();
// console.log(prntName);

//sum(4,5);
function sum(a,b) {
  console.log(a+b);
  return a+b;
}

const sumTwo = function() {
console.log('running');
}

// sumTwo();
// const result = sum(4,6);
//
// console.log(result);

const Two = () => {

  console.log('running');
}



// Immediaately Invocked Function Expression

;(function(){
  console.log('connecting...');
})();


;(()=>{
  console.log('connected!');
})();





{
  let data = "19";
}

// console.log(data)




function caal(...numbers) {
  if (!numbers){
    return;
  }
  let res = 0;
  for (number of numbers){
    res  += number;
  }
  return res;
}


console.log(caal(1,4,6))













