// Dark mode toggle
const darkModeToggle = document.getElementById('dark-mode-toggle');
  const body = document.body;

  // Load user preference from localStorage
  const userPrefersDarkMode = localStorage.getItem('dark-mode') === 'enabled';

  // Apply dark mode based on user preference
  if (userPrefersDarkMode) {
    body.classList.add('dark-mode');
    darkModeToggle.checked = true;
  }

  darkModeToggle.addEventListener('change', () => {
  // Toggle dark mode class
    body.classList.toggle('dark-mode');

    // Save user preference to localStorage
    const isDarkModeEnabled = body.classList.contains('dark-mode');
    localStorage.setItem('dark-mode', isDarkModeEnabled ? 'enabled' : 'disabled');
  });

