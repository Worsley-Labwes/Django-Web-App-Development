$(document).ready(function() {
    $("#postForm").submit(function(event) {
        event.preventDefault();
        let title = $("#postTitle").val();
        let content = $("#postContent").val();
        let csrfToken = $("input[name=csrfmiddlewaretoken]").val();

        $.ajax({
            type: "POST",
            url: "/add_post/",
            data: {
                'title': title,
                'content': content,
                'csrfmiddlewaretoken': csrfToken
            },
            success: function(response) {
                if (response.status === "success") {
                    $("#postList").prepend(
                        `<li id="post-${response.id}">
                            <strong class="post-title">${response.title}</strong> - You
                            <button class="btn btn-warning btn-sm edit-btn" data-id="${response.id}">Edit</button>
                            <button class="btn btn-danger btn-sm delete-btn" data-id="${response.id}">Delete</button>
                        </li>`
                    );
                    $("#postTitle").val('');
                    $("#postContent").val('');
                } else {
                    alert("Error: Could not add post.");
                }
            }
        });
    });
});
