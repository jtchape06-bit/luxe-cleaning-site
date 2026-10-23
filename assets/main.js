(function () {
  var burger = document.querySelector('.burger');
  var nav = document.querySelector('nav.main');
  if (burger && nav) {
    burger.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  var items = document.querySelectorAll('.rv');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { threshold: 0.12 });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add('in'); });
  }

  // Enquiry forms -> Luxecleaningcoltd@gmail.com via FormSubmit (AJAX endpoint)
  document.querySelectorAll('form[data-enquiry]').forEach(function (form) {
    var msg = form.querySelector('.form-msg');
    var btn = form.querySelector('button[type=submit]');
    form.addEventListener('submit', function (ev) {
      ev.preventDefault();
      if (form.querySelector('.hp').value) return; // honeypot
      btn.disabled = true;
      var label = btn.textContent;
      btn.textContent = 'Sending…';
      msg.className = 'form-msg';
      fetch('https://formsubmit.co/ajax/luxecleaningcoltd@gmail.com', {
        method: 'POST',
        headers: { 'Accept': 'application/json' },
        body: new FormData(form)
      }).then(function (r) { return r.json(); }).then(function (d) {
        if (d && (d.success === 'true' || d.success === true)) {
          form.reset();
          msg.className = 'form-msg ok';
          msg.textContent = 'Thank you — your enquiry has been sent. We will be in touch shortly.';
        } else { throw new Error('fail'); }
      }).catch(function () {
        msg.className = 'form-msg err';
        msg.innerHTML = 'Sorry, something went wrong. Please email us directly at <a href="mailto:Luxecleaningcoltd@gmail.com"><u>Luxecleaningcoltd@gmail.com</u></a>.';
      }).then(function () { btn.disabled = false; btn.textContent = label; });
    });
  });
})();
