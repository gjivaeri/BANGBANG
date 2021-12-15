var writername = $("#writer_name").text()
var username = $("#user_name").text()

$(document).ready(function(){
if(username == writername){
  $(".change").removeClass("hidden");
}
})