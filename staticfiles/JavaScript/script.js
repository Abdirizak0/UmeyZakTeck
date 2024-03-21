 // Function to toggle the navigation menu
 function toggleMenu() {
    var menu = document.getElementById("menu");
    menu.classList.toggle("show");
}

// Event listener to toggle the menu when the menu button is clicked
document.getElementById("menu-btn").addEventListener("click", function() {
    toggleMenu();
});

// Close the menu when a menu item is clicked (optional)
var menuItems = document.querySelectorAll("#menu a");
menuItems.forEach(function(item) {
    item.addEventListener("click", function() {
        toggleMenu();
    });
});