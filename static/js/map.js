document.getElementById('mapdiv').style.display = "block";

var map_data = jsonify(map_data_raw)
var dates = jsonify(dates_raw)
var voivodes = jsonify(voivodes_raw)


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

function check_undefined(value) {
    if (value === undefined || isNaN(value))
        return 'no data'
    else
        return value
}

function get_sum(data, day, type) {
    let result = 0
    for (let x in data) {
        result += data[x][day][type]
    }
    return result
}


function show_general_info(element) {
    let panel = document.getElementById('general-voivodeship-info')
    let txt = element.getAttribute("xlink:title");
    panel.querySelector("#voivodeship").innerHTML = txt
    panel.style.transform = "translateX(-500px)";
    let v = document.getElementById("date-div").value
    document.getElementById('label-inf').innerText = v + " overall statistics"
    document.getElementById('total-val').innerText = check_undefined(voivodes[txt][v]['daily infected'])
    document.getElementById('cured-val').innerText = check_undefined(voivodes[txt][v]['daily cured'])
    document.getElementById('deaths-val').innerText = check_undefined(voivodes[txt][v]['daily deceased'])

    document.getElementById('total-val-pol').innerText = check_undefined(get_sum(voivodes, v, 'daily infected'))
    document.getElementById('cured-val-pol').innerText = check_undefined(get_sum(voivodes, v, 'daily cured'))
    document.getElementById('deaths-val-pol').innerText = check_undefined(get_sum(voivodes, v, 'daily deceased'))
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
    let cases = []

    for (let x of areas) {

        week = 7;

        count_from = week + index

        for (count_from; count_from >= index; count_from--) {

            cases.push(data_json[dates[count_from]]['Voivodeships'][x.id]['daily infected'])
        }

    }

    sum = Math.max.apply(null, cases)

    for (let x of areas) {

        week = 7;

        count_from = week + index

        till_today_infected = 0

        for (count_from; count_from >= index; count_from--) {
            till_today_infected += data_json[dates[count_from]]['Voivodeships'][x.id]['daily infected']

            cases.push(data_json[dates[count_from]]['Voivodeships'][x.id]['daily infected'])
        }

        mid = till_today_infected / week
        x.style.fill = color_picker(mid, sum)


    }

    let areasII = document.getElementsByClassName("scale-table")

    for (let xII of areasII) {
        xII.value = String(parseInt(xII.id * sum))
        xII.style.backgroundColor = color_picker(parseInt(xII.value), sum);
    }

}

function btn_infected() {

    document.getElementById("daily infected").value = "True"
    document.getElementById("daily infected").style.backgroundColor = "rgba(3, 75, 35, 0.95)"
    document.getElementById("daily cured").value = "False"
    document.getElementById("daily cured").style.backgroundColor = "black"
    document.getElementById("daily deceased").value = "False"
    document.getElementById("daily deceased").style.backgroundColor = "black"

    $('.knob').val(1).trigger('change')
    $('.knob').val(0).trigger('change')

}


function btn_cured() {

    document.getElementById("daily infected").value = "False"
    document.getElementById("daily infected").style.backgroundColor = "black"
    document.getElementById("daily cured").value = "True"
    document.getElementById("daily cured").style.backgroundColor = "rgba(3, 75, 35, 0.95)"
    document.getElementById("daily deceased").value = "False"
    document.getElementById("daily deceased").style.backgroundColor = "black"
    $('.knob').val(1).trigger('change')
    $('.knob').val(0).trigger('change')

}


function btn_deceased() {

    document.getElementById("daily infected").value = "False"
    document.getElementById("daily infected").style.backgroundColor = "black"
    document.getElementById("daily cured").value = "False"
    document.getElementById("daily cured").style.backgroundColor = "black"
    document.getElementById("daily deceased").value = "True"
    document.getElementById("daily deceased").style.backgroundColor = "rgba(3, 75, 35, 0.95)"
    $('.knob').val(1).trigger('change')
    $('.knob').val(0).trigger('change')
}


function paint_areas_death(data_json, index) {
    let areas = document.getElementsByClassName("area")
    let cases = []

    for (let x of areas) {

        week = 7;

        count_from = week + index

        for (count_from; count_from >= index; count_from--) {

            cases.push(data_json[dates[count_from]]['Voivodeships'][x.id]['daily deceased'])
        }

    }

    sum = Math.max.apply(null, cases)

    for (let x of areas) {

        week = 7;

        count_from = week + index

        till_today_infected = 0

        for (count_from; count_from >= index; count_from--) {
            till_today_infected += data_json[dates[count_from]]['Voivodeships'][x.id]['daily deceased']

            cases.push(data_json[dates[count_from]]['Voivodeships'][x.id]['daily deceased'])
        }

        mid = till_today_infected / week
        x.style.fill = color_picker(mid, sum)


    }

    let areasII = document.getElementsByClassName("scale-table")

    for (let xII of areasII) {
        xII.value = String(parseInt(xII.id * sum))
        xII.style.backgroundColor = color_picker(parseInt(xII.value), sum);
    }

}


function paint_areas_cured(data_json, index) {
    let areas = document.getElementsByClassName("area")
    let cases = []

    for (let x of areas) {

        week = 7;

        count_from = week + index

        for (count_from; count_from >= index; count_from--) {

            cases.push(data_json[dates[count_from]]['Voivodeships'][x.id]['daily cured'])
        }

    }

    sum = Math.max.apply(null, cases)

    for (let x of areas) {

        week = 7;

        count_from = week + index

        till_today_infected = 0

        for (count_from; count_from >= index; count_from--) {
            till_today_infected += data_json[dates[count_from]]['Voivodeships'][x.id]['daily cured']

            cases.push(data_json[dates[count_from]]['Voivodeships'][x.id]['daily cured'])
        }

        mid = till_today_infected / week
        x.style.fill = color_picker(mid, sum)


    }

    let areasII = document.getElementsByClassName("scale-table")

    for (let xII of areasII) {
        xII.value = String(parseInt(xII.id * sum))
        xII.style.backgroundColor = color_picker(parseInt(xII.value), sum);
    }

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


function get_date_from_knob(data_json, index) {
    date = data_json[dates[index]]['date']
    document.getElementById("date-div").value = date;
}


paint_areas(map_data, 0)

function render_template() {
    let val = document.getElementById('voivodeship')
    let el = document.getElementById('statistics-link')
    el.href = '/statistics/' + val.innerHTML
    el.click()
}

document.getElementById('statistics-link').style.opacity=1