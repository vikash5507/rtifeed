function make_handlers_for(rti_id, pic_url){
  // alert(rti_id);
  $('.like'+rti_id).each(function(){
    $(this).unbind('click');
    $(this).on('click', function(){
      post_response(rti_id, 'like');
    });
  });
  
  $('.unlike'+rti_id).each(function(){
    $(this).unbind('click');
    $(this).on('click', function(){
      post_response(rti_id, 'unlike');
    });
  });

  $('.follow'+rti_id).each(function(){
    $(this).unbind('click');
    $(this).on('click', function(){
      post_response(rti_id, 'follow');
    });
  });
  $('.unfollow'+rti_id).each(function(){
    $(this).unbind('click');
    $(this).on('click', function(){
      post_response(rti_id, 'unfollow');
    });
  });

  $('.load_prev_comments'+rti_id).each(function(){
    $(this).unbind('click');
    $(this).on('click', function(){
      load_prev_comments(rti_id);
    });
  });

  $('.show_all'+rti_id).each(function(){
    $(this).unbind('click');
    $(this).on('click', function(){
      show_all_comments(rti_id);
    });
  });

  $('.hide_all'+rti_id).each(function(){
    $(this).unbind('click');
    $(this).on('click', function(){
      hide_all_comments(rti_id);
    });
  });

  $('.comment'+rti_id).each(function(){
    $(this).unbind('keydown');
    $(this).on('keydown', function(e){
      if(e.which == 13){
        // alert("yup");
        post_comment(rti_id, $(this).val(), pic_url);
      };
    });
  });
}

function load_prev_comments(rti_id){
  $.ajax({
    url : '/load_prev_comments',
    data : {
      rti_query_id : rti_id
    },
    success : function(data){
      $('.comment_container' + rti_id).each(function(){
        $(this).html(data);
        // toggle_load_to_hide_comments();
      });
      $('.load_prev_comments' + rti_id).each(function(){
        $(this).remove();
      });
      $('.hide_all' + rti_id).each(function(){
        $(this).css('display', '');
      })

    },
    error : function(err){
      console.log(err);
    }
  })
}

function hide_all_comments(rti_id){
  $('.comment_container' + rti_id).each(function(){
    $(this).css('display', 'none');
  });
  $('.hide_all' + rti_id).each(function(){
    $(this).css('display', 'none');
  });
  $('.show_all' + rti_id).each(function(){
    $(this).css('display', '');
  });
}

function show_all_comments(rti_id){
  $('.comment_container' + rti_id).each(function(){
    $(this).css('display', '');
  });
  $('.hide_all' + rti_id).each(function(){
    $(this).css('display', '');
  });
  $('.show_all' + rti_id).each(function(){
    $(this).css('display', 'none');
  });
}

function post_comment(rti_id, comment_text, pic_url){
  comment_text = $.trim(comment_text);
  if(comment_text.length == 0){
    return;
  }
  $.ajax({
    url : '/post_comment',
    data : {
      comment_text : comment_text,
      rti_query_id : rti_id
    },
    dataType : 'json',
    beforeSend : function(){
      // $('#comment_container{{rti_id}}').append("test");
      $('.comment_container'+rti_id).each(function(){
        $(this).append('<div class="box-comment" id = "temp_com">'+
              
          '<img class="img-circle img-sm" src="'+ pic_url +'" alt="user image">'+
          '<div class="comment-text">'+
            '<span class="username">'+
              '{{ name_user }}'+
              '<span class="text-muted pull-right"> Just Now</span>'+
            '</span>'+
            comment_text +
          '</div>'+
        '</div>');
        $('.comment' + rti_id).each(function(){
          $(this).val("");
        });
        
      });
      
        
    },
    success : function(data){
      // alert(data);
      $('.lc_count'+rti_id).each(function(){
        $(this).html(data['no_likes']+ ' likes - ' + data['no_comments'] +'comments');
      });
      
      $("#temp_com").remove();
      $('.comment_container' + rti_id).each(function(){
        $(this).append(data['comment_html']);
      });
      
      $('.comment' + rti_id).each(function(){
        $(this).val("");
      });
    },
    error : function(err){
      console.log(err);
    }
  });
}

function post_response(rti_id, rtype){
  // alert(rtype);
  url = '';
  if(rtype == 'like'){
    url = '/post_like';
  }
  else if(rtype == 'unlike'){
    url = '/post_unlike';
  }
  else if(rtype == 'follow'){
    url = '/post_follow_query';
  }
  else if(rtype == 'unfollow'){
    url = '/post_unfollow_query'; 
  }

  $.ajax({
    url : url,
    data : {
      rti_query_id : rti_id,
    },
    dataType : 'json',
    beforeSend : function(){

    },
    success : function(data){
      
      handle_success_response(rti_id, data, rtype);
      
    },
    error : function(err){
      console.log(err);
    }
  });
}

function handle_success_response(rti_id, data, rtype){
  
  $('.lc_count'+rti_id).each(function(){
    $(this).html(data['no_likes']+ ' likes - ' + data['no_comments'] +'comments');
  });
  
  if(rtype == 'like'){

    $('.likecontainer'+rti_id).each(function(){
        $(this).html('<button class="btn btn-default btn-xs unlike'+rti_id+'">'+
        '<i class="fa fa-thumbs-up"></i> Liked</button>')
      });

      $('.unlike'+rti_id).each(function(){
        $(this).on('click', function(){
          post_response(rti_id, 'unlike');
        });
      });
  }
  else if(rtype == 'unlike'){
    $('.likecontainer'+rti_id).each(function(){
        $(this).html('<button class="btn btn-default btn-xs like'+rti_id+'">'+
        '<i class="fa fa-thumbs-o-up"></i> Like </button>')
      });

      $('.like'+rti_id).each(function(){
        $(this).on('click', function(){
          post_response(rti_id, 'like');
        });
      });
  
  }
  else if(rtype == 'follow'){
    $('.followcontainer'+rti_id).each(function(){
        $(this).html('<button class="btn btn-default btn-xs unfollow'+rti_id+'">'+
        '<i class="fa fa-star"></i>Unfollow </button>')
      });

      $('.unfollow'+rti_id).each(function(){
        $(this).on('click', function(){
          post_response(rti_id, 'unfollow');
        });
      });
  }
  else if(rtype == 'unfollow'){
    $('.followcontainer'+rti_id).each(function(){
        $(this).html('<button class="btn btn-default btn-xs follow'+rti_id+'">'+
         '<i class="fa fa-star-o"></i>Follow </button>')
      });

      $('.follow'+rti_id).each(function(){
        $(this).on('click', function(){
          post_response(rti_id, 'follow');
        });
      });
  }
}

function comment_handler(comment_id, rti_id, comment_text){
  // alert(comment_text);
  $('.del_comment' + comment_id).each(function(){
    $(this).on('click', function(){
      post_delete_comment(comment_id, rti_id);
    });
  });

  $('.edit_comment' + comment_id).each(function(){
    $(this).unbind('click');
    $(this).on('click', function(){

      edit_comment(comment_id, rti_id, comment_text);
    });
  });
}

function edit_comment(comment_id, rti_id, comment_text){
  $('.comment_content' + comment_id).each(function(){
    $(this).html('<input type="text" class="form-control' +
      ' input-sm comment_edit_content'+ comment_id + '"' + 
      ' id = "comment_edit_content'+ comment_id+'">');
  });
  $('.comment_edit_content' + comment_id).each(function(){
    $(this).val(comment_text);
    $(this).unbind('keydown');
    $(this).on('keydown', function(e){
      if(e.which == 13){
        alert("yup");
        post_edit_comment(comment_id, $(this).val(), rti_id);
      }
    });
  });

  toggle_edit_button(comment_id, comment_text, rti_id);
  
  // $('#comment_edit_content' + comment_id)
}

function post_edit_comment(comment_id, comment_text, rti_id){
  $.ajax({
    url : '/post_edit_comment',
    data : {
      comment_id : comment_id,
      comment_text : comment_text
    },
    beforeSend : function(){

    },
    success : function(data){
      // toggle_edit_button(comment_id, comment_text, rti_id);
      $('.comment_content' + comment_id).each(function(){
        $(this).html(comment_text);

      });
      $('.edit_comment' + comment_id).each(function(){
        $(this).unbind('click');
        $(this).on('click', function(){
          edit_comment(comment_id, rti_id, comment_text);
        });
      });

    },
    error : function(err){

    }
  });
}

function toggle_edit_button(comment_id, comment_text, rti_id){
  $('.edit_comment' + comment_id).each(function(){
    $(this).unbind('click');
    $(this).on('click', function(){
      $('.comment_content' + comment_id).each(function(){
        $(this).html(comment_text);
      });
      $('.edit_comment' + comment_id).each(function(){
        $(this).on('click', function(){
          edit_comment(comment_id, rti_id, comment_text);
        });
      });
    });
  });
}
function post_delete_comment(comment_id, rti_id){
  $.ajax({
      url : '/post_delete_comment',
      data : {
        comment_id : comment_id 
      },
      dataType : 'json',
      beforeSend : function(){

      },
      success : function(data){
        // alert(data);
        $('.comment_readbox' + comment_id).each(function(){
          $(this).remove();
        })
        
        $('.lc_count'+rti_id).each(function(){
          $(this).html(data['no_likes']+ ' likes - ' + data['no_comments'] +'comments');
        });
      },
      error : function(err){
        console.log(err);
      }

    });
}