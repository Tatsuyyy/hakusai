const { exec } = require('child_process');

exec('npx tailwindcss -c ./tailwind.config.js ./static/hakusai/css/tailwind.css -o ./static/hakusai/css/style.css && cleancss -o ./static/hakusai/css/style.min.css ./static/hakusai/css/style.css', (err, stdout, stderr) => {
  if (err) {
    console.error(err);
  } else {
    console.log(stdout);
    console.error(stderr);
  }
});