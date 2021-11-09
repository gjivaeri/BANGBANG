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

function review(){
  let click = document.getElementById("drop-content");
  click.style.display = "none";
  const element = document.getElementById('options');
  element.innerHTML = '리뷰순 <span id="triangle">▼</span>';
  // const spanTag = document.createElement("span");
  // const textNode = document.createTextNode('▼');
  // spanTag.appendChild(textNode);
  // document.querySelector('button:options').appendChild(spanTag);
}

function distance(){
  let click = document.getElementById("drop-content");
  click.style.display = "none";
  const element = document.getElementById('options');
  element.innerHTML = '거리순 <span id="triangle">▼</span>';
}

function price(){
  let click = document.getElementById("drop-content");
  click.style.display = "none";
  const element = document.getElementById('options');
  element.innerHTML = '가격낮은순 <span id="triangle">▼</span>';
}
