function recycleAnalysisChart(sum1, sum2){
    const ctx = document.getElementById('myChart');
            
    new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: ['Recycle', 'Repurpose'],
        datasets: [{
        label: '# of Votes',
        data: [sum1, sum2],
        borderWidth: 1
        }]
    },
    options: {
        scales: {
        y: {
            beginAtZero: true
        }
        }
    }
    });
}

recycleAnalysisChart(43, 34)
