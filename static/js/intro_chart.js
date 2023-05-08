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
        data: [39, 85],
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
      labels: ['2018', '2020'],
      options: {
        plugins: {
            title: {
                display: true,
                text: 'Custom Chart Title'
            }
        }
    },
      datasets: [{
        data: [88, 36],
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
      labels: ['BSIT'],
      options: {
        plugins: {
            title: {
                display: true,
                text: 'Custom Chart Title'
            }
        }
    },
      datasets: [{
        data: [124],
        backgroundColor: [
          'rgb(54, 162, 235)',
        ],
        hoverOffset: 4
      }]
    },

  });

var ctx = document.getElementById('ss').getContext('2d');
var ss = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['Low (₱9,520-₱19,040)', 'Lower Middle (₱19,040-₱38,080)', 'Middle (₱38,080-₱66,640)', 'Upper Middle (₱66,640-₱114,240'],
        datasets: [{
            label: false,
            data: [61, 34, 26, 3],
            backgroundColor: [
            'rgb(255, 99, 132)',
            'rgb(54, 162, 235)',
            'rgb(255, 205, 86)',
            'rgb(15, 245, 145)'
          ],
          hoverOffset: 4
        }]
      },

      options: {
        plugins: {
            legend: {
                display: false
            }
        }
    }
  
    });

    var ctx = document.getElementById('working-scholar-hal').getContext('2d');
    var ss = new Chart(ctx, {
          type: 'bar',
          data: {
            labels: ['Working Students', 'Scholars', 'Has a laptop'],
            datasets: [{
                label: ['Yes'],
                data: [26, 19, 91],
                backgroundColor: [
                'rgb(255, 99, 132)',
                'rgb(54, 162, 235)',
                'rgb(255, 205, 86)',
                'rgb(15, 245, 145)'
              ],
              hoverOffset: 4
            },{
              label: ['No'],
              data: [98, 105, 33],
              backgroundColor: [
              'rgb(255, 99, 132)',
              'rgb(54, 162, 235)',
              'rgb(255, 205, 86)',
              'rgb(15, 245, 145)'
            ],
            hoverOffset: 4
          }]
          },
           
          options: {
            plugins: {
                legend: {
                    display: false
                }
            }
        }
    
        });



