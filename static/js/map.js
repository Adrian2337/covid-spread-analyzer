document.getElementById('mapdiv').style.display = "block";

var map_data = jsonify(map_data_raw)
var dates = jsonify(dates_raw)


function color_picker(value, sum) {
    let lim1 = 0.3 * sum
    let lim2 = 0.5 * sum
    let lim3 = 0.6 * sum
    let lim4 = 0.8 * sum
    if (value < lim1 && value > 0)
        return "green"
    else if (lim2 > value)
        return "yellow"
    else if (lim3 > value)
        return "orange"
    else if (lim4 > value)
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
    console.log(data_json)
    for (let x of areas) {
        x.style.fill = color_picker(data_json[dates[index]]['Voivodeships'][x.id]['daily infected'], 600)

    }
}

function get_sum_all_casses(data, type) {
    data_json[dates[index]]['Voivodeships'][x.id]['daily infected']
}

paint_areas(map_data, 0)

function render_template() {
    let val = document.getElementById('voivodeship')
    let el = document.getElementById('statistics-link')
    el.href = '/statistics/' + val.innerHTML
    el.click()
}