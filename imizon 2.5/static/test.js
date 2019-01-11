function show() {
  var x = document.getElementById("myDIV");
  x.style.display = "block";
}

function hide() {
	var x = document.getElementById("myDIV");
	x.style.display = "none";
}

function toggleBuy() {
  var test = document.querySelector('#defaultCheck1').checked;
  var x = document.getElementById("checkBuy");
  if(test) x.classList.remove("disabled");
  else  x.classList.add("disabled");
}

function timerFeedback() {
  setTimeout(goToFdb, 10000);
}
function goToFdb() {
  window.location.href = 'feedbacks';
}

// function showShipping(divID) {
// 	// var x = document.getElementById("FCA");
// 	// x.style.display = "block";
// 	document.getElementById("FCA").style.display = "none";
// 	document.getElementById("FOB").style.display = "none";
// 	document.getElementById("DDP").style.display = "none";
// 	document.getElementById("EXW").style.display = "none";
// 	document.getElementById(divID).style.display = "block";
// }