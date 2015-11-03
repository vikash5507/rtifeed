function make_handlers_for_follow(user_id){
  $('.user_follow_btn').each(function(){
    $(this).unbind('click');
    $(this).on('click', function(){
      follow_unfollow_user('follow', user_id);
    });  
  });
  


  $('.user_unfollow_btn').each(function(){
    $(this).unbind('click');
    $(this).on('click', function(){
      follow_unfollow_user('unfollow', user_id);
    });  
  });
}


function follow_unfollow_user(response_type, user_id){
  var url = '';
  if(response_type == 'follow'){
    url = '/post_follow_user';
  }
  else{
    url = '/post_unfollow_user'; 
  }
  alert('test');
  $.ajax({
    url : url,
    data : {
      other_user_id : user_id
    },
    dataType : 'json',
    beforeSend : function(){

    },
    success : function(data){
      if(response_type == 'follow'){
        $('#follow_btn').html('<b>Unfollow</b>');
        $('#follow_btn').attr('class', 'btn btn-danger btn-block user_unfollow_btn');
        $('#follow_btn').attr('id', 'unfollow_btn');  
      }
      else{
        $('#unfollow_btn').html('<b>Follow</b>');
        $('#unfollow_btn').attr('class', 'btn btn-primary btn-block user_follow_btn');
        $('#unfollow_btn').attr('id', 'follow_btn');
      }
      $('#num_followers').html(data['num_followers']);
      $('#num_following').html(data['num_following']);
      make_handlers_for_follow(user_id);
    },
    error : function(err){
      console.log(err);
    }
  })
}

// make_handlers_for_follow();