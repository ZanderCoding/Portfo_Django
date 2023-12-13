document.addEventListener('DOMContentLoaded', function () {
    const menuToggle = document.querySelector('.menu-toggle');
    const navbar = document.querySelector('.navbar');
    const darkModeSwitch = document.getElementById('dark-mode-toggle');

    menuToggle.addEventListener('click', function () {
        const isOpen = navbar.style.left === '0px';
        navbar.style.left = isOpen ? '-300px' : '0';
    });

    darkModeSwitch.addEventListener('change', function () {
        document.body.classList.toggle('dark-mode', darkModeSwitch.checked);
    });
});
