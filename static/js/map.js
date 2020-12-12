document.getElementById('mapdiv').style.display = "block";

var map_data = jsonify(map_data_raw)
var dates = jsonify(dates_raw)


function color_picker(value, sum) {
    let lim1 = 0.1 * sum
    let lim2 = 0.2 * sum
    let lim3 = 0.3 * sum
    let lim4 = 0.4 * sum
    let lim5 = 0.5 * sum
    let lim6 = 0.6 * sum
    let lim7 = 0.7 * sum
    let lim8 = 0.8 * sum
    let lim9 = 0.9 * sum
    let lim10 = 1.0 * sum

    if (value < lim1 && value > 0)
        return "#00ffbf"
    else if (lim2 > value)
        return "#00ff80"
    else if (lim3 > value)
        return "#80ff00"
    else if (lim4 > value)
        return "#bfff00"
    else if (lim5 > value)
        return "#ffff00"
    else if (lim6 > value)
        return "#ffbf00"
    else if (lim7 > value)
        return "#ff8000"
    else if (lim8 > value)
        return "#ff4000"
    else if (lim9 > value)
        return "#d92626"
    else if (lim10 > value)
        return "#b94646"
    else
        return "#9f6060"
}

function color_picker3(value, pred_max) {
    let lim1 = pred_max * 0.3
    let lim2 = pred_max * 0.6
    let lim3 = pred_max * 0.75
    let lim4 = pred_max * 0.9
    if (value < lim1 && value > 0)
        return "LightSkyBlue"
    else if (lim2 > value)
        return "Blue"
    else if (lim3 > value)
        return "MediumBlue"
    else if (lim4 > value)
        return "DarkBlue"
    else
        return "Navy"
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
    sum = 100_000

    
    for (let x of areas) {

        // below count days from beginnig of data collections
        var then = new Date(2020, 9, 25) // (count 09 as ocotober) month is zero based XDDD
        now = new Date();

        days = Math.round(Math.abs(now - then) / (1000 * 60 * 60 * 24));

        till_today_infected = 0

        for (days; days >= index; days--) {
            till_today_infected += data_json[dates[days]]['Voivodeships'][x.id]['daily infected']
        }

        x.style.fill = color_picker(till_today_infected, sum)

        
    }

    
}

function get_date_from_knob(data_json, index) {
    date = data_json[dates[index]]['date']
    document.getElementById("date-div").value = date;
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

function get_max_case(data, idx) {
    let max = 0
    for (let x in data) {
        let val = data[x][idx]
        if (max < val) {
            max = val
        }
    }
    return max
}

