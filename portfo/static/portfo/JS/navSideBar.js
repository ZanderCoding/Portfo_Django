document.addEventListener('DOMContentLoaded', function () {
    const menuToggle = document.querySelector('.menu-toggle');
    const navbar = document.querySelector('.navbar');

    document.addEventListener('click', function (event) {
        const isOpen = navbar.style.left === '0px';
        const isMenuToggle = event.target === menuToggle;
        const isNavbarContent = navbar.contains(event.target);

        if (isOpen && !isMenuToggle && !isNavbarContent) {
            navbar.style.left = '-300px';
        }
    });

    menuToggle.addEventListener('click', function () {
        const isOpen = navbar.style.left === '0px';
        navbar.style.left = isOpen ? '-300px' : '0';
    });
});