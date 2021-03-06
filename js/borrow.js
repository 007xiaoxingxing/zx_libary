/**
 * Created by xiaoxing on 2016/12/23.
 */
$(document).ready(function () {

    $(".borrow").click(function () {
        var openid = $("#borrow-dlg").attr("openid");
        location.href = "http://lib.star-chen.com/borrow?openid=" + openid;

    });
    $(".person").click(function () {
        var openid = $("#borrow-dlg").attr("openid");
        location.href = "http://lib.star-chen.com/person?openid=" + openid;

    });

    $(".book-item").click(function () {

        var book_id = $(this).attr("id").substr(5);
        var status = $("#book-" + book_id + " .book-status").html();
        if (status == "可外借") {
            var book_des = $("#book-" + book_id + " .origin-des").html();
            $(".book-des").html(book_des);
            $("#borrow-dlg").attr("book_id", book_id);
            $("#borrow-dlg").show();
        }
        else {
            $.ajax({

                url: "borrowInfo?bookid=" + book_id,
                type: "GET",
                success: function (data) {
                    if (data != "") {

                        obj = JSON.parse(data);
                        borrower = obj.borrower;
                        borrow_time = obj.borrowTime;
                        info = borrower + "借于" + borrow_time;
                        console.log(info);
                        $(".borrow_detail").html(info);
                        $("#borrow-info").show();
                    }
                }
            });
        }
    });
    $(".know-btn").click(function () {

        $("#borrow-info").hide();
    });
    $(".give-up").click(function () {

        $("#borrow-dlg").hide();

    });

    $(".borrow-it").click(function () {
        var openid = $("#borrow-dlg").attr("openid");
        var bookID = $("#borrow-dlg").attr("book_id");
        $.ajax({
            url: "borrow",
            type: "POST",
            data: "{\"openID\":\"" + openid + "\",\"bookID\":\"" + bookID + "\"}",
            success: function (data) {
                if (data == "success") {
                    $("#borrow-dlg").hide();
                    $("#book-" + bookID + " .book-status").html("外借待办");
                    $("#book-" + bookID + " .book-status").css("color", "#f00");

                }
            }
        })

    });
})