var data_p = JSON.parse(data_t.replaceAll(/&quot;/ig, '"'));
paint_areas(data_p, 1)
document.getElementById('mapdiv').style.display = "block";

function color_picker(value) {
    if (value < 15)
        return "lime"
    else if (150 > value > 15)
        return "green"
    else if (500 > value > 150)
        return "orange"
    else if (800 > value > 500)
        return "purple"
    else
        return "red"
}


function paint_areas(data, index) {
    let areas = document.getElementsByClassName("area")
    for (let x of areas) {
        x.style.fill = color_picker(data[index][x.id])

    }
}


function show_general_info(element) {
    let panel = document.getElementById('general-voivodeship-info')
    panel.querySelector("#voivodeship").innerHTML = element.getAttribute("xlink:title");
    panel.style.transform = "translateX(-500px)";
}

function hide_general_info() {
    let panel = document.getElementById('general-voivodeship-info')
    panel.style.transform = "translateX(+500px)";
}
