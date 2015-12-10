var fetched_rti_list = [];

function make_feed_for_url(feed_url){
  load_feed(feed_url);
  $('#bodyid').unbind("scroll");
  $('#bodyid').scroll(function () {
    if($(window).scrollTop() >= $(document).height() - $(window).height()) {
      console.log('scroll top ' + $(document).scrollTop());
      // load_feed(feed_url);
    }
  });
}


function load_feed(feed_url){
  $.ajax({
    url : feed_url,
    data : {
      fetched_rti_list : JSON.stringify(fetched_rti_list),
    },
    dataType : 'json',
    success : function(data){
      fetched_rti_list = fetched_rti_list.concat(data['rti_id_list']);
      if(data['rti_id_list'].length == 0){
        $('#feedcontainer').append('<h3> No Recent Activity </h3>')
      }
      $('#feedcontainer').append(data['feed_html']);
    },
    error : function(err){
      console.log(err);
    }

  });
}

