$(document).ready(function() {
    $('.blog-likes').click(function() {
        var id;
        id = $(this).attr('data-blog-id');
        $.get('/like-blog/', {
            blog_id: id
        }, function(data) {
            $('.like_count_blog').html(data);
        });
    });
});