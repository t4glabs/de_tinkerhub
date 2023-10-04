frappe.ready(function() {
    // Get a reference to the anchor tag by its class name
    var anchor = document.querySelector('.edit-button');
    
    // Check if the anchor tag exists
    if (anchor) {
        // Change the text content of the anchor tag
        anchor.textContent = 'Edit Profile';
    }
})