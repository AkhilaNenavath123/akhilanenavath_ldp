//Question1. Write a program to demonstrate how a function can be passed as a parameter to another function.
// Function that will be passed as a parameter
function greet(name) {
    return `Hello, ${name}!`;
  }
  
  // Function that takes another function as a parameter
  function processUserInput(callback) {
    const name = "Akhila";
    console.log(callback(name));
  }
  
/* Question2:An arrow function takes two arguments firstName and lastName and returns a 2 letter string that represents the first letter of both the arguments.
For the arguments Roger and Waters, the function returns ‘RW’. */
// Call processUserInput and pass greet as a parameter
processUserInput(greet);

  // Arrow function to return the initials of firstName and lastName
const getInitials = (firstName, lastName) => {
  return `${firstName[0]}${lastName[0]}`;
};

// Example usage
const initials = getInitials('Roger', 'Waters');
console.log(initials); // Outputs: RW

  