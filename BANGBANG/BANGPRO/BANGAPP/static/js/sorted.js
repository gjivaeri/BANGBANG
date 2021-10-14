var getUrlParameter = function getUrlParameter(sParam) {
  //url parameter를 얻어온다, 그 후 대부분의 문자를 디코딩하는 함수 사용
  var sPageURL = decodeURIComponent(window.location.search.substring(1)),
      sURLVariables = sPageURL.split('&'),
      sParameterName,
      i;

      //window.location.search는 ?sourid=chrom과 같은 부분을 가지고 온다. substring(1)로 객체의 시작인덱스부터 가져옴

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

//attr은 스크립트로 추가된 엘리먼트는 컨트롤 할 수 없어서 prop사용함
