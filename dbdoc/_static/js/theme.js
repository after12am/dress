window.SphinxRtdTheme = (function (jquery) {
    var stickyNav = (function () {
        var navBar,
            win,
            stickyNavCssClass = 'stickynav',
            applyStickNav = function () {
                if (navBar.height() <= win.height()) {
                    navBar.addClass(stickyNavCssClass);
                } else {
                    navBar.removeClass(stickyNavCssClass);
                }
            },
            enable = function () {
                applyStickNav();
                win.on('resize', applyStickNav);
            },
            init = function () {
                navBar = jquery('nav.wy-nav-side:first');
                win    = jquery(window);
            };
        jquery(init);
        return {
            enable : enable
        };
    }());
    return {
        StickyNav : stickyNav
    };
}($));


$(function() {
    
    // Shift nav in mobile when clicking the menu.
    $(document).on('click', "[data-toggle='wy-nav-top']", function() {
      $("[data-toggle='wy-nav-shift']").toggleClass("shift");
      $("[data-toggle='rst-versions']").toggleClass("shift");
    });
    // Close menu when you click a link.
    $(document).on('click', ".wy-menu-vertical .current ul li a", function() {
      $("[data-toggle='wy-nav-shift']").removeClass("shift");
      $("[data-toggle='rst-versions']").toggleClass("shift");
    });
    $(document).on('click', "[data-toggle='rst-current-version']", function() {
      $("[data-toggle='rst-versions']").toggleClass("shift-up");
    });  
    // Make tables responsive
    $("table.docutils:not(.field-list)").wrap("<div class='wy-table-responsive'></div>");
    
    // search keyword
    $('input.search').keyup(function(e) {
        
        var word = $(this).val();
        var $docs = $('.document > .section');
        var $menu = $('.wy-menu .simple a');
        
        function filter() {
            
            var $this = $(this);
            var $imenu = $('.wy-menu .simple .' + $this.attr('id'));
            
            $this.removeHighlight().highlight(word);
            
            if ($this.find('.highlight').length > 0) {
                $this.show();
                $imenu.show();
            } else {
                $this.hide();
                $imenu.hide();
            }
        }
        
        if (word.length > 0) {
            $docs.each(filter);
        } else {
            $docs.removeHighlight().show();
            $menu.show();
        }
    });
    
    function update_navi(hash) {
        $('.wy-menu li').removeClass('current');
        $('.wy-menu li[data-hash=' + hash + ']').toggleClass('current');
    }
    
    update_navi(location.hash.split('#')[1]);
    $('.wy-menu li a').click(function() {
        var hash = $(this).parent().attr('data-hash');
        update_navi(hash);
    });

    SphinxRtdTheme.StickyNav.enable();
});