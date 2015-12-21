$(document).ready(function() {
  var user_engine, rti_engine, remoteHost, template, empty;
  $.support.cors = true;

  
  

  user_engine = new Bloodhound({
    identify: function(o) { return o.search_link; },
    queryTokenizer: Bloodhound.tokenizers.whitespace,
    datumTokenizer: Bloodhound.tokenizers.obj.whitespace('name', 'name_user'),
    dupDetector: function(a, b) { return a.search_link === b.search_link; },
    
    remote: {
      url: '/search_model?query=%QUERY&model_type=user&search_type=autocomplete&data_type=json',
      wildcard: '%QUERY'
    }
  });

  rti_engine = new Bloodhound({
    identify: function(o) { return o.search_link; },
    queryTokenizer: Bloodhound.tokenizers.whitespace,
    datumTokenizer: Bloodhound.tokenizers.obj.whitespace('rti_description', 'rti_description'),
    dupDetector: function(a, b) { return a.search_link === b.search_link; },
    
    remote: {
      url: '/search_model?query=%QUERY&model_type=rti&search_type=autocomplete&data_type=json',
      wildcard: '%QUERY'
    }
  });

  

  department_engine = new Bloodhound({
    identify: function(o) { return o.search_link; },
    queryTokenizer: Bloodhound.tokenizers.whitespace,
    datumTokenizer: Bloodhound.tokenizers.obj.whitespace('tds_name', 'tds_name'),
    dupDetector: function(a, b) { return a.search_link === b.search_link; },
    
    remote: {
      url: '/search_model?query=%QUERY&model_type=department&search_type=autocomplete&data_type=json',
      wildcard: '%QUERY'
    }
  });

  state_engine = new Bloodhound({
    identify: function(o) { return o.search_link; },
    queryTokenizer: Bloodhound.tokenizers.whitespace,
    datumTokenizer: Bloodhound.tokenizers.obj.whitespace('tds_name', 'tds_name'),
    dupDetector: function(a, b) { return a.search_link === b.search_link; },
    
    remote: {
      url: '/search_model?query=%QUERY&model_type=state&search_type=autocomplete&data_type=json',
      wildcard: '%QUERY'
    }
  });

  topic_engine = new Bloodhound({
    identify: function(o) { return o.search_link; },
    queryTokenizer: Bloodhound.tokenizers.whitespace,
    datumTokenizer: Bloodhound.tokenizers.obj.whitespace('tds_name', 'tds_name'),
    dupDetector: function(a, b) { return a.search_link === b.search_link; },
    
    remote: {
      url: '/search_model?query=%QUERY&model_type=topic&search_type=autocomplete&data_type=json',
      wildcard: '%QUERY'
    }
  });



  // ensure default users are read on initialization
  // engine.get('1090217586', '58502284', '10273252', '24477185')

  $('.navbar-search-input').typeahead({
      hint: $('.Typeahead-hint'),
      menu: $('.Typeahead-menu'),
      minLength: 1,
      classNames: {
        open: 'is-open',
        empty: 'is-empty',
        cursor: 'is-active',
        suggestion: 'Typeahead-suggestion',
        selectable: 'Typeahead-selectable'
      }
    }, 
    {
      source: user_engine,
      displayKey: 'name_user',
      templates: {
        // header: '<h3 style = "background-color:white;">People</h3>',
        suggestion: function(data){

          return make_user_template(data);
        },
        // empty: empty
      }
    },
    {
      source: rti_engine,
      displayKey: 'rti_description',
      templates: {
        // header: '<h3 style = "background-color:white;">RTI</h3>',
        suggestion: function(data){
          return make_rti_template(data);
        }
        // empty: empty
        }
    },

    {
      source: department_engine,
      displayKey: 'tds_name',
      templates: {
        // header: '<h3 style = "background-color:white;">RTI</h3>',
        suggestion: function(data){
          return make_tds_template(data, 'department');
        }
        // empty: empty
        }
    },

    {
      source: state_engine,
      displayKey: 'tds_name',
      templates: {
        // header: '<h3 style = "background-color:white;">RTI</h3>',
        suggestion: function(data){
          return make_tds_template(data, 'state');
        }
        // empty: empty
        }
    },

    {
      source: topic_engine,
      displayKey: 'tds_name',
      templates: {
        // header: '<h3 style = "background-color:white;">RTI</h3>',
        suggestion: function(data){
          return make_tds_template(data, 'topic');
        }
        // empty: empty
        }
    }


  ).bind('typeahead:selected',function(e, datum, dataset){
    window.location.href = datum.search_link;
  })

  .on('typeahead:asyncrequest', function() {
    $('.Typeahead-spinner').show();
  })
  .on('typeahead:asynccancel typeahead:asyncreceive', function() {
    $('.Typeahead-spinner').hide();
  });

});




function make_user_template(data){
  
  var user_template = '<div class="ProfileCard u-cf">'+
    '<img class="ProfileCard-avatar" src="'+ data.profile_picture +'">'+
    '<a href = "' + data.search_link + '"> </a>'+
    '<div class="ProfileCard-details">'+
      '<div class="ProfileCard-realName"><a href = "' + data.search_link + '">  '+ data.name_user +' </a></div>'+
    '</div>'+

    '<div class="ProfileCard-stats">'+
      '<div class="ProfileCard-stat"><span class="ProfileCard-stat-label">Following:</span>'+ data.num_following +'</div>'+
      '<div class="ProfileCard-stat"><span class="ProfileCard-stat-label">Followers:</span>'+ data.num_followers +'</div>'+
    '</div>'+
  '</div>';
   
  
  return user_template;
}

function make_rti_template(data){
  var rti_template = '<div class="ProfileCard u-cf">'+
    // '<img class="ProfileCard-avatar" src="'+ data.rti_picture +'">'+
    '<a href = "' + data.search_link + '"> </a>'+
    '<div class="ProfileCard-details">'+
      '<div class="ProfileCard-realName"><a href = "' + data.search_link + '">  '+ data.rti_description +' </a></div>'+
    '</div>'+

    '<div class="ProfileCard-stats">'+
      
      '<div class="ProfileCard-stat"><span class="ProfileCard-stat-label">Likes:</span>'+ data.no_likes +'</div>'+
      '<div class="ProfileCard-stat"><span class="ProfileCard-stat-label">Comments:</span>'+ data.no_comments +'</div>'+
    '</div>'+
  '</div>';
    

  
  return rti_template;
}

function make_tds_template(data, tds_type){
  var tds_template = '<div class="ProfileCard u-cf">'+
    // '<img class="ProfileCard-avatar" src="'+ data.rti_picture +'">'+
    '<a href = "' + data.search_link + '"> </a>'+
    '<div class="ProfileCard-details">'+
      '<div class="ProfileCard-realName"><a href = "' + data.search_link + '">  '+ data.tds_name +' </a></div>'+
    '</div>'+

    '<div class="ProfileCard-stats">'+
      '<div class="ProfileCard-stat"><span class="ProfileCard-stat-label">Queries:</span>'+ data.tds_no_rti_queries +'</div>'+
      '<div class="ProfileCard-stat"><span class="ProfileCard-stat-label">Responses:</span>'+ data.tds_no_rti_responses +'</div>'+
      '<div class="ProfileCard-stat"><span class="ProfileCard-stat-label">Followers:</span>'+ data.tds_no_followers +'</div>'+
    '</div>'+
  '</div>';
    

  
  return tds_template;
}
// .bind('typeahead:selected', function (obj, datum) {
//   window.location.href = datum.link;
// });

$('.navbar-search-input').on('keyup', function(e) {
    // alert($(this).val());
    if (e.which == 13) {
        window.location.href = '/search_page?query='+ $(this).val() +'&model_type=all&search_type=search&data_type=default'
    }
});

