/**
 * Created by xiaoxing on 2016/12/23.
 */
$(document).ready(function(){

            $(".borrow").click(function(){

                location.href="http://lib.star-chen.com/borrow?openid=123";

            });
            $(".person").click(function(){

                location.href="http://lib.star-chen.com/person?openid=123";

            });

            $(".book-item").click(function(){

                $("#borrow-dlg").show();
            });

            $(".give-up").click(function(){

                $("#borrow-dlg").hide();

            });
        })