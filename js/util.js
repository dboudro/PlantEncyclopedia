function hoverKirby() {
  var kirby = document.getElementById('about-me-title');
  kirby.innerHTML = '(>^.^<)';
  kirby.style.backgroundColor = '#EEEEEE';
  kirby.style.color = '#BDBDBD';
  kirby.style.display = 'inline';
  kirby.style.padding = '1px 20px 1px 3px';
  kirby.style.cursor = "none";
}
function byeKirby() {
  var kirby = document.getElementById('about-me-title');
  kirby.innerHTML = 'ABOUT ME.';
  kirby.style.backgroundColor = '#FFF';
  kirby.style.color = '#BFB49B';
  kirby.style.padding = '1px 3px 1px 3px';
}
