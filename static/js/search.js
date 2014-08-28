$(function() {
    
    function highlighted(word) {
        return function() {
            
            var escaped = word.replace('/\'/', '\\\'');
            var re = new RegExp("(" + escaped + ")", "gi");
            var rep_text = $('<span>$1</span>').addClass('highlighted')[0].outerHTML
            
            $(this).children().each(function() {
                // excludes table header
                if (this.nodeName.toLowerCase() === 'th') return;
                // walk through, and highlight the searched word
                $.proxy(highlighted(escaped), this)();
            });
            
            $(this).html($(this).html().replace(/\r/, ''));
            $(this).contents().each(function() {
                if (this.nodeType === 3) {
                    if ($(this).text().match(re)) {
                        $(this).replaceWith($(this).text().replace(re, rep_text))
                    }
                }
            });
        }
    }
    
    function search(word) {
        
        $('.document > .section').each(highlighted(word));
        $('.document > .section').each(function() {
            var id = $(this).attr('id');
            if ($(this).find('.highlighted').length > 0) {
                $(this).show();
                $('.wy-menu .simple .' + id).show();
            } else {
                $(this).hide();
                $('.wy-menu .simple .' + id).hide();
            }
        });
    }
    
    $('input.search').keyup(function(e) {
        
        $('.highlighted').replaceWith(function() {
            return $(this).text();
        });
        
        var search_word = $(this).val();
        if (search_word.length > 0) {
            search(search_word);
        } else {
            $('.document > .section').show();
            $('.wy-menu .simple a').show();
        }
        
    });
    
});