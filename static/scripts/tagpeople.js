var word=/@(\w+)/ig; //@abc Match
var fetched_text = null;
function create_tagging_for(selector){
	$(selector).on('keyup', function(){
		var content = $(this).val();
		if(content == fetched_text){
			return;
		}
		fetched_text = content;
		var name = content.match(word);
		if(name && name.length > 0){
			console.log(name.length);
			name = name[0].substring(1, name[0].length)
			$.ajax({
				url: '/search_model?query='+ name +'&model_type=user&search_type=autocomplete&data_type=json',
				dataType : 'json',
				success : function(data){
					
				},
				error : function(err){
					console.log(err);
				}

			});
		}
	});
}