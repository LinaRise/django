  
function input() {
  var x = document.getElementById("areatoShowOrHide");
  if (x.style.display === "none") {
	  var text = "В свободное времы люблю танцевать. Много читаю";
    document.forms.form1.area.value = text;
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}