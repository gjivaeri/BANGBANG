const one = document.getElementById('first')
const two = document.getElementById('second')
const three = document.getElementById('third')
const four = document.getElementById('fourth')
const five = document.getElementById('fifth')

const form = document.querySelector('.rate-form')
const confirmBox = document.getElementById('confirm-box')

const csrf = document.getElementsByName('csrfmiddlewaretoken')

const handleStarSelect = (size) => {
  const children = form.children
  for (let i=0; i < children.length; i++) {
    if(i <= size){
      children[i].classList.add('checked')
    } else {
      children[i].classList.remove('checked')
    }
  }
}

const handleSelect = (selection) => {
  switch(selection){
    case 'first': {
      handleStarSelect(1)
      return
    }
    case 'second': {
      handleStarSelect(2)
      return
    }
    case 'third': {
      handleStarSelect(3)
      return
    }
    case 'fourth': {
      handleStarSelect(4)
      return
    }
    case 'fifth': {
      handleStarSelect(5)
      return
    }
  }
}

const getNumericValue = (stringValue) =>{
  let numericValue
  if (stringValue === 'first') {
    numericValue = 1
  }
  else if (stringValue === 'second'){
    numericValue = 2
  }
  else if (stringValue === 'third'){
    numericValue = 3
  }
  else if (stringValue === 'fourth'){
    numericValue = 4
  }
  else if (stringValue === 'fifth'){
    numericValue = 5
  }
  else {
    numericValue = 0
  }
  return numericValue
}


if (one){
  const arr = [one, two, three, four, five]
  arr.forEach(item => item.addEventListener('mouseover', (event)=>{
    console.log(event.target.id)
  }))

  arr.forEach(item=> item.addEventListener('click', (event)=>{
    const val = event.target.id
    console.log(val)
    let isSubmit = false

    form.addEventListener('submit', e=>{
      e.preventDefault()
      if(isSubmit){
        return
      }
      isSubmit = true
      const id = e.target.id
      console.log(id)
      const val_num = getNumericValue(val)

      $.ajax({
        type: 'POST', 
        url: 'rate/',
        data: {
          'csrfmiddlewaretoken': csrf[0].nodeValue,
          'el_id': id,
          'val': val_num,
        },
        success: function(response){
          console.log(response)
          confirmBox.innerHTML = `<h1>Successfully rated with ${response}</h1>`
        },
        error: function(error){
          console.log(error)
          confirmBox.innerHTML = '<h1>Ups.. something went wrong</h1>'
        }
      })
    })
  }))
}



//jquery 사용
//테마 방문 날짜 선택기
$(function() {
  $( ".datepicker" ).datepicker({
    changeMonth: true,
    changeYear: true,
    yearRange: "2020:2022",
    // You can put more options here.

  });
});


//선택 테마 이미지 불러오기
function changeTheme(){
  selectValue = $(".visitedTheme option:selected").val();
  pk = selectValue

  $.ajax({
      type: "POST", url: '/selectImg/', data: { 'pk': pk, 'csrfmiddlewaretoken': '{{ csrf_token }}' }, dataType: "json", 
      success: function (response) { // 성공
          $(".themeImg").html('<img src=/media/'+response+'>'); // 좋아요 개수 변경
      },
      error: function (request, status, error) { // 실패
          alert("방문한 테마를 선택해주세요");
      },
  });
  return false;  //새로고침 시키지 말라고 넣음
};

//select 유지시키기 위한 함수
var getUrlParameter = function getUrlParameter(sParam) {
  //url parameter를 얻어온다, 그 후 대부분의 문자를 디코딩하는 함수 사용
  var sPageURL = decodeURIComponent(window.location.search.substring(1)),
      sURLVariables = sPageURL.split('&'),
      sParameterName,
      i;
      // console.log(sPageURL);
      //window.location.search는 ?sourid=chrom과 같은 부분을 가지고 온다. substring(1)로 객체의 시작인덱스부터 가져옴

  for (i = 0; i < sURLVariables.length; i++) {
      sParameterName = sURLVariables[i].split('=');

      if (sParameterName[0] === sParam) {
          return sParameterName[1] === undefined ? true : sParameterName[1];
      }
  }
};

$(function(){
  var theme_val = getUrlParameter('theme_ID');
  $('.visitedTheme').val(theme_val);
  $('.visitedTheme').change(function () {
    // console.log($(this).val());
    theme = $('.visitedTheme option:selected').val();
    $('.form').submit();
  })
});




//수연님 js
// $(document).ready(function() {
//   $("form#ratingForm").click(function(e) 
//   {
//       e.preventDefault(); // prevent the default click action from being performed
//       if ($("#ratingForm :radio:checked").length == 0) {
//           $('#star_review_rate').html("nothing checked");
//           return false;
//       } else {
//           $('#star_review_rate').html($('input:radio[name=themeRevStar]:checked').val() + '점');
//       }
//   });
// });

// function checkfunction(rating)
// {
// var rating = document.getElementsByName('rating');
// var score = document.querySelector('star_review_rate');
// for(i=0; i<rating.length; i++) {
//   if(rating[i].checked==true) {
//     cosole.log(star_review_rate.value = rating[i].value);
//   }
// }
// }
//