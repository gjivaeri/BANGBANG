$(".like").click(function () { // .like 버튼을 클릭 감지
  likeButton = $(this)
  pk = likeButton.attr('name')
  $.ajax({
      type: "POST", url: '/like/', data: { 'pk': pk, 'csrfmiddlewaretoken': '{{ csrf_token }}' }, dataType: "json", 
      success: function (response) { // 성공
          // alert(response.message);
          $("#count-" + pk).html(response.like_count + "+"); // 좋아요 개수 변경
      },
      error: function (request, status, error) { // 실패
          alert("로그인이 필요합니다.");
          window.location.replace("/registration/login/") // 로그인 페이지로 넘어가기
      },
  });
  return false;  //새로고침 시키지 말라고 넣음
})