function displaytips() {
    tipbutt = document.getElementsByClassName("tipsbutton")[0];
    tips = document.getElementById("tips");
    if (tipbutt.innerHTML == "Tips") {
        tips.style.display = "block";
        tipbutt.innerHTML = "Hide"
    }
    else {
        tips.style.display = "none";
        tipbutt.innerHTML = "Tips"
    }
}