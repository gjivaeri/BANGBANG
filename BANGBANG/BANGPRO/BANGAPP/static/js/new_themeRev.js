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