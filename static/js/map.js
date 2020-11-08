document.getElementById('mapdiv').style.display = "block";

var map_data = jsonify(map_data_raw)
var dates = jsonify(dates_raw)


function color_picker(value) {
    console.log(value)
    if (value < 1200 && value > 0)
        return "green"
    else if (1700 > value)
        return "yellow"
    else if (2300 > value)
        return "orange"
    else if (3500 > value)
        return "red"
    else
        return "purple"
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

function jsonify(variable) {
    return JSON.parse(variable.replaceAll(/&quot;/ig, '"').replaceAll('&#x27;', '"'));

}

function paint_areas(data_json, index) {
    let areas = document.getElementsByClassName("area")
    for (let x of areas) {
        console.log(data_json[dates[index]]['Voivodeships'][x.id]['daily infected'], x.id, dates[index])
        x.style.fill = color_picker(data_json[dates[index]]['Voivodeships'][x.id]['daily infected'])

    }
}

paint_areas(map_data, 0)
