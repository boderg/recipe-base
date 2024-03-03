// Materialize functionality

$(document).ready(function(){
    $('.sidenav').sidenav({edge: "left"});
    $('.tooltipped').tooltip();
    $('select').formSelect();
});


// Add event listener to the form to create a new 
// input field when the last input field is filled

// Select the parent element
let parentElement = document.getElementById('parent');

// Variable to store the last key pressed
let lastKeyPressed = null;

// Add keydown event listener to the window
window.addEventListener('keydown', function (event) {

    // Store the last key pressed
    lastKeyPressed = event.key;
});

// Add input event listener to the parent element
parentElement.addEventListener('input', function (event) {

    // Check if the target is an input field
    if (event.target.tagName.toLowerCase() === 'input') {

        // Check if the value is not empty, the last key pressed was not backspace, and the input field doesn't already have a sibling input field
        if (event.target.value.length === 1 
            && lastKeyPressed !== 'Backspace' 
            && !(event.target.nextElementSibling 
            && event.target.nextElementSibling.tagName.toLowerCase() === 'input')) {

            // Create a new input field
            let newInput = document.createElement('input');
            newInput.type = 'text';
            newInput.placeholder = 'Enter next item here';

            // Append the new input field to the parent element
            parentElement.appendChild(newInput);
        }
    }
});