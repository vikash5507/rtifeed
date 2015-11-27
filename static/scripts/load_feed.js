var fetched_rti_list = [];

function make_feed_for_url(feed_url){
  load_feed(feed_url);
  $(window).unbind("scroll");
  $(window).scroll(function () {
    if ($(window).scrollTop() >= $(document).height() - $(window).height()) {
      load_feed(feed_url);
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
      $('#feedcontainer').append(data['feed_html']);
    },
    error : function(err){
      console.log(err);
    }

  });
}

