/**
 * Created by xiaoxing on 2016/12/28.
 */
$(document).ready(function () {



    $(".check-btn").click(function () {

        var book_id = $(this).attr("book-id");
        var type = $(this).attr("type");
        $.ajax({

            url:"check",
            type:"POST",
            data:"{\"bookID\":"+book_id+",\"type\":\""+type+"\"}",
            success:function (data) {

                if(data == "success"){

                    $("#book-"+book_id).remove();
                }
            }
        })
    });

});