document.addEventListener('DOMContentLoaded', function() {
  var homeBtn = document.getElementById('homeBtn');
  var dropdown = homeBtn.nextElementSibling;

  homeBtn.addEventListener('click', function() {
    var expanded = this.getAttribute('aria-expanded') === 'true';
    this.setAttribute('aria-expanded', !expanded);
    if (dropdown.style.display === 'block') {
      dropdown.style.display = 'none';
    } else {
      dropdown.style.display = 'block';
    }
  });

  // Close dropdown if clicked outside
  document.addEventListener('click', function(event) {
    if (!homeBtn.contains(event.target) && !dropdown.contains(event.target)) {
      dropdown.style.display = 'none';
      homeBtn.setAttribute('aria-expanded', 'false');
    }
  });
});
