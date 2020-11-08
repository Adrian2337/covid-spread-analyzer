var ctx = document.getElementById('predictions-graph').getContext('2d');
console.log(total_cases, cured_cases, deaths)
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['date1', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
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
            yAxes: [{
                ticks: {
                    beginAtZero: false
                }
            }]
        }
    }
});
