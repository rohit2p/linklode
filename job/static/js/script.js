function toggleMobileMenu() {
    const menu = document.getElementById('mobileMenu');
    menu.classList.toggle('hidden');
  }
  
  // Close mobile menu when clicking outside (optional enhancement)
  document.addEventListener('click', function(e) {
    const menu = document.getElementById('mobileMenu');
    if (!e.target.closest('nav') && !menu.classList.contains('hidden')) {
      menu.classList.add('hidden');
    }
  });