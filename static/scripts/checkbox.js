const checkbox = document.getElementsByTagName("input")
var i = 0;

function UpdateProgress(item, increment) {
    var progressbar = document.getElementById("progress");
    
    localStorage.setItem(1, checkbox.checked);
    console.log(localStorage);

    if (item.checked) {
        i++;
        progressbar.style.width = i*increment*100 + "%";

    } else {
        i--;
        progressbar.style.width = i*increment*100 + "%";
    }
}   

function load() {
    for (check in checkbox) {
        try{
            var checked = JSON.parse(localStorage.getItem(check.innerHTML));
            console.log(checked);
        } catch {
            console.log(check);
        }
        try {document.getElementById(check).checked = checked;}
        catch{}
    }
}

load();