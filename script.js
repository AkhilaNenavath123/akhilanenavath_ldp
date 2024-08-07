function openTab(evt, tabName) {
    var i, tabcontent, tablinks;

    // Hide all tab contents
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    // Remove the active class from all tab links
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    // Show the current tab content and add the active class to the tab link
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
}

// Default open the Home tab
document.addEventListener("DOMContentLoaded", function() {
    document.querySelector('.tablinks').click();
});

// Add event listener for form submission
document.getElementById('myForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting the default way
    alert('Your message has been sent to Akhila!');
});
