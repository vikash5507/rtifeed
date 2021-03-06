var proposed_flag = false;
function make_handlers_for(rti_id, user_context, pf){
  // alert(rti_id);
  proposed_flag = pf;
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

  $('.spam'+rti_id).each(function(){
    $(this).unbind('click');
    $(this).on('click', function(){
        spam_sweet_alert(rti_id);
    });
  });


  $('.unspam'+rti_id).each(function(){
    $(this).unbind('click');
    $(this).on('click', function(){
      post_response(rti_id, 'unspam');
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
        post_comment(rti_id, $(this).val(), user_context);
      };
    });
  });

  $('.delete_rti'+rti_id).each(function(){
    $(this).unbind('click');
    $(this).on('click', function(){
      delete_rti(rti_id, 'query');
    });
  });

  $('.delete_rti_response'+rti_id).each(function(){
    $(this).unbind('click');
    $(this).on('click', function(){
      delete_rti(rti_id, 'response');
    });
  });

  $('.view_likes'+rti_id).each(function(){
    $(this).unbind('click');
    $(this).on('click', function(){
      view_likes(rti_id, 1);
    });
  });

}

function view_likes(rti_id, page_no){
  $.ajax({
    url : '/view_likes',
    data : {
      rti_id : rti_id,
      page_no : page_no,
    },
    dataType : 'json',
    beforeSend : function(){
      $('#like_loader' + rti_id).css('display', '');
    },
    success : function(data){
      $('#like_loader' + rti_id).css('display', 'none');
      $('#like_body' + rti_id).html(data['like_list_html']);

    },
    error : function(err){
      console.log(err);
    }
  })
}

function delete_rti(rti_id, rti_type){
  swal({   
    title: "Are you sure?",   
    // text: "Write something interesting:",   
    showCancelButton: true,   
    closeOnConfirm: false,   
    animation: "slide-from-top",   
    confirmButtonText : 'Yes Delete this',
    showLoaderOnConfirm: true,
    },
    function(){
      $.ajax({
        url : '/delete_rti',
        data : {
          'rti_id' : rti_id,
          'rti_type' : rti_type
        },
        type : 'POST',
        success : function(){
          swal('Deleted', 'Your RTI has been successfully deleted', 'success');
          if(rti_type == 'query'){
            $('#feed_box' + rti_id).remove();  
          }
          else{
            $('#feed_box_response' + rti_id).remove();
          }
          
        },
        error : function(){
          swal('Oops', 'Something went wrong', 'error');
        }
      })
      
    });
}


function spam_sweet_alert(rti_id){
  swal({   
    title: "Why did you find this inappropriate?",   
    // text: "Write something interesting:",   
    type: "input",   
    showCancelButton: true,   
    closeOnConfirm: false,   
    animation: "slide-from-top",
    showLoaderOnConfirm : true,
    inputPlaceholder: "Reason" }, 
    function(inputValue){   
      if (inputValue === false) 
        return false;    
      if (inputValue === "") {     
        swal.showInputError("Please specify a reason!");     
        return false;
      }      
      post_response(rti_id, 'spam', inputValue);
      // swal('Thanks!', 'Your feedback has been registered', 'success');
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

function post_comment(rti_id, comment_text, user_context){
  comment_text = $.trim(comment_text);
  if(comment_text.length == 0){
    return;
  }
  $.ajax({
    url : '/post_rti_activity',
    data : {
      comment_text : comment_text,
      activity_type : 'comment',
      rti_query_id : rti_id,
      undo : 0,
      edit : 0
    },
    dataType : 'json',
    type : 'POST',
    beforeSend : function(){
      // $('#comment_container{{rti_id}}').append("test");
      $('.comment_container'+rti_id).each(function(){
        $(this).append('<div class="box-comment" id = "temp_com">'+
              
          '<img class="img-circle img-sm" src="'+ user_context['profile_picture'] +'" alt="user image">'+
          '<div class="comment-text">'+
            '<span class="username">'+
               user_context['name_user'] +
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
        $(this).html(data['no_likes']+ ' likes - ' + data['no_comments'] +' comments');
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
      console.log(JSON.stringify(err));
    }
  });
}

function post_response(rti_id, rtype, meta_data){
  // alert(rtype);
  meta_data = typeof meta_data !== 'undefined' ? meta_data : false;
  var url = '/post_rti_activity';
  var activity_type = '';
  var undo = 0;
  if(rtype == 'like'){
    activity_type = 'like';
  }
  else if(rtype == 'unlike'){
    activity_type = 'like';
    undo = 1;
  }
  else if(rtype == 'follow'){
    activity_type = 'follow';

  }
  else if(rtype == 'unfollow'){
    activity_type = 'follow';
    undo = 1;
  }

  else if(rtype == 'spam'){
    activity_type = 'spam';

  }
  
  else if(rtype == 'unspam'){
    activity_type = 'spam';
    undo = 1;
  }

  $.ajax({
    url : url,
    data : {
      rti_query_id : rti_id,
      activity_type : activity_type,
      meta_data : meta_data,
      undo : undo,
      edit : 0
    },
    type : 'POST',
    dataType : 'json',
    beforeSend : function(){
      handle_success_response(rti_id, rtype);
    },
    success : function(data){
      
      $('.lc_count'+rti_id).each(function(){
        $(this).html(data['no_likes']+ ' likes - ' + data['no_comments'] +' comments');
      });
      if(rtype == 'spam'){
        swal('Thanks!', 'Your feedback has been registered', 'success');
      }
      
    },
    error : function(err){
      console.log(JSON.stringify(err));
    }
  });
}

function handle_success_response(rti_id, rtype){
  
  
  
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
        '<i class="fa fa-star"></i> Unfollow </button>')
      });

      $('.unfollow'+rti_id).each(function(){
        $(this).on('click', function(){
          post_response(rti_id, 'unfollow');
        });
      });
  }
  else if(rtype == 'unfollow'){
    $('.followcontainer'+rti_id).each(function(){
        var follow_text = "Follow";
        if(proposed_flag){
          follow_text = "Want an answer!"
        }
        // alert(proposed_flag);
        $(this).html('<button class="btn btn-default btn-xs follow'+rti_id+'">'+
         '<i class="fa fa-star-o"></i> '+ follow_text +' </button>')
      });

      $('.follow'+rti_id).each(function(){
        $(this).on('click', function(){
          post_response(rti_id, 'follow');
        });
      });
  }

  else if(rtype == 'spam'){
    $('.spamcontainer'+rti_id).each(function(){
        $(this).html('<button class="btn btn-default btn-xs unspam'+rti_id+'">'+
        '<i class="fa fa-thumbs-down"></i> Undo mark as Spam </button>')
      });

      $('.unspam'+rti_id).each(function(){
        $(this).on('click', function(){
          post_response(rti_id, 'unspam');
        });
      });
  }
  else if(rtype == 'unspam'){
    $('.spamcontainer'+rti_id).each(function(){
        $(this).html('<button class="btn btn-default btn-xs spam'+rti_id+'">'+
         '<i class="fa fa-thumbs-o-down"></i> Mark as Spam </button>')
      });

      $('.spam'+rti_id).each(function(){
        $(this).on('click', function(){
          spam_sweet_alert(rti_id);
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
  
  $('.comment_like' + comment_id).each(function(){
    $(this).unbind('click');
    $(this).on('click', function(){
      post_comment_activity(comment_id, rti_id, 'like', comment_text);
    });
  });

  $('.comment_unlike' + comment_id).each(function(){
    $(this).unbind('click');
    $(this).on('click', function(){
      post_comment_activity(comment_id, rti_id, 'unlike', comment_text);
    });
  });

}

function post_comment_activity(comment_id, rti_id, comment_activity, comment_text){
  $.ajax({
    url : '/post_comment_activity',
    data : {
      comment_id : comment_id,
      rti_id : rti_id,
      comment_activity : comment_activity
    },
    type : 'POST',
    dataType : 'json',
    beforeSend : function(){
      if(comment_activity == 'like'){
        // console.log('like');
        $('.comment_like_button_container' + comment_id).each(function(){
          $(this).html('<button class="btn btn-default btn-xs comment_unlike' + comment_id +  ' pull-right"'+
            ' id = "comment_unlike{{ comment_id }}"><i class="fa fa-thumbs-up"></i></button>');
        });
      }
      else{
        // console.log('unlike');
        $('.comment_like_button_container' + comment_id).each(function(){
          $(this).html('<button class="btn btn-default btn-xs comment_like' + comment_id +  ' pull-right"'+
            ' id = "comment_like{{ comment_id }}"><i class="fa fa-thumbs-o-up"></i></button>');
        });
      }
    },
    success : function(data){
      
      $('#comment_no_likes' + comment_id).html(data['no_likes'] + " likes");
      comment_handler(comment_id, rti_id, comment_text);
    },
    error : function(err){
      console.log(err);
    }
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
        // alert("yup");
        post_edit_comment(comment_id, $(this).val(), rti_id);
      }
    });
  });

  toggle_edit_button(comment_id, comment_text, rti_id);
  
  // $('#comment_edit_content' + comment_id)
}

function post_edit_comment(comment_id, comment_text, rti_id){
  $.ajax({
    url : '/post_rti_activity',
    data : {
      comment_id : comment_id,
      comment_text : comment_text,
      rti_query_id : rti_id,
      activity_type : 'comment',
      undo : 0,
      edit : 1
    },
    type : 'POST',
    beforeSend : function(){
      $('.comment_content' + comment_id).each(function(){
        $(this).html(comment_text);
      });
    },
    success : function(data){
      // toggle_edit_button(comment_id, comment_text, rti_id);
      
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
      url : '/post_rti_activity',
       data : {
        comment_id : comment_id,
        rti_query_id : rti_id,
        activity_type : 'comment',
        undo : 1,
        edit : 0
      },
      type : 'POST',
      dataType : 'json',
      beforeSend : function(){
        $('.comment_readbox' + comment_id).each(function(){
          $(this).remove();
        })
      },
      success : function(data){
        // alert(data);
        
        
        $('.lc_count'+rti_id).each(function(){
          $(this).html(data['no_likes']+ ' likes - ' + data['no_comments'] +' comments');
        });
      },
      error : function(err){
        console.log(err);
      }

    });
}