var last_fetched_id = null;
function get_notifications(notification_type){
	$.ajax({
		url : '/get_notifications',
		dataType : 'json',
		data : {
			notification_type : notification_type,
		},
		success : function(data){
			// alert(data['notification_list_html']);
			if(data['num_new_messages'] > 0){
				$('#num_new_messages').html(data['num_new_messages']);
			}
			else{
				$('#num_new_messages').html("");
			}

			if(notification_type == 'all'){
				$('#notification_container').html(data['notification_list_html']);	
			}
			else{
				$('#notification_container').prepend(data['notification_list_html']);	
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
		url : '/mark_all_notifications',
		success : function(data){
			$('#notification_number').html("");	
		},
		error : function(err){
			console.log(err);
		}
	})
});

get_notifications('all');

window.setInterval(function(){
  get_notifications('unread');
}, 5000);

