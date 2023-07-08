 var form = document.getElementById('post-form');
 var requiredInputs = form.querySelectorAll('input[required]');

 requiredInputs.forEach(function(input) {
   input.addEventListener('invalid', function() {
     input.classList.add('required-field');
     var label = input.previousElementSibling;
     label.classList.add('required-label');
   });

   input.addEventListener('input', function() {
     input.classList.remove('required-field');
     var label = input.previousElementSibling;
     label.classList.remove('required-label');
   });
 });