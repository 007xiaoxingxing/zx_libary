/**
 * Created by xiaoxing on 2016/12/23.
 */
$(document).ready(function () {

            $(".borrow").click(function () {
                openid = $(".back-it").attr("openid");
                location.href = "http://lib.star-chen.com/borrow?openid="+openid;

            });
            $(".person").click(function () {
                openid = $(".back-it").attr("openid");
                location.href = "http://lib.star-chen.com/person?openid="+openid;

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
        var book_id =$("#back-dlg").attr("book-id");
        $.ajax({

            url:"back",
            type:"POST",
            data:"{\"openID\":\""+openid+"\",\"bookID\":\""+book_id+"\"}",
            success:function(data){
                if(data == "success"){

                    $("#back-dlg").hide();
                    $("#book-"+book_id).remove();

                }
            }
        })
    });
        })