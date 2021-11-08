$(document).ready(function() {
  $("form#ratingForm").click(function(e) 
  {
      e.preventDefault(); // prevent the default click action from being performed
      if ($("#ratingForm :radio:checked").length == 0) {
          $('#star_review_rate').html("nothing checked");
          return false;
      } else {
          $('#star_review_rate').html($('input:radio[name=themeRevStar]:checked').val() + '점');
      }
  });
});