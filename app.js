document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll('.fade-text').forEach(el => {
    setTimeout(() => {
      el.classList.add('show');
    }, 100);
  });
});