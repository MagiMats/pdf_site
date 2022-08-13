const checkbox1 = document.getElementById("checkbox1")
const checkbox2 = document.getElementById("checkbox2")
const checkbox3 = document.getElementById("checkbox3")

var progress = 0;

var i = 2;

function UpdateProgress() {
    var progressbar = document.getElementById("progress")
    if (checkbox1.checked == true) {
        progressbar.style.width = i + "%";
        i += 1
    }
}   