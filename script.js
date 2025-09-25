document.addEventListener('DOMContentLoaded', () => {
    const taglineElement = document.getElementById('typing-tagline');
    if (taglineElement) {
        const taglineText = "Empowering Canadian Retail Investors in Fixed Income Markets";
        let i = 0;
        const typingSpeed = 50; // ms per character

        function typeWriter() {
            if (i < taglineText.length) {
                taglineElement.innerHTML += taglineText.charAt(i);
                i++;
                setTimeout(typeWriter, typingSpeed);
            } else {
                taglineElement.style.borderRight = 'none'; // Remove cursor after typing
            }
        }

        taglineElement.style.borderRight = '2px solid #fff'; // Cursor effect
        typeWriter();
    }
});
