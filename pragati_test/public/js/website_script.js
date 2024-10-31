// website_script.js

document.addEventListener('DOMContentLoaded', function() {
  console.log("Website Script Loaded");  // Confirmation message to the console

  // Add your JavaScript functionality here
  // Example: Form submission handling
  const form = document.querySelector('form'); // Adjust selector as needed
  if (form) {
    form.addEventListener('submit', function(event) {
      event.preventDefault(); // Prevent the default form submission

      // Handle form submission, collect data, etc.
      console.log("Form submitted!");
      // You can also send an AJAX request or similar here
    });
  }
});
