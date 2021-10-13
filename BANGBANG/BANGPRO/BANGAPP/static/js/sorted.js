var getUrlParameter = function getUrlParameter(sParam) {
  var sPageURL = decodeURIComponent(window.location.search.substring(1)),
      sURLVariables = sPageURL.split('&'),
      sParameterName,
      i;

  for (i = 0; i < sURLVariables.length; i++) {
      sParameterName = sURLVariables[i].split('=');

      if (sParameterName[0] === sParam) {
          return sParameterName[1] === undefined ? true : sParameterName[1];
      }
  }
};
// 정렬방식 셀렉트 박스 유지
$(document).ready(function(){
var sort = getUrlParameter('sort');
if(sort == 'themeRevRecom'){
  $('.sort-likes').prop('selected', 'selected')
}else if(sort == 'themeRevRating'){
  $('.sort-rating').prop('selected', 'selected')
}else{
  $('.sort-date').prop('selected', 'selected')
}
});