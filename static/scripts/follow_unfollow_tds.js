function make_handlers_for_follow(tds_id, tds_type){
  // alert('hmm');
  $('.tds_follow_btn').each(function(){
    $(this).unbind('click');
    $(this).on('click', function(){
      follow_unfollow_tds('follow', tds_id, tds_type);
    });  
  });
  


  $('.tds_unfollow_btn').each(function(){
    $(this).unbind('click');
    $(this).on('click', function(){
      follow_unfollow_tds('unfollow', tds_id, tds_type);
    });  
  });
}


function follow_unfollow_tds(response_type, tds_id, tds_type){
  var url = '';
  if(response_type == 'follow'){
    url = '/post_follow_tds';
  }
  else{
    url = '/post_unfollow_tds'; 
  }
  // alert('test');
  $.ajax({
    url : url,
    data : {
      tds_id : tds_id,
      tds_type : tds_type
    },
    dataType : 'json',
    beforeSend : function(){

    },
    success : function(data){
      if(response_type == 'follow'){
        $('#follow_btn').html('<b>Unfollow</b>');
        $('#follow_btn').attr('class', 'btn btn-danger btn-block tds_unfollow_btn');
        $('#follow_btn').attr('id', 'unfollow_btn');  
      }
      else{
        $('#unfollow_btn').html('<b>Follow</b>');
        $('#unfollow_btn').attr('class', 'btn btn-primary btn-block tds_follow_btn');
        $('#unfollow_btn').attr('id', 'follow_btn');
      }
      // alert(JSON.stringify(data, null, 4));
      make_handlers_for_follow(tds_id, tds_type);
    },
    error : function(err){
      console.log(err);
    }
  })
}

// make_handlers_for_follow();