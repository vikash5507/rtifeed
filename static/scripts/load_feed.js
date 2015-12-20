var fetched_rti_list = [];
var loading = false;
function make_feed_for_url(feed_url){
  // $('#feedcontainer').css('height','200px');
  $('#feedcontainer').after('<center><div id = "feed_loader" style = "display:none;"><img height="40" width = "40" src = "/static/dist/img/spinner.gif"></img></div></center>');
  load_feed(feed_url);
  $(window).unbind("scroll");
  $(window).scroll(function () {
    // console.log('scroll');
    if($(window).scrollTop() >= $(document).height() - $(window).height()) {
      load_feed(feed_url);
    }
  });
}


function load_feed(feed_url){
  if(loading){
    return;
  }
  // console.log(fetched_rti_list);
  loading = true;
  $.ajax({
    url : feed_url,
    data : {
      fetched_rti_list : JSON.stringify(fetched_rti_list),
    },
    dataType : 'json',
    beforeSend : function(){
      $('#feed_loader').css('display', '');
    },
    success : function(data){
      fetched_rti_list = fetched_rti_list.concat(data['rti_id_list']);
      if(data['rti_id_list'].length == 0 && fetched_rti_list.length == 0){
        $('#feedcontainer').append('<h3> No Recent Activity </h3>');
        loading = true;
      }
      $('#feedcontainer').append(data['feed_html']);
      $('#feed_loader').css('display', 'none');
      loading = false;
    },
    error : function(err){
      $('#feed_loader').css('display', 'none');
      console.log(err);
      loading = false;
    }

  });
}

