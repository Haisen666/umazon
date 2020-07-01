$(function() {
    $('.hover-activate').hover(
        function() {
          $(this).find('.account-hover').addClass('account-active');
          
        },
        function() {
          $(this).find('.account-hover').removeClass('account-active');
          
        }
      );

});
