function dp_menu(){
  let click = document.getElementById("drop-content");
  if(click.style.display === "none"){
      click.style.display = "block";
  }else{
      click.style.display = "none";
  }
  const triangle = document.getElementById('triangle');
  if(triangle.innerText === '▼') {
      triangle.innerText = '▲';
  } else triangle.innerText ='▼';
}

function like(){
  location.href='/home/?sort=-themeLike';
}

function distance(){
  let click = document.getElementById("drop-content");
  click.style.display = "none";
  const element = document.getElementById('options');
  element.innerHTML = '거리순 <span id="triangle">▼</span>';
}

function price(){
  location.href='/home/?sort=-themePrice';
}


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

// // 정렬방식 셀렉트 박스 유지
$(document).ready(function(){
  var sort = getUrlParameter('sort');
  if(sort == '-themeLike'){
    let click = document.getElementById("drop-content");
    click.style.display = "none";
    const element = document.getElementById('options');
    element.innerHTML = '좋아요순 <span id="triangle">▼</span>';
  }else if(sort == '-themePrice'){
    let click = document.getElementById("drop-content");
    click.style.display = "none";
    const element = document.getElementById('options');
    element.innerHTML = '가격낮은순 <span id="triangle">▼</span>';
  }else{
    // $('.sort-date').prop('selected', true)
  }
  });






//거리순 필터링을 위한 위치정보 불러오기 + 거리계산
let shops = [
  {name:"강남방탈출", latitude:37.50201131555239, longitude:127.02536556486315},
  {name:"신촌방탈출", latitude:37.5720302842096, longitude:126.94168614116083},
  {name:"부천방탈출", latitude:37.487075729793915, longitude:126.78200703369356},
  {name:"대학로방탈출", latitude:37.59319726685757, longitude:127.00208348755136}
]

//거리계산함수
function getDistance(lat1, lon1, lat2, lon2, unit) {
	if ((lat1 == lat2) && (lon1 == lon2)) {
		return 0;
	}
	else {
		var radlat1 = Math.PI * lat1/180;
		var radlat2 = Math.PI * lat2/180;
		var theta = lon1-lon2;
		var radtheta = Math.PI * theta/180;
		var dist = Math.sin(radlat1) * Math.sin(radlat2) + Math.cos(radlat1) * Math.cos(radlat2) * Math.cos(radtheta);
		if (dist > 1) {
			dist = 1;
		}
		dist = Math.acos(dist);
		dist = dist * 180/Math.PI;
		dist = dist * 60 * 1.1515;
		if (unit=="K") { dist = dist * 1.609344 } //킬로미터 계산
		if (unit=="N") { dist = dist * 0.8684 }
		return dist;
	}
}

//현위치 불러와서 거리비교 하는 함수 (html5 Geolocation API 사용)
navigator.geolocation.getCurrentPosition((position) => {
  let latitude = position.coords.latitude;
  let longitude = position.coords.longitude;
  
  console.log(latitude, longitude);

  for(let i=0; i<shops.length; i++) {
    let distance = getDistance(latitude, longitude, shops[i].latitude, shops[i].longitude, "K")
    shops[i].distance = distance;
  }

  let calShop = shops.sort(function (a, b){
    if (a.distance > b.distance){
      return 1;
    }
    if (a.distance < b.distance){
      return -1;
    }
    return 0
  }); //거리순에 따라 오름차순 순으로 정렬해준다.
  console.log(calShop)
}, (err) => {

});
