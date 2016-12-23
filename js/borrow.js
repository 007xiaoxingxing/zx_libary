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
        var status = $("#book-"+book_id+" .book-status").html();
        if(status == "可外借"){
            var book_des = $("#book-"+book_id+" .origin-des").html();
            $(".book-des").html(book_des);
            $("#borrow-dlg").attr("book_id",book_id);
            $("#borrow-dlg").show();
        }
        else if(status == "已外借")
            console.log("已外借");

    });

    $(".give-up").click(function () {

        $("#borrow-dlg").hide();

    });

    $(".borrow-it").click(function () {
        var openid = $("#borrow-dlg").attribute("openid");
        var bookID = $("#borrow-dlg").attribute("book_id");
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