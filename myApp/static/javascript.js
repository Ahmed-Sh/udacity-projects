$(function () {
    $(form).submit(function (event) {
        event.preventDefault()
    });

    // Add Posts
    var title = $("input[name='title']"),
        content = $("input[name='content']"),
        topicData = {
            "title":title,
            "content":content
        };
    $.ajax({
        type:"POST",
        url:"/api/topic/add",
        data:JSON.stringify(topicData),
        contentType:"application/json;charset=utf-8",
        dataType:"json",
        success: function (response) {
            alert("Add topic successfully!")
        }
    });

    // Remove Posts
    $("#delete_button").click(function(){
    var post = $(this), post_id =  $(this).data('id');
    $.ajax({
        type: "PATCH",
        dataType: "json",
        data: { "approved": "True"},
        url: "/topic/delete/" + post_id + "/?format=json",
        success: function(data){
            post.remove();
            alert("Deleted topic successfully!");
        }
    });
});
});