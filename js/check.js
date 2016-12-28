/**
 * Created by xiaoxing on 2016/12/28.
 */
$(document).ready(function () {



    $(".check-btn").click(function () {

        var book_id = $(this).attr("book-id");
        $.ajax({

            url:"check",
            type:"POST",
            data:"{\"bookID\":"+book_id+"}",
            success:function (data) {

                console.log(data);
            }
        })
    });

});