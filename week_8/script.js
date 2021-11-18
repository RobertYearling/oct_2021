// let pineapple = 3
// console.log(pineapple)
// pineapple = pineapple + 23
// pineapple += 23
// console.log(pineapple);

// pineapple = pineapple + 1
// pineapple += 1
// pineapple++

// // Numbers
// var num1 = 5
// var num2 = 35
// var num3 = num1 * num2
// console.log("Total Bill: ", num3);

// // Booleans

// var bool = true
// var bool = false
// console.log(bool);

// // Strings
// let str1 = "Rob"
// let str2 = " eats many pizza's"
// console.log(str1);
// console.log(str1 + str2);



// Arrays

// let arr = [ "Rob", "Yearling", 29, ["Chicago", "IL", 60304]]
// console.log(arr[3] + arr )

// Conditionals
// == EQUALS   integer and string
    // int 2 and str 2 true
// === Strict int 2 and str 2 false
// != Not Equal To
// >= Greater Than or Equal To
// <= Less Than or Equal To

// Loops

// For Loop
// Where we want it to start
// Where we want it to end
// How much do we move each time to get to the end

// for ( pizza = 1; pizza <= 10; pizza+=2 ) {
//     console.log(pizza);
// }

// While Loop

// var i = 0
// while(i < 100) {
//     console.log(i);
//     i++
// }

// Decreasing Multiples of 3 Using a loop write code that will console.log all of the values that are evenly divisible by 3 from 100 down to 0

// Drecrease by mulitples of 3
// Use a loop and console.log
// All values divisble by 3
// from 3 to 100

// for ( i = 100; i >= 0; i-- ){
//     if ( i % 2 == 0) {
//         console.log(i);
//     }
// }


// Given an array with multiple values, write a function that returns the maximum number in the array. (e.g. for [-3,3,5,7] max is 7)

// Write Function - Done
// variable store a value - Done
// for loop - Done
// if statement with conidtional

// function findMax(arr) {
//     let max = 0
//     for ( i = 0; i < arr.length; i++ ) {
//         if ( arr[i] > max ) {
//             max = arr[i]
//         }
//     }
//     return max
// }
// console.log(findMax([-3,3,5,7]));


// Write a function that would return an array of all the odd numbers between 1 to 50. (ex. [1,3,5, .... , 47,49]). Hint: Use 'push' method.


// Write a function - Done
// return an Array
// All Odd Numbers 1 - 50

// function arrOdd(num) {
//     let arr = []
//     for ( i = 1; i <= num; i ++ ) {
//         if ( i % 2 == 1 ) {
//             arr.push(i)
//         }
//     }
//     return arr
// }
// console.log(arrOdd(50));


// let arrNum = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
// console.log(arrNum.length);