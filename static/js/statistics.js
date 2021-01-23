function jsonify(variable) {
    return JSON.parse(variable.replaceAll(/&quot;/ig, '"').replaceAll('&#x27;', '"'));
}

var voi_data = jsonify(data_raw)
console.log(voi_data)
var draw_total_tests=true;
var draw_daily_tests=true;

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
var infected_delta=[]

var currDate_index=0
var dates=[]
var respirator_pie_data=[]
var week_respirator_pie_data=[]
var respirators_last_data=0
var tests_pie_data=[]
var tests_pie_last_data=0
var daily_pie_data=[]
var daily_pie_last_data=0

function getData() {

    dates=Object.keys(voi_data)
    currDate_index=dates.length-1

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
        deaths_100k_infected.push(voi_data[date]["deaths per 100k infected"])
        infected_delta.push(voi_data[date]["infected delta"])


        free_respirators.push(voi_data[date]["free respirators"])
        used_respirators.push(voi_data[date]["occupied respirators"])
    }
}
function draw_daily_Chart() {
    var ctx = document.getElementById('daily-chart').getContext('2d');
    var data_with_tests = {
            labels: dates,
            datasets: [{
                data: daily_infected,
                borderColor: "rgba(255, 0, 255, 1)",
                pointBackgroundColor: "rgba(255, 0, 255, 1)",
                pointBorderColor: "rgba(0, 0, 0, 1)",
                borderWidth: 3,
                label: "Infected",
                name: "Daily Infected"
            }
            ,{
                data: daily_tests,
                borderColor: "rgba(0, 0, 255, 1)",
                pointBackgroundColor: "rgba(0, 0, 255, 1)",
                pointBorderColor: "rgba(0, 0, 0, 1)",
                borderWidth: 3,
                label: "Tests",
                name: "Daily tests"
            }
            ,{
                data: daily_cured,
                borderColor: "rgba(255, 255, 0, 1)",
                pointBackgroundColor: "rgba(255, 255, 0, 1)",
                pointBorderColor: "rgba(0, 0, 0, 1)",
                borderWidth: 3,
                label: "Cured",
                name: "Daily Cured"
            },
                {

                data: daily_deceased,
                borderColor: "rgb(86,231,85)",
                pointBackgroundColor: "rgb(86,231,85)",
                pointBorderColor: "rgba(0, 0, 0, 1)",
                borderWidth: 3,
                label: "Deceased",
                name: "Daily Deceased"

            }
            ]
        };
    var data_without_tests = {
            labels: dates,
            datasets: [{
                data: daily_infected,
                borderColor: "rgba(255, 0, 255, 1)",
                pointBackgroundColor: "rgba(255, 0, 255, 1)",
                pointBorderColor: "rgba(0, 0, 0, 1)",
                borderWidth: 3,
                label: "Infected",
                name: "Daily Infected"
            }
            ,{
                data: daily_cured,
                borderColor: "rgba(255, 255, 0, 1)",
                pointBackgroundColor: "rgba(255, 255, 0, 1)",
                pointBorderColor: "rgba(0, 0, 0, 1)",
                borderWidth: 3,
                label: "Cured",
                name: "Daily Cured"
            },
                {

                data: daily_deceased,
                borderColor: "rgb(86,231,85)",
                pointBackgroundColor: "rgb(86,231,85)",
                pointBorderColor: "rgba(0, 0, 0, 1)",
                borderWidth: 3,
                label: "Deceased",
                name: "Daily Deceased"

            }
            ]
        };
    var data
    if(draw_daily_tests){
    data=data_with_tests;}else {
        data=data_without_tests
    }
    var myLineChart = new Chart(ctx, {
        type: 'line',
        data: data,
        options: {
            title: {
            display: true,
                fontColor: "white",
                fontSize: "18",
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
            },
            legend: {
            display: true,
            labels: {
                fontColor: 'white'
            }
        }}
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
                pointBackgroundColor: "rgba(255, 0, 255, 1)",
                pointBorderColor: "rgba(0, 0, 0, 1)",
                borderWidth: 3,
                label: "Infected",
                name: "Total Infected"
            }
            ,{
                data: total_cured,
                borderColor: "rgba(255, 255, 0, 1)",
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
                fontColor: "white",
                fontSize: "18",
            },
            legend: {
            display: true,
            labels: {
                fontColor: 'white'
            }
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
                borderColor: "rgb(246,177,255)",
                pointBackgroundColor: "rgb(246,177,255)",
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
                fontColor: "white",
                fontSize: "18",
            },
            legend: {
            display: true,
            labels: {
                fontColor: 'white'
            }
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
                fontColor: "white",
                fontSize: "18",
            },
            legend: {
            display: true,
            labels: {
                fontColor: 'white'
            }
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
                borderColor: "rgb(86,231,85)",
                pointBackgroundColor: "rgb(86,231,85)",
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
                fontColor: "white",
                fontSize: "18",
            },
            legend: {
            display: true,
            labels: {
                fontColor: 'white'
            }
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

function get_respirator_pie_Data() {
    var i=0
    for(i=free_respirators.length-1; i>0; i--){
        if(free_respirators[i]!=undefined && used_respirators[i]!=undefined){
            respirators_last_data=i;
            break;
        }
    }

    respirator_pie_data = {
        datasets: [{
            backgroundColor: ["rgb(246,177,255)", "rgb(108,106,214)","rgb(165,109,144)"],
            data: [free_respirators[i], used_respirators[i]]
        }],

        labels: [
            'Free',
            'Occupied',
        ]
    };
}
function draw_respirator_pieChart(){
    var ctx = document.getElementById('pie-chart').getContext('2d');
    var myDoughnutChart = new Chart(ctx, {
    type: 'doughnut',
    data: respirator_pie_data,

        options: {
        title:{
            display: true,
            text: 'Respirators ' + dates[respirators_last_data],
            fontColor: "white",
                fontSize: "18",
        },
            legend: {
            display: true,
            labels: {
                fontColor: 'white'
            }
        }
    }
    });
}

function get_week_respirator_pie_data(){
  var i=0
    for(i=free_respirators.length-1; i>0; i--){
        if(free_respirators[i]!=undefined && used_respirators[i]!=undefined){
            respirators_last_data=i;
            break;
        }
    }

    week_respirator_pie_data = {
        datasets: [{
            backgroundColor: ["rgb(255,251,47)", "rgb(138,255,73)","rgb(255,253,122)"],
            data: [respiratorWeekAvg(free_respirators), respiratorWeekAvg(used_respirators)]
        }],

        labels: [
            'Free',
            'Occupied',
        ]
    };
}
function respiratorWeekAvg(data){
    if(respirators_last_data<6){
        return data[respirators_last_data]
    } else{
        var sum=0;
        for(var i=respirators_last_data; i>respirators_last_data-6; i--){
            sum+=data[i];
        }
        return sum/7
    }
}
function draw_respirator_week_pie(){
 var ctx = document.getElementById('pie-week-chart').getContext('2d');
    var myDoughnutChart = new Chart(ctx, {
    type: 'doughnut',
    data: week_respirator_pie_data,

        options: {
        title:{
            display: true,
            text: 'Respirators week avg',
            fontColor: "white",
                fontSize: "18",
        },
            legend: {
            display: true,
            labels: {
                fontColor: 'white'
            }
        }
    }
    });
}

function get_tests_vs_infected_pie_Data(){
    var i=0;
    for(i=daily_tests.length-1; i>0; i--){
        if(daily_tests[i]!=undefined && daily_infected[i]!=undefined){
            tests_pie_last_data=i;
            break
        }
    }
    let negative=daily_tests[tests_pie_last_data]-daily_infected[tests_pie_last_data]
    tests_pie_data = {
        datasets: [{
            backgroundColor: ["rgb(149,41,62)","rgb(49,214,155)"],
            data: [daily_infected[tests_pie_last_data], negative]
        }],

        labels: [
            'Positive',
            'Negative',
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
            text: 'Tests '+dates[tests_pie_last_data],
            fontColor: "white",
                fontSize: "18",
        },
            legend: {
            display: true,
            labels: {
                fontColor: 'white'
            }
        }
    }
    });
}

function get_dailypieData(){
    var i=0;
    for(i=daily_cured.length-1; i>0; i--){
        if(daily_infected[i]!=undefined && daily_cured[i]!=undefined){
            daily_pie_last_data=i;
            break;
        }
    }

    daily_pie_data = {
        datasets: [{
            backgroundColor: ["rgb(244,113,101)", "rgb(22,208,220)",],
            data: [daily_infected[daily_pie_last_data], daily_cured[daily_pie_last_data]]
        }],

        labels: [
            'Infected',
            'Cured',
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
            text: 'Infected vs Cured '+dates[daily_pie_last_data],
            fontColor: "white",
                fontSize: "18",
        },
            legend: {
            display: true,
            labels: {
                fontColor: 'white'
            }
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
                fontColor: "white",
                fontSize: "18",
            text: 'Total infected per 100.000 citizens',
            },
            legend: {
            display: true,
            labels: {
                fontColor: 'white'
            }
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
                pointBackgroundColor: "rgba(0, 0, 255, 1)",
                pointBorderColor: "rgba(0, 0, 0, 1)",
                borderWidth: 3,
                label: "Infected/100k daily",
                name: "Infected/100k daily"
            } ,
                {
                data: weekavg_infected_100k,
                borderColor: "rgba(255, 0, 0, 1)",
                pointBackgroundColor: "rgba(255, 0, 0, 1)",
                pointBorderColor: "rgba(0, 0, 0, 1)",
                borderWidth: 3,
                label: "Infected/100k week avg",
                name: "Infected/100k week avg"
            }]
        },

        options: {
            title: {
            display: true,
            text: 'Infected per 100.000 citizens',
                fontColor: "white",
                fontSize: "18",
            },
            legend: {
            display: true,
            labels: {
                fontColor: 'white'
            }
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

function populateRow(row, data){
    for(var i=1; i<8; i++){
       var cell=row.insertCell(i);
       if(data[currDate_index+1-i]!=undefined){
        cell.innerHTML=data[currDate_index+1-i].toString().slice(0,8)}else{
           cell.innerHTML="-"
       }
    }
}
function populateTable(){
    var table = document.getElementById("data-table");
    var row = table.insertRow(0);
    var cell = row.insertCell(0);
    cell.innerHTML=" "
    for(var i=1; i<8; i++){
        cell=row.insertCell(i);
        cell.innerHTML=dates[currDate_index+1-i]
    }
    row = table.insertRow(1);
    cell = row.insertCell(0);
    cell.innerHTML="Daily infected"
    populateRow(row, daily_infected)
    row = table.insertRow(2)
    cell = row.insertCell(0)
    cell.innerHTML="Daily deceased"
    populateRow(row, daily_deceased)
    row = table.insertRow(3)
    cell = row.insertCell(0)
    cell.innerHTML="Infected delta"
    populateRow(row, infected_delta)
    row = table.insertRow(4)
    cell = row.insertCell(0)
    cell.innerHTML="Deaths/100k infected"
    populateRow(row, deaths_100k_infected)
    row = table.insertRow(5)
    cell = row.insertCell(0)
    cell.innerHTML="Infections/100k"
    populateRow(row, daily_infected_100k)
    row = table.insertRow(6)
    cell = row.insertCell(0)
    cell.innerHTML="Infections/100k week avg"
    populateRow(row, weekavg_infected_100k)




}


function initiate(){
   document.title="Statistics";
    getData()
    populateTable()
    if(total_tests[0]==undefined){
        draw_total_tests=false;
    }
    if(daily_tests[0]==undefined){
        draw_daily_tests=false;
    }
    get_respirator_pie_Data()
    get_tests_vs_infected_pie_Data()
    get_week_respirator_pie_data()
    get_dailypieData()
    draw_daily_Chart()
    draw_total_Chart()
    draw_total_diseased_Chart()
    draw_daily_diseased_Chart()
    if (draw_total_tests){
    draw_total_tests_Chart()
    } else {
        document.getElementById('total-tests-chart').style.display = 'none';
    }
    drawInfected100k()
    drawInfected100ktoday()
    draw_respirator_pieChart()
    draw_respirator_week_pie()
    if(tests_pie_last_data!=0){
draw_testpieChart()} else {
        document.getElementById('pie-tests-canvas').style.display = 'none'
    }
    if(daily_cured[daily_pie_last_data]!=0){
    draw_dailypie()}else {
        document.getElementById("pie-daily-canvas").style.display = 'none'
    }
}


initiate()

/* side menu */
function openNav() {
  document.getElementById("side-menu").style.width = "22%";
}

function closeNav() {
  document.getElementById("side-menu").style.width = "0";
}