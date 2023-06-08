function diamond(number) {
    let output = '';
  
    // Generate the top half of the diamond
    for (let row = 1; row <= number; row++) {
      for (let column = 1; column <= row; column++) {
        output += ' ' + column; // Add numbers to the left of the diamond
      }
      output += '<br>'; // Start a new line
    }
  
    // Generate the bottom half of the diamond
    for (let row = number - 1; row >= 1; row--) {
      for (let column = 1; column <= row; column++) {
        output += ' ' + column; // Add numbers to the left of the diamond
      }
      output += '<br>'; // Start a new line
    }
  
    // Display the diamond pattern
    document.getElementById('result').innerHTML = output;
  } 