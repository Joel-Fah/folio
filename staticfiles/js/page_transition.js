$(document).ready(function() {
    // Add a click event listener to all links with the class 'page-link'
    $('body').on('click', 'a.page-link', function(event) {
        // Prevent the default link behavior
        event.preventDefault();

        // Get the href attribute of the clicked link
        var href = $(this).attr('href');

        // Add a class to the body for the page transition effect
        $('body').addClass('page-transition');

        // After a short delay, redirect to the clicked link
        setTimeout(function() {
            window.location.href = href;
        }, 500); // Adjust the delay as needed
    });
});
