$(document).ready(function(){
    $('#username').keyup(function(){
        var data = $("#regForm").serialize()   // capture all the data in the form in the variable data
        $.ajax({
            method: "POST",   // we are using a post request here, but this could also be done with a get
            url: "/username",
            data: data
        })
        .done(function(res){
             $('#usernameMsg').html(res)  // manipulate the dom when the response comes back
        })
    })

    $('#usersearch').keyup(function(e){
        if(e.keyCode === 8 && $(this).text() === ""){
            $('#search-helper').html("");
        } else {        
            var data = $("#searchForm").serialize();
            $.ajax({
                method: "GET",
                url: "/usersearch",
                data: data
            }).done(function(res){
                $('#search-helper').html(res);
            });
        }
    });
})