 $(document).ready(function ($) {

        // delegate calls to data-toggle="lightbox"
        $(document).delegate('*[data-toggle="lightbox"]:not([data-gallery="navigateTo"])', 'click', function(event) {
          event.preventDefault();
          return $(this).ekkoLightbox({
            onShown: function() {
              if (window.console) {
                // return console.log('Checking our the events huh?');
              }
            },
            onNavigate: function(direction, itemIndex) {
              if (window.console) {
                // return console.log('Navigating '+direction+'. Current item: '+itemIndex);
              }
            }
          });
        });

        //Programatically call
        $('#open-image').click(function (e) {
          e.preventDefault();
          $(this).ekkoLightbox();
        });
        

        $(document).delegate('*[data-gallery="navigateTo"]', 'click', function(event) {
          event.preventDefault();
          return $(this).ekkoLightbox({
            onShown: function() {
              var lb = this;
              $(lb.modal_content).on('click', '.modal-footer a', function(e) {
                e.preventDefault();
                lb.navigateTo(2);
              });
            }
          });
        });

      });