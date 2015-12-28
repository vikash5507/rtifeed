$('#feedback_button').on('click', function(){
  if($('#feedback_content').val() == ""){
    $('#feedback_msg').css('display', '');
    return;
  }
  $.ajax({
    url : '/feedback',
    data : {
      feedback_text : $('#feedback_content').val()
    },
    dataType : 'json',
    beforeSend : function(){
      $('#feedback_button').html('Please wait');
      $('#feedback_button').attr('disabled', true);
    },
    success : function(data){
      $('#close_feedback').trigger('click');
      swal('Thank you for your feedback!', 'We will get back soon', 'success');
      $('#feedback_msg').css('display', 'none');
      $('#feedback_content').val("");
      $('#feedback_button').attr('disabled', false);
      $('#feedback_button').html('Submit Feedback');
    },
    error : function(err){
      $('#close_feedback').trigger('click');
      swal('Oops!', 'Something went wrong', 'error');
    }
  })
});