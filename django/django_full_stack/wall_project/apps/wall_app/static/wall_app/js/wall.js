$(document).ready(function(){
    // $('#username').keyup(function(){
    //     var data = $("#regForm").serialize()   // capture all the data in the form in the variable data
    //     $.ajax({
    //         method: "POST",   // we are using a post request here, but this could also be done with a get
    //         url: "/username",
    //         data: data
    //     })
    //     .done(function(res){
    //          $('#usernameMsg').html(res)  // manipulate the dom when the response comes back
    //     })
    // })

    // $('#usersearch').keyup(function(e){
    //     if(e.keyCode === 8 && $(this).text() === ""){
    //         $('#search-helper').html("");
    //     } else {        
    //         var data = $("#searchForm").serialize();
    //         $.ajax({
    //             method: "GET",
    //             url: "/usersearch",
    //             data: data
    //         }).done(function(res){
    //             $('#search-helper').html(res);
    //         });
    //     }
    // });
	var url = window.location.href;

	$("#post-new-message").submit(function(e){
		e.preventDefault();
		
		var data = $("#post-new-message").serialize();
		
		$.ajax({
			method: "POST",
			url: "messages/post",
			data: data
		}).done(function(res){
			$('body').html(res);
		});
	});

	$(".post-comment-form").submit(function(e){
		e.preventDefault();

		var formID = e.target.id, messageID = formID.match(/.*(\d+)/)[1];
		
		var data = $("#" + e.target.id).serialize();
		
		$.ajax({
			method: "POST",
			url: "messages/" + messageID + "/comments/post",
			data: data
		}).done(function(res){
			$('body').html(res);
		});
	});

	$(".delete-message-form").submit(function(e){
		e.preventDefault();

		var formID = e.target.id, messageID = formID.match(/.*-(\d+)/)[1];
		
		console.log(messageID);

		var data = $("#" + e.target.id).serialize();
		
		$.ajax({
			method: "POST",
			url: "messages/" + messageID + "/destroy",
			data: data
		}).done(function(res){
			$('body').html(res);
		});
	});
});