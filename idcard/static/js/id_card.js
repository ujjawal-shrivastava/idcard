(function(){
            var menu_trigger = $("[data-card-menu]");
            var back_trigger = $("[data-card-back]");
            
            menu_trigger.click(function(){
                $(".card, body").toggleClass("show-menu");
            });    
               
            back_trigger.click(function(){
                $(".card, body").toggleClass("show-menu");
            });    
            
            window.oncontextmenu = function () {
                return false;
            }
            $(document).keydown(function (event) {
                if (event.keyCode == 123) {
                    return false;
                }
                else if ((event.ctrlKey && event.shiftKey && event.keyCode == 73) || (event.ctrlKey && event.shiftKey && event.keyCode == 74)) {
                    return false;
                }
            });
        })();
        