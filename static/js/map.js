function color_picker(value) {
    if (value <15)
        return "yellow"
    else if (150 > value > 15)
        return "green"
    else if (500 > value > 150)
        return "orange"
    else
        return "red"
}

function paint_areas(data) {
    let areas = document.getElementsByClassName("area")
    for (let x of areas) {
        x.style.fill = color_picker(data['d1'][x.id])
    }
}

var data_p = JSON.parse(data_t.replaceAll(/&quot;/ig, '"'));
paint_areas(data_p)
