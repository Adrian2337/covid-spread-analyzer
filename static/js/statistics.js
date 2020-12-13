function jsonify(variable) {
    return JSON.parse(variable.replaceAll(/&quot;/ig, '"').replaceAll('&#x27;', '"'));
}

var voi_data = jsonify(data_raw)
console.log(voi_data)
var daily_infected=[]
var daily_deceased=[]
var daily_cured=[]
var daily_tests=[]

var total_cured=[]
var total_infected=[]
var total_deceased=[]
var total_tests=[]

var total_infected_100k=[]
var daily_infected_100k=[]
var weekavg_infected_100k=[]

var deaths_100k_infected=[]
var free_respirators=[]
var used_respirators=[]
var infected_now=[]

var dates=[]
var pie_chart_data=[]
var tests_pie_data=[]
var daily_pie_data=[]

function getData() {

    dates=Object.keys(voi_data)

    for (var date in voi_data) {
        daily_deceased.push(voi_data[date]["daily deceased"])
        daily_infected.push(voi_data[date]["daily infected"])
        daily_cured.push(voi_data[date]["daily cured"])
        daily_tests.push(voi_data[date]["daily tests"])

        total_deceased.push(voi_data[date]["total deceased"])
        total_infected.push(voi_data[date]["total infected"])
        total_cured.push(voi_data[date]["total cured"])
        total_tests.push(voi_data[date]["total tests"])

        total_infected_100k.push(voi_data[date]["total infected per 100k"])
        daily_infected_100k.push(voi_data[date]["infections per 100k"])
        weekavg_infected_100k.push(voi_data[date]["infections per 100k week avg"])

        free_respirators.push(voi_data[date]["free respirators"])
        used_respirators.push(voi_data[date]["occupied respirators"])
    }
}

function draw_daily_Chart() {
    var ctx = document.getElementById('daily-chart').getContext('2d');
    var myLineChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: dates,
            datasets: [{
                data: daily_infected,
                borderColor: "rgba(255, 0, 255, 1)",
               // backgroundColor: "rgba(255, 0, 255, 1)",
                pointBackgroundColor: "rgba(255, 0, 255, 1)",
                pointBorderColor: "rgba(0, 0, 0, 1)",
                borderWidth: 3,
                label: "Infected",
                name: "Daily Infected"
            }
            ,{
                data: daily_tests,
                borderColor: "rgba(0, 0, 255, 1)",
              //  backgroundColor: "rgba(0, 0, 255, 1)",
                pointBackgroundColor: "rgba(0, 0, 255, 1)",
                pointBorderColor: "rgba(0, 0, 0, 1)",
                borderWidth: 3,
                label: "Tests",
                name: "Daily tests"
            }
            ,{
                data: daily_cured,
                borderColor: "rgba(255, 255, 0, 1)",
                //backgroundColor: "rgba(255, 255, 0, 1)",
                pointBackgroundColor: "rgba(255, 255, 0, 1)",
                pointBorderColor: "rgba(0, 0, 0, 1)",
                borderWidth: 3,
                label: "Cured",
                name: "Daily Cured"
            }
            ]
        },
        options: {
            title: {
            display: true,
            text: 'Daily',
            },
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
function draw_total_Chart() {
    var ctx = document.getElementById('total-chart').getContext('2d');
    var myLineChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: dates,
            datasets: [{
                data: total_infected,
                borderColor: "rgba(255, 0, 255, 1)",
               // backgroundColor: "rgba(255, 0, 255, 1)",
                pointBackgroundColor: "rgba(255, 0, 255, 1)",
                pointBorderColor: "rgba(0, 0, 0, 1)",
                borderWidth: 3,
                label: "Infected",
                name: "Total Infected"
            }
            ,{
                data: total_cured,
                borderColor: "rgba(255, 255, 0, 1)",
                //backgroundColor: "rgba(255, 255, 0, 1)",
                pointBackgroundColor: "rgba(255, 255, 0, 1)",
                pointBorderColor: "rgba(0, 0, 0, 1)",
                borderWidth: 3,
                label: "Cured",
                name: "Total Cured"
            }
            ]
        },
        options: {
            title: {
            display: true,
            text: 'Total',
            },
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
function draw_total_tests_Chart(){

    var ctx = document.getElementById('total-tests-chart').getContext('2d');
    var myLineChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: dates,
            datasets: [{
                data: total_tests,
                borderColor: "rgba(0, 0, 255, 1)",
              //  backgroundColor: "rgba(0, 0, 255, 1)",
                pointBackgroundColor: "rgba(0, 0, 255, 1)",
                pointBorderColor: "rgba(0, 0, 0, 1)",
                borderWidth: 3,
                label: "Tests",
                name: "Total tests"
            }]
        },
        options: {
            title: {
            display: true,
            text: 'Total tests',
            },
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

function draw_total_diseased_Chart(){
    var ctx = document.getElementById('totald-chart').getContext('2d');
    var myLineChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: dates,
            datasets: [{

                data: total_deceased,
                borderColor: "rgba(0, 125, 255, 1)",
                backgroundColor: "rgba(0, 125, 255, 1)",
                pointBackgroundColor: "rgba(0, 125, 255, 1)",
                pointBorderColor: "rgba(0, 0, 0, 1)",
                borderWidth: 3,
                label: "Deceased",
                name: "Total Deceased"

            }]
        },
        options: {
            title: {
            display: true,
            text: 'Total',
            },
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
function draw_daily_diseased_Chart(){
    var ctx = document.getElementById('dailyd-chart').getContext('2d');
    var myLineChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: dates,
            datasets: [{

                data: daily_deceased,
                borderColor: "rgba(0, 255, 0, 1)",
               // backgroundColor: "rgba(0, 255, 0, 1)",
                pointBackgroundColor: "rgba(0, 255, 0, 1)",
                pointBorderColor: "rgba(0, 0, 0, 1)",
                borderWidth: 3,
                label: "Deceased",
                name: "Daily Deceased"

            }
            ]
        },
        options: {
            title: {
            display: true,
            text: 'Daily',
            },
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

function get_piechart_Data() {
    pie_chart_data = {
        datasets: [{
            backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f"],
            data: [free_respirators[5], used_respirators[5]]
        }],

        labels: [
            'Free',
            'Occupied',
        ]
    };
}
function draw_pieChart(){
    var ctx = document.getElementById('pie-chart').getContext('2d');
    var myDoughnutChart = new Chart(ctx, {
    type: 'doughnut',
    data: pie_chart_data,

        options: {
        title:{
            display: true,
            text: 'Data for '+dates[5],
        }
    }
    });
}

function get_testspieData(){
    let negative=daily_tests[5]-daily_infected[5]
    tests_pie_data = {
        datasets: [{
            backgroundColor: ["rgba(255,255,0)","rgba(140, 100,255)"],
            data: [daily_infected[5], negative]
        }],

        labels: [
            'positive',
            'negative',
        ]
    };
}
function draw_testpieChart(){
   var ctx = document.getElementById('pie-tests-chart').getContext('2d');
    var myDoughnutChart = new Chart(ctx, {
    type: 'doughnut',
    data: tests_pie_data,

        options: {
        title:{
            display: true,
            text: 'Data for '+dates[5],
        }
    }
    });
}

function get_dailypieData(){
    daily_pie_data = {
        datasets: [{
            backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f"],
            data: [daily_infected[5], daily_cured[5], daily_deceased[5]]
        }],

        labels: [
            'Infected',
            'Cured',
            'Deceased',
        ]
    };
}
function draw_dailypie(){
    var ctx = document.getElementById('pie-daily-chart').getContext('2d');
    var myDoughnutChart = new Chart(ctx, {
    type: 'doughnut',
    data: daily_pie_data,

        options: {
        title:{
            display: true,
            text: 'Data for '+dates[5],
        }
    }
    });
}

function drawInfected100k(){
    var ctx = document.getElementById('infected100k-graph').getContext('2d');
    var myLineChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: dates,
            datasets: [{

                data: total_infected_100k,
                borderColor: "rgba(0, 255, 0, 1)",
               // backgroundColor: "rgba(0, 255, 0, 1)",
                pointBackgroundColor: "rgba(0, 255, 0, 1)",
                pointBorderColor: "rgba(0, 0, 0, 1)",
                borderWidth: 3,
                label: "Infected/100k",
                name: "Total Deceased"

            },               ]
        },
        options: {
            title: {
            display: true,
            text: 'Total infected per 100.000 citizens',
            },
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
function drawInfected100ktoday(){
    var ctx = document.getElementById('infected100ktoday-graph').getContext('2d');
    var myLineChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: dates,
            datasets: [{
                data: daily_infected_100k,
                borderColor: "rgba(0, 0, 255, 1)",
              //  backgroundColor: "rgba(0, 0, 255, 1)",
                pointBackgroundColor: "rgba(0, 0, 255, 1)",
                pointBorderColor: "rgba(0, 0, 0, 1)",
                borderWidth: 3,
                label: "Infected/100k daily",
                name: "Infected/100k daily"
            }            ]
        },
        options: {
            title: {
            display: true,
            text: 'Daily infected per 100.000 citizens',
            },
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

//TODO ogarnąć w zależności od danych
function initiate(){
    getData()
get_piechart_Data()
get_testspieData()
get_dailypieData()
draw_daily_Chart()
draw_total_Chart()
draw_total_diseased_Chart()
draw_daily_diseased_Chart()
draw_total_tests_Chart()
draw_pieChart()
draw_testpieChart()
draw_dailypie()
drawInfected100k()
drawInfected100ktoday()
}

initiate()

