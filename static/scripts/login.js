 $(function () {
        $('input').iCheck({
          checkboxClass: 'icheckbox_square-blue',
          radioClass: 'iradio_square-blue',
          increaseArea: '20%' // optional
        });
      });

      function switchVisible(){
        if(document.getElementById('sign_in')){
          if(document.getElementById('sign_in').style.display == 'none'){
            document.getElementById('sign_in').style.display = 'block';
            document.getElementById('sign_up').style.display = 'none';
          }
          else{
            document.getElementById('sign_in').style.display = 'none';
            document.getElementById('sign_up').style.display = 'block'; 
          }
        }
      }

      function validate_signup_form(){
        
      }

      $('#signup_form').on('submit', function(e){
        var password = $('#password').val();
        var re_password = $('#re_password').val();
        if(password != re_password){
          swal('Oops', 'Passwords do not match', 'error');
          return false;
        }
        if(password.length < 4){
          swal('Password too short!', 'Please choose a password of atleast 5 characters', 'error');
          return false;
        }
        
        e.preventDefault();
        var formData = new FormData($(this)[0]);
        
        $.ajax({
          url : '/email_signup',
          type : 'POST',
          data : formData,
          dataType : 'json',
          beforeSend : function(){
            $('#signup_form :input').prop("disabled", true);
            // alert('HMM');
          },
          success : function(data){
            swal(data['message'], data['message_long'], data['message_type']);
            switchVisible();
          },
          error : function(err){
            console.log(JSON.stringify(err));
          },
          contentType : false,
          processData : false
        });
      });

      $('#forgot_password').on('click', function(){
        swal({   
          title: "Please enter your email address and we will send you a new password",   
          // text: "Write something interesting:",   
          type: "input",   
          showCancelButton: true,   
          closeOnConfirm: false,   
          animation: "slide-from-top",
          showLoaderOnConfirm : true,   
          inputPlaceholder: "Email" },
          function(inputValue){
            if (inputValue === false) 
              return false;    
            if (inputValue === "") {     
              swal.showInputError("Please specify an email address");     
              return false;
            }      
            $.ajax({
              url : '/forgot_password',
              data : {
                'email' : inputValue
              },
              dataType : 'json',
              success : function(data){
                swal(data['message'], data['message_long'], data['message_type']);
              },
              error : function(){
                swal('Oops', 'Something went wrong', 'error');
              }
            });
          });
      });