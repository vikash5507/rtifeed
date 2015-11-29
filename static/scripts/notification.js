function get_notifications(){
	$.ajax({
		url : '/get_notifications',
		dataType : 'json',
		success : function(data){
			// alert(data['notification_list_html']);
	 		$('#notification_container').html(data['notification_list_html']);
	 		if(data['no_unread_notifications'] > 1){
	 			$('#notification_header').html('You have ' + data['no_unread_notifications'] + ' new notifications');
	 		}
	 		if(data['no_unread_notifications'] == 1){
	 			$('#notification_header').html('You have ' + data['no_unread_notifications'] + ' new notification');	
	 		}
	 		if(data['no_unread_notifications'] > 0){
	 			$('#notification_number').html(data['no_unread_notifications']);	
	 		}
	 	},
		error : function(err){
			console.log(err);
		}
	});	
}


$('#notification_toggle').click(function(){
	$.ajax({
		url : 'mark_all_notifications',
		success : function(data){
			$('#notification_number').html("");	
		},
		error : function(err){
			console.log(err);
		}
	})
});

get_notifications();