const checkbox = document.getElementsByTagName("input")
var i = 0;

function UpdateProgress(item, increment) {
    var progressbar = document.getElementById("progress");

    if (item.checked) {
        i++;
        progressbar.style.width = i*increment*100 + "%";

    } else {
        i--;
        progressbar.style.width = i*increment*100 + "%";
    }
}   

