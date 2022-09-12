// navbar
function hideIconBar(){
    var iconBar = document.getElementById("iconBar");
    var navigation = document.getElementById("navigation");
    iconBar.setAttribute("style", "display:none;");
    navigation.classList.remove("hide-nav");
}

function showIconBar(){
    var iconBar = document.getElementById("iconBar");
    var navigation = document.getElementById("navigation");
    iconBar.setAttribute("style", "display:block;");
    navigation.classList.add("hide-nav");
}

// dynamic Date
var year = new Date().getFullYear();
var date = `&copy; &nbsp;Forrum ${year} | All Rights Reserved.`
document.getElementsByTagName('footer')[0].innerHTML = date;