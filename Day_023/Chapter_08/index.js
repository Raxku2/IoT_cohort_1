
// for loop 
// for (let a = 1; a < 5; a++) {
//   console.log(a);
//
// }

let fuellevel = 0

// do {
//   console.log("Engine running ...");
//   console.log(fuellevel)
//   fuellevel--;
// } while (fuellevel > 0);



// for (let safeBox = 1; safeBox <= 10; safeBox++) {
//   if (safeBox === 1) {
//     console.log("Diamond found");
//     break;
//   }
//   console.log(`Box ${safeBox} is empty`)
// }


// for (let floor = 1; floor <= 8; floor++) {
//   if (floor == 5) {
//     continue;
//     console.log("floor 5 is under construction");
//     // continue;
//   }
//   console.log(`Elevator stopped at floor ${floor}`)
//
// }


const fruits = ['apple','banana','cherry'];


// for (fruit in fruits){
//   console.log(fruits[fruit]);
// }
//
//
// for (fruit of fruits){
//   console.log(fruit);
// }
//
// for (let index = 0; index < fruits.length; index++) {
//   const element = fruits[index];
//   console.log(element);
//
// }


const user = {
  name: "Rakesh",
  role: 'Admin',
  level: 42
}


for (key in user){
  console.log('value of key: ',key,' is ',user[key]);
}






















