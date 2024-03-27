/* jshint esversion: 11, jquery: true */

// Materialize functionality

$(document).ready(function () {
    $('.sidenav').sidenav({
        edge: "left"
    });
    $('.tooltipped').tooltip();
    $('select').formSelect();
    $('.modal').modal();
});

function addItem(listId, inputName) {
    // Create a new input element
    var newInput = document.createElement("input");
    newInput.type = "text";
    newInput.name = inputName;
    newInput.className = "validate";
    newInput.placeholder = "Enter next item";

    // Append the new input element to the parent div
    var parentDiv = document.getElementById(listId);
    parentDiv.appendChild(newInput);
}

function removeItem(listId) {
    // Get the parent div
    var parentDiv = document.getElementById(listId);

    // Get all input fields within the parent div
    var inputFields = parentDiv.getElementsByTagName("input");

    // Check if there are more than one input fields
    if (inputFields.length > 1) {
        // Remove the last input field
        parentDiv.removeChild(inputFields[inputFields.length - 1]);
    }
}
