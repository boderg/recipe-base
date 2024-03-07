// Materialize functionality

$(document).ready(function () {
    $('.sidenav').sidenav({
        edge: "left"
    });
    $('.tooltipped').tooltip();
    $('select').formSelect();
    $('.modal').modal();
});


// Add event listener to the form to create a new 
// input field when the last input field is filled
// on list items only

// Variables to store the last key pressed and parent elements
let lastKeyPressed = null;
let parentElements = ['list1', 'list2', 'list3', 'list4'].map(id => document.getElementById(id));

// Add keydown event listener to the window to store the last key pressed
window.addEventListener('keydown', function (event) {

    lastKeyPressed = event.key;
});

// Function to add input event listener to a parent element
function addInputEventListener(parentElement) {
    parentElement.addEventListener('input', function (event) {

        // Check if the target is an input field
        if (event.target.tagName.toLowerCase() === 'input') {

            // Check if the value is not empty, the last key pressed was not backspace, and the input field doesn't already have a sibling input field
            if (event.target.value.length === 1 &&
                lastKeyPressed !== 'Backspace' &&
                !(event.target.nextElementSibling &&
                    event.target.nextElementSibling.tagName.toLowerCase() === 'input')) {

                // Create a new input field
                let newInput = document.createElement('input');
                newInput.placeholder = 'Enter next item';
                newInput.type = 'text';
                newInput.name = event.target.name;

                // Add blur event listener to the new input field to remove it if it's empty
                newInput.addEventListener('blur', function () {
                    if (newInput.parentNode.lastChild === newInput && newInput.value === '') {
                        newInput.parentNode.removeChild(newInput);
                    }
                });

                // Append the new input field to the parent element
                parentElement.appendChild(newInput);
            }
        }
    });
}

// Add input event listener to each parent element
parentElements.forEach(addInputEventListener);

// Add event listener to the form to prevent the form 
// from submitting when the enter key is pressed
let form = document.getElementById('add_recipe');

form.addEventListener('keydown', function (event) {
    if (event.key === 'Enter') {
        event.preventDefault();
    }
});