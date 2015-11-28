$.ajax({
	url : '/get_notifications',
	success : function(data){
 		alert(data);
	},
	error : function(err){
		console.log(err);
	}
})