$('#listButton').click(function() {
  $.ajax({
      type: "GET",
      url:"/themeRevAddDetail/", // list url을 불러옴
      dataType: 'html', // list의 형태는 html
      success: function(data){ // 성공했을 때 일단 good을 alert로 띄운다.
          alert('good');
          $('#example').html(data) // 그 이후에 example div에 list html의 data를 가져온다.
      },
      error: function(request, status, error){ // 실패했을 때 bad alert, 에러가 무엇이었는지, 그리고 간단한 html 출력
          alert('bad');
          alert(error);
          $('#example').html('AJAX 통신에 실패했습니다.');
      }
  })
})