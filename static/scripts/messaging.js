var message_loading = false;
var last_fetched_index = null;
$.ajax({
  url : '/fetch_messages/' + other_username,
  dataType : 'json',
  beforeSend : function(){
    message_loading = true;
    $('#message_loader').css('display', '');
  },
  success : function(data){
    $('#messages_container').append(data['message_list_html']);
    $('#messages_container').scrollTop($('#messages_container')[0].scrollHeight);
    message_loading = false;
    $('#message_loader').css('display', 'none');
    last_fetched_index = data['last_fetched_index'];
  },
  error : function(err){
    console.log(err);
    message_loading = false;
  }
});

$('#messages_container').on('scroll', function(){
  if($(this).scrollTop() < 10 && !message_loading){
    console.log('fetching!');
    $.ajax({
      url : '/fetch_messages/' + other_username,
      data : {
        last_fetched_index : last_fetched_index
      },
      dataType : 'json',
      beforeSend : function(){
        message_loading = true;
        $('#message_loader').css('display', '');
      },
      success : function(data){
        $('#messages_container').prepend(data['message_list_html']);
        message_loading = false;
        if(!data['last_fetched_index']){
          message_loading = true;
        }
        last_fetched_index = data['last_fetched_index'];
        $('#message_loader').css('display', 'none');
      },
      error : function(err){
        console.log(err);
        message_loading = false;
      }
    });
  }
});

$('#send_button').on('click', function(){
  var message_text = $('#message_box').val().trim();
  if(message_text.length == 0){
    return;
  }
  $('#message_box').val("");
  $.ajax({
    url : '/send_message/' + other_username,
    data : {
      'message_text' : message_text
    },
    dataType : 'json',
    beforeSend : function(){
      $('#message_loader').css('display', '');
    },
    success : function(data){
      $('#messages_container').append(data['new_messages']);
      $('#messages_container').scrollTop($('#messages_container')[0].scrollHeight);
      $('#message_loader').css('display', 'none');
    },
    error : function(err){
      $('#message_loader').css('display', 'none');
      console.log(err);
    }
  })
});


$('#message_box').on('keypress', function(e){
  if(e.which == 13) {
      // alert('checl');
      $('#send_button').trigger('click');
  }
});
function fetch_new_messages(){
  $.ajax({
    url : '/fetch_messages/' + other_username,
    data : {
      'unread' : 1,
    },
    dataType : 'json',
    success : function(data){
      // alert('yo');
      if(data['message_list_html'].length == 0){
        return;
      }
      $('#messages_container').append(data['message_list_html']);
      $('#messages_container').scrollTop($('#messages_container')[0].scrollHeight);
    },

  })
}
window.setInterval(function(){
  fetch_new_messages();
}, 3000);

$('#message_modal_button').on('click', function(){

  var msg_username = $('#message_modal_search').val();
  if(msg_username.trim().length == 0){
    swal('Please enter a receipent');
    return;
  }

  var message_text = $('#message_modal_text').val().trim();
  if(message_text.length == 0){
    swal('Please write a message');
    return;
  }

  

  $.ajax({
    url : '/send_message/' + msg_username,
    data : {
      'message_text' : $('#message_modal_text').val()
    },
    dataType : 'json',
    beforeSend: function(){
      $('#message_modal_button').html('Please wait');
    },
    success : function(data){
      window.location.href = '/messages/' + msg_username;
    },
    error : function(err){
      swal('Oops!', 'There was a problem delivering your message', 'error');
      console.log(err);
    }
  })
});