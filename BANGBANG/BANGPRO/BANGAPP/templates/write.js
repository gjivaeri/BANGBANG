function checkfunction(rating)
{
var rating = document.getElementsByName('rating');
var score = document.querySelector('star_review_rate');
for(i=0; i<rating.length; i++) {
  if(rating[i].checked==true) {
    cosole.log(star_review_rate.value = rating[i].value);
  }
}
}