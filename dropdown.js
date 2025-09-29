// Centralized dropdown functionality
document.addEventListener('DOMContentLoaded', function() {
    const dropdown = document.querySelector('.top-nav .dropdown');
    const toggle = dropdown?.querySelector('#markets-toggle');
    const content = dropdown?.querySelector('.dropdown-content');
    
    if (!dropdown || !toggle || !content) return;
    
    
    function closeDropdown() {
        dropdown.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
    }
    
    function toggleDropdown() {
        const isOpen = dropdown.classList.contains('open');
        dropdown.classList.toggle('open');
        toggle.setAttribute('aria-expanded', !isOpen);
    }
    
    // Click toggle
    toggle.addEventListener('click', function(e) {
        e.preventDefault();
        toggleDropdown();
    });
    
    // Keyboard support
    toggle.addEventListener('keydown', function(e) {
        if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            toggleDropdown();
        }
    });
    
    // Global Escape key handling
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && dropdown.classList.contains('open')) {
            closeDropdown();
            toggle.focus();
        }
    });
    
    // Close on outside click
    document.addEventListener('click', function(e) {
        if (!dropdown.contains(e.target)) {
            closeDropdown();
        }
    });
    
    // Close when focus leaves dropdown entirely
    dropdown.addEventListener('focusout', function(e) {
        setTimeout(function() {
            if (!dropdown.contains(document.activeElement)) {
                closeDropdown();
            }
        }, 10);
    });
});