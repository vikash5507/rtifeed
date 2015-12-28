var fetched_rti_list = [];
var loading = false;
var no_activity = false;
function make_feed_for_url(feed_url){
  // $('#feedcontainer').css('height','200px');
  $('#feedcontainer').after('<center><div id = "feed_loader" style = "display:none; padding-bottom : 40px;"><img height="40" width = "40" src = "/static/dist/img/spinner.gif"></img></div></center>');
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
  if(loading || no_activity){

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
      if(data['rti_id_list'].length == 0 && !no_activity){
        $('#feedcontainer').append('<center><h3 style = "padding-bottom : 10px;"> No Recent Activity </h3></center>');
        no_activity = true;
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

