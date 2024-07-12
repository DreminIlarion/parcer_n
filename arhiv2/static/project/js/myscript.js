document.getElementById('select_all')
  .addEventListener('click', function (e) {
    var els = document.querySelectorAll(
      'input[name=additional]'
    );

    Array.prototype.forEach.call(els, function(cb){
      cb.checked = e.target.checked;
    });
  })
;

// document.getElementById('select_all').checked = false;
// document.getElementById('all_ch').checked = false;