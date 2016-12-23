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
                var book_id =$(this).attr("book-id");
                $("#back-dlg").attr("book-id",book_id);
                $("#back-dlg").show();
            });

            $(".give-up").click(function () {

                $("#back-dlg").hide();

            });
    $(".back-it").click(function () {

        var openid =$(".back-it").attr("openid");
        var book_id =$(".back-it").attr("book-id");
        $.ajax({

            url:"back",
            type:"POST",
            data:"{\"openID\":\""+open()+"\",\"bookID\":\""+book_id+"\"}",
            success:function(data){
                alert(data);
            }
        })
    });
        })