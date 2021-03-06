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



//jquery ??????
//?????? ?????? ?????? ?????????
$(function() {
  $( ".datepicker" ).datepicker({
    changeMonth: true,
    changeYear: true,
    yearRange: "2017:2022",
    showButtonPanel: true,
    closeText: '??????', // ?????? ?????? ?????? 
    dateFormat: "yy-mm-dd", // ????????? ????????? ???????????? ?????? ??????. 
    showAnim: "slide", //?????????????????? ????????????.
    numberOfMonths: [1,2], 
  });
});


//?????? ?????? ????????? ????????????
function changeTheme(){
  selectValue = $("#id_theme_ID option:selected").val();
  pk = selectValue

  $.ajax({
      type: "POST", url: '/selectImg/', data: { 'pk': pk, 'csrfmiddlewaretoken': '{{ csrf_token }}' }, dataType: "json", 
      success: function (response) { // ??????
          $(".themeImg").html('<img src=/media/'+response+'>'); 
      },
      error: function (request, status, error) { // ??????
          alert("????????? ????????? ??????????????????");
      },
  });
  return false;  //???????????? ????????? ????????? ??????
};

//select ??????????????? ?????? ??????
var getUrlParameter = function getUrlParameter(sParam) {
  //url parameter??? ????????????, ??? ??? ???????????? ????????? ??????????????? ?????? ??????
  var sPageURL = decodeURIComponent(window.location.search.substring(1)),
      sURLVariables = sPageURL.split('&'),
      sParameterName,
      i;
      // console.log(sPageURL);
      //window.location.search??? ?sourid=chrom??? ?????? ????????? ????????? ??????. substring(1)??? ????????? ????????????????????? ?????????

  for (i = 0; i < sURLVariables.length; i++) {
      sParameterName = sURLVariables[i].split('=');

      if (sParameterName[0] === sParam) {
          return sParameterName[1] === undefined ? true : sParameterName[1];
      }
  }
};

$(function(){
  var theme_val = getUrlParameter('theme_ID');
  $('.#id_theme_ID').val(theme_val);
  $('.#id_theme_ID').change(function () {
    // console.log($(this).val());
    theme = $('.#id_theme_ID option:selected').val();
    $('.form').submit();
  })
});


