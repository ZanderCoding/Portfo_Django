function animate(id, words) {
  let currentWordIndex = 0;
  let currentCharIndex = 0;
  let isDeleting = false;

  function type() {
    const currentWord = words[currentWordIndex];
    const textElement = document.getElementById(id);

    if (isDeleting) {
      // Deleting characters
      textElement.textContent = currentWord.substring(0, currentCharIndex - 1);
      currentCharIndex--;
    } else {
      // Typing characters
      textElement.textContent = currentWord.substring(0, currentCharIndex + 1);
      currentCharIndex++;
    }

    // Check if word is fully typed or deleted
    if (!isDeleting && currentCharIndex === currentWord.length + 1) {
      isDeleting = true;
      setTimeout(() => {
        type();
      }, 1500); // Wait before starting to delete
    } else if (isDeleting && currentCharIndex === 0) {
      isDeleting = false;
      currentWordIndex = (currentWordIndex + 1) % words.length;
      setTimeout(() => {
        type();
      }, 500); // Wait before starting to type the next word
    } else {
      // Continue typing or deleting
      setTimeout(() => {
        type();
      }, isDeleting ? 75 : 150); // Speed of typing or deleting
    }
  }

  type(); // Start the typing animation
}

function animateTitle(id, words) {
  let currentWordIndex = 0;
  let currentCharIndex = 0;

    function type() {
        const currentWord = words[currentWordIndex];
        const textElement = document.getElementById(id);

        // Typing characters
        textElement.textContent = currentWord.substring(0, currentCharIndex + 1);
        currentCharIndex++;

        setTimeout(() => {
            type();
        }, 50); // Wait before starting to type the next word
    }
    
    type(); // Start the typing animation
}