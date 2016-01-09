var myDropzone = new Dropzone("div#rti_images", { 
    url: "submit_rti_photos",
    maxFiles : 5,
    maxFilesize : 10,
    acceptedFiles : 'image/*, application/pdf',
    // addRemoveLinks : true,
    dictDefaultMessage : 'Click to browse OR drag files here'
});


var can_submit = true;

myDropzone.on('sending', function(data, xhr_obj, fd){
  fd.append('rti_hash', '{{ rti_hash }}');
  can_submit = false;
  $('#post_id').prop('disabled', true);
});

myDropzone.on('complete', function(){
  can_submit = true;
  $('#post_id').prop('disabled', false);
})

$('#govt_id').change(function(){
  get_department_list();
})

$('#department_name').on('keydown', function(e){
  if(e.which == 9){
    return;
  }
  get_authority_list();
});

function get_authority_list(){
  $.ajax({
    url : '/get_authorities_of',
    data : {
      gov_id : $('#govt_id').val(),
      department_name : $('#department_name').val()
    },
    dataType : 'json',
    beforeSend : function(){
      // $('input').attr('disabled', 'disabled');
      // $('#tds_loader').css('display','');
    },
    success : function(data){
      // alert(data);
      
      var authorities = new Bloodhound({
        datumTokenizer: Bloodhound.tokenizers.whitespace,
        queryTokenizer: Bloodhound.tokenizers.whitespace,
        local: data['authority_list']
      });
      $('#authority_name').val("");
      $('#authority_name').typeahead('destroy');
      $('#authority_name').typeahead({
        hint: true,
        highlight: true,
        minLength: 0
      },
      {
        name: 'authorities',
        source: authorities
      });

      // $('input').removeAttr('disabled');
      // $('#tds_loader').css('display','none');
      // $(".chosen-select").chosen({disable_search_threshold: 10});
    },
    error : function(err){
      console.log(err);
    }
  });
}

get_department_list();
function get_department_list(){
  $.ajax({
    url : '/get_departments_of',
    data : {
      gov_id : $('#govt_id').val()
    },
    dataType : 'json',
    beforeSend : function(){
      // $('input').attr('disabled', 'disabled');
      // $('#tds_loader').css('display','');
    },
    success : function(data){
      // alert(data);
      var departments = new Bloodhound({
        datumTokenizer: Bloodhound.tokenizers.whitespace,
        queryTokenizer: Bloodhound.tokenizers.whitespace,
        local: data['department_list']
      });
      $('#department_name').val("");
      $('#department_name').typeahead('destroy');
      $('#department_name').typeahead({
        hint: true,
        highlight: true,
        minLength: 0
      },
      {
        name: 'departments',
        source: departments
      });

      $('#dept_id').html(data['departments']);
      // $('input').removeAttr('disabled');
      // $('#tds_loader').css('display','none');
      // $(".chosen-select").chosen({disable_search_threshold: 10});
    },
    error : function(err){
      console.log(err);
    }
  });
}

$(".textarea").wysihtml5();


  $("#descr_id").on('keyup', function() {
        var words = this.value.match(/\S+/g).length;
        if (words > 40) {
            // Split the string on first 200 words and rejoin on spaces
            var trimmed = $(this).val().split(/\s+/, 40).join(" ");
            // Add a space at the end to keep new typing making new words
            $(this).val(trimmed + " ");
        }
        else {
            // $('#display_count').text(words);
            $('#descr_count').text(40-words);
        }
    });
  
var sampletag=[];
$.ajax({
    url : '/get_rti_tag',
    dataType:'json',
    data : {
    },
    success : function(data){
      for (var i=0;i<data.length;i++)
      {
        sampletag.push(data[i]['tag_name']);
      }
    },
    error : function(err){
      console.log(err);
    }
  });
var sampleTags = sampletag;
//-------------------------------
// Preloading data in markup
//-------------------------------
$('#rti_tags').tagit({
    availableTags: sampleTags, // this param is of course optional. it's for autocomplete.
    // configure the name of the input field (will be submitted with form), default: item[tags]
    itemName: 'item',
    fieldName: 'tags'
});

if(typeof(String.prototype.trim) === "undefined")
{
    String.prototype.trim = function() 
    {
        return String(this).replace(/^\s+|\s+$/g, '');
    };
}

$(document).ready(function(){
  $('.wysihtml5-sandbox').contents().find('body').on("keydown",function(e) {
    if(e.which == 9){
      e.preventDefault();
      e.returnValue = false;
      $('#descr_id').focus();
    }
  });
});
