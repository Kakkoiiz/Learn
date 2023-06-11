

// clone map

// Array.prototype.map2 = function(callback) {
//   var output = [], arrayLength = this.length
//   for (var i =0; i < arrayLength; ++i){
//     var result = callback(this[i], i)
//     output.push(result)
//   }
//   return output;
// }
// var htmls =  courses.map2(function(course){
//   return  `<h2>${course}</h2>`
// });

// console.log(htmls.join(''));


// -----------------------------------------------------------------//
// clone forEach

// Array.prototype.forEach2 = function(callback) {
//   var arrayLength = this.length
//   for (var i = 0; i < arrayLength; i++){
//     if (this.hasOwnProperty(i)) {
//       callback(this[i], i);

//     }
//   }

// }

// courses.forEach2(function(course) {
//   console.log(course);
// })


// ------------------------------------------//
// clone every

// Array.prototype.every2 = function(callback) {
//   var arrayLength = this.length;
//   for (var i = 0; i < arrayLength; i++) {
//     if (!callback(this[i], i)) {
//       return false;
//     }
//   }
//   return true;
// }
// var check = courses.every2(function(course, index){
//   console.log(index)
//   return course === 'Java';
// })

// console.log(check)

// ----------------------------------------//
// clone some
// Array.prototype.some2 = function(callback) {
//   var arrayLength = this.length;
//   for (var i = 0; i < arrayLength; i++ ) {
//     if(callback(this[i],i)){
//       return true;
//     }
//   }
//   return false;
// }
// var checkSome = courses.some2(function(course) {
//   return course === 'CSS'
// })
// console.log(checkSome)

// ----------------------------------------
// clone filter

// Array.prototype.filter2 = function(callback) {
//   var output = [];
//   for(var index in this) {
//     if(this.hasOwnProperty(index)){
//       var result = callback(this[index], index, this);
//       if (result){
//         output.push(this[index]);
//       }
//     }
//   }
//   return output
// }



var courses = [
    {
      name: 'JavaScripts',
      coin: 300,
      isFinish: false
    },
    {
      name: 'HTML/CSS',
      coin: 500,
      isFinish: false
    },
    {
      name: 'PHP',
      coin: 400,
      isFinish: false
    }
  ]
  
  
  var fliterCourses = courses.some(function(course, index, array) {
    return course.isFinish;
  })
  
  console.log(fliterCourses)