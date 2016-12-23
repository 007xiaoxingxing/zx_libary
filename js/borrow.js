/**
 * Created by xiaoxing on 2016/12/23.
 */
$(document).ready(function () {

    $(".borrow").click(function () {

        location.href = "http://lib.star-chen.com/borrow?openid=123";

    });
    $(".person").click(function () {

        location.href = "http://lib.star-chen.com/person?openid=123";

    });

    $(".book-item").click(function () {

        var book_id = $(this).attr("id").substr(5);
        console.log(book_id);
        $("#borrow-dlg").show();

    });

    $(".give-up").click(function () {

        $("#borrow-dlg").hide();

    });

    $(".borrow-it").click(function () {
        var openid = "123";
        var bookID = "1";
        $.ajax({
            url: "borrow",
            type: "POST",
            data: "{\"openID\":\""+openid+"\",\""+bookID+"\":\"1\"}",
            success: function (data) {
                if (data == "success") {
                    $("#borrow-dlg").hide();
                    $("#book-"+bookID+" .book-status").html("已借出");
                    $("#book-"+bookID+" .book-status").css("color", "#f00");

                }
            }
        })

    });
})