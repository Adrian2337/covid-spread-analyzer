function jsonify(variable) {
    return JSON.parse(variable.replaceAll(/&quot;/ig, '"').replaceAll('&#x27;', '"'));
}

var voi_dataa = jsonify(data_raw)
//console.log(voi_dataa)
var infected_arr=[]
var deceased_arr=[]
var dates=[]

function getData() {
    for (var date in voi_dataa) {
        infected_arr.push(voi_dataa[date]["daily infected"])
    }

    for (var date in voi_dataa) {
        deceased_arr.push(voi_dataa[date]["daily deceased"])
    }
    dates=Object.keys(voi_dataa)
}

function draw_chart() {
    var ctx = document.getElementById('cases-graph').getContext('2d');
    var myLineChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: dates,
            datasets: [{

                data: deceased_arr,
                borderColor: "white",
                backgroundColor: "rgba(0, 255, 0, 1)",
                pointBackgroundColor: "rgba(255, 255, 255, 1)",
                pointBorderColor: "rgba(0, 0, 0, 1)",
                borderWidth: 1,
                label: "Deceased",
                name: "Daily Deceased"

            },{
                data: infected_arr,
                borderColor: "white",
                backgroundColor: "rgba(255, 0, 255, 1)",
                pointBackgroundColor: "rgba(255, 255, 255, 1)",
                pointBorderColor: "rgba(0, 0, 0, 1)",
                borderWidth: 1,
                label: "Infected",
                name: "Daily Infected"
            }
            ]
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

getData()
draw_chart()
