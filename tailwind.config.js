/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './main/templates/**/*.html',
    './main/templates/**/*.js',
    './imageupload/templates/**/*.html',
    './imageupload/templates/**/*.js',
    './venv/lib/python3.11/site-packages/django/contrib/admin/templates/**/*.html',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
