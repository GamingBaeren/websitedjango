/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class', // Enable class-based dark mode toggling
  content: [
    './main/templates/**/*.html',
    './main/templates/**/*.js',
    './imageupload/templates/**/*.html',
    './imageupload/templates/**/*.js',
    './venv/lib/python3.11/site-packages/django/contrib/admin/templates/**/*.html',
  ],
  theme: {
    extend: {
      colors: {
        'light-bg': '#f5f0e9', // Light mode background color from the image
        'light-text': '#000000', // Black text for light mode
        'dark-bg': '#140303', // Custom dark mode background color
      },
    },
  },
  plugins: [],
  safelist: [
    'bg-light-bg',
    'text-light-text',
    'bg-dark-bg',
  ],
}
