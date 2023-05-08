var ctx = document.getElementById('gender').getContext('2d');
var gender = new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels: ['Female', 'Male'],
      options: {
        plugins: {
            title: {
                display: true,
                text: 'Custom Chart Title'
            }
        }
    },
      datasets: [{
        label: 'Percentage',
        data: [34.2, 65.8],
        backgroundColor: [
          'rgb(255, 99, 132)',
          'rgb(54, 162, 235)',
          'rgb(255, 205, 86)'
        ],
        hoverOffset: 4
      }]
    },

  });

var ctx = document.getElementById('cys').getContext('2d');
var cys = new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels: ['2019', '2020'],
      options: {
        plugins: {
            title: {
                display: true,
                text: 'Custom Chart Title'
            }
        }
    },
      datasets: [{
        label: 'Percentage',
        data: [57.5, 42.5],
        backgroundColor: [
          'rgb(255, 99, 132)',
          'rgb(54, 162, 235)',
          'rgb(255, 205, 86)'
        ],
        hoverOffset: 4
      }]
    },

  });

  var ctx = document.getElementById('course').getContext('2d');
var course = new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels: ['BSIT', 'BSCS'],
      options: {
        plugins: {
            title: {
                display: true,
                text: 'Custom Chart Title'
            }
        }
    },
      datasets: [{
        label: 'Percentage',
        data: [63.2, 36.8],
        backgroundColor: [
          'rgb(255, 99, 132)',
          'rgb(54, 162, 235)',
          'rgb(255, 205, 86)'
        ],
        hoverOffset: 4
      }]
    },

  });

