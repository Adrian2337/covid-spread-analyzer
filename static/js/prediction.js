function color_picker(value, sum) {
    console.log(value)

    let lim1 = 0.25 * sum
    let lim2 = 0.35 * sum
    let lim3 = 0.50 * sum
    let lim4 = 0.7 * sum

    if (value < lim1 && value > 0)
        return "green"
    else if (lim2 > value)
        return "yellow"
    else if (lim3 > value)
        return "orange"
    else if (lim4 > value)
        return "red"
    else
        return "darkred"
}


function paint_areas(data) {
    let areas = document.getElementsByClassName("area")
    console.log(data)
    sum = 100_000
    for (let x of areas) {
        console.log(data[x.id], x.id);
        // below sum all predicted cases as input value
        x.style.fill = color_picker(data[x.id].reduce((a, b) => a + b, 0), sum);

    }
}


function draw_chart(dates, total_cases, cured_cases, deaths) {
    var ctx = document.getElementById('predictions-graph').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: dates,
            datasets: [{
                data: total_cases,
                backgroundColor: "rgba(202, 201, 197, 0.5)",
                borderColor: "rgba(202, 201, 197, 1)",
                pointBackgroundColor: "rgba(202, 201, 197, 1)",
                pointBorderColor: "#fff",
                borderWidth: 1,
                label: "Total Cases",
                name: "Total Cases"

            }, {
                data: cured_cases,
                backgroundColor: "rgba(171, 9, 0, 0.5)",
                borderColor: "rgba(171, 9, 0, 1)",
                pointBackgroundColor: "rgba(171, 9, 0, 1)",
                pointBorderColor: "#fff",
                borderWidth: 1,
                label: "Cured Cases",
                name: "Cured Cases"

            }, {
                data: deaths,
                backgroundColor: "rgba(166, 78, 46, 0.5)",
                borderColor: "rgba(12, 74, 0, 1)",
                pointBackgroundColor: "rgba(123, 76, 0, 1)",
                pointBorderColor: "#fff",
                borderWidth: 1,
                label: "Deaths",
                name: "Deaths"

            }]
        },
        options: {
            scales: {
                xAxes: [{
                    ticks: {
                        autoSkip: false,
                        maxRotation: 90,
                        minRotation: 90
                    }
                }]
            }
        }
    });
}

function jsonify(variable) {
    return JSON.parse(variable.replaceAll(/&quot;/ig, '"').replaceAll('&#x27;', '"'));

}

function clearCanvas(context, canvas) {
    context.clearRect(0, 0, canvas.width, canvas.height);
    var w = canvas.width;
    canvas.width = 1;
    canvas.width = w;
}

var myChart = null;

function draw_chart_onclick(element) {
    var ctx = document.getElementById('predictions-graph').getContext('2d');
    let voi = element.getAttribute("xlink:title")
    var data_array = graph_data[voi]
    var pred_arr = predicted_values[voi]
    if (myChart !== null)
        myChart.destroy()
    myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: dates,
            datasets: [{
                data: pred_arr,
                borderColor: "white",
                backgroundColor: "rgba(86, 215, 152, 0.5)",
                pointBackgroundColor: "rgba(202, 201, 197, 0.5)",
                pointBorderColor: "#fff",
                borderWidth: 1,
                label: "Predictions",
                name: "Total Predicted Cases"

            }, {
                data: data_array,
                backgroundColor: "rgba(243, 139, 74, 0.6)",
                borderColor: "rgba(202, 201, 197, 0.6)",
                pointBackgroundColor: "rgba(202, 201, 197, 0.7)",
                pointBorderColor: "#fff",
                borderWidth: 1,
                label: "Real Cases",
                name: "Total Cases"

            }]
        },
        options: {
            scales: {
                xAxes: [{
                    ticks: {
                        autoSkip: false,
                        maxRotation: 90,
                        minRotation: 90
                    }
                }]
            }
        }
    })
    ;
}

function get_max_case(data) {
    let max = 0
    for (let x in data) {
        let val = data[x][data[x].length - 1]
        if (max < val) {
            max = val
        }
    }
    return max
}

function fill_date() {
    let el = document.getElementById('date-div')
    el.innerHTML = 'Prediction for ' + dates[dates.length - 1]
    el.style.color = 'white'
    el.style.fontSize = '28px'
}

var predicted_values = jsonify(predicted_values_raw)
var graph_data = jsonify(graph_data_raw)
var dates = jsonify(dates_raw)

pred_max = get_max_case(predicted_values)

draw_chart_onclick(document.getElementById("Mazowieckie-a"))
paint_areas(predicted_values)

fill_date()