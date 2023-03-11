document.addEventListener("DOMContentLoaded", function() {
    // Devices by type chart
    var devicesByTypeCtx = document.getElementById('devicesByTypeChart').getContext('2d');
    var devicesByTypeChart = new Chart(devicesByTypeCtx, {
        type: 'doughnut',
        data: {
            labels: ['Desktops', 'Laptops', 'Mobile devices'],
            datasets: [{
                data: [25, 35, 40],
                backgroundColor: [
                    '#007bff',
                    '#dc3545',
                    '#ffc107'
                ],
                borderColor: 'rgba(255, 255, 255, 1)',
                borderWidth: 2,
                hoverOffset: 10,
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
        }
    });


    // Devices by location chart
    var devicesByLocationCtx = document.getElementById('devicesByLocationChart').getContext('2d');
    var devicesByLocationChart = new Chart(devicesByLocationCtx, {
        type: 'bar',
        data: {
            labels: ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose'],
            datasets: [{
                label: 'Desktops',
                data: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
                backgroundColor: '#007bff'
            }, {
                label: 'Laptops',
                data: [20, 30, 40, 50, 60, 70, 80, 90, 100, 110],
                backgroundColor: '#dc3545'
            }, {
                label: 'Mobile devices',
                data: [30, 40, 50, 60, 70, 80, 90, 100, 110, 120],
                backgroundColor: '#ffc107'
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
        }
    });


    // Device trend chart
    var ctx = document.getElementById('deviceTrendChart').getContext('2d');
    var deviceTrendChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
            datasets: [{
                label: '# of Devices',
                data: [12, 19, 3, 5, 2, 3, 7, 10, 15, 12, 8, 5],
                backgroundColor: 'rgba(255, 99, 132, 1)',
                borderColor: 'rgba(255, 99, 132, 1)',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });


    // Device licence usage chart
    var ctx = document.getElementById('licenseUsageChart').getContext('2d');
    var licenseUsageChart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: ['Windows', 'MacOS', 'Linux'],
            datasets: [{
                data: [300, 200, 100],
                backgroundColor: [
                    '#007bff',
                    '#dc3545',
                    '#ffc107',
                ],
                borderColor: 'rgba(255, 255, 255, 1)',
                borderWidth: 2,
                hoverOffset: 10,
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'right'
                }
            }
        }
    });

});
