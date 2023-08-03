const role = sessionStorage.getItem('role');
const token = sessionStorage.getItem('token');

const titleRole = {
    'a':'Airline',
    'm':'Manufacturer',
    'r':'Recycle Faclities'
}

function setTitle(){
    const head = document.getElementsByTagName('head')[0];

    let title = document.createElement('title');
    title.textContent = `${titleRole[role]}`;
    // console.log(titleRole.getItem('a'))
    // console.log("efrsf")
    head.appendChild(title);

    let doc = document.getElementById('role-profile')
    doc.innerText = `${titleRole[role]}`
}
setTitle()
let chartData = {};
let sum1 = 0;
let sum2 = 0;

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


function materialCompositionChart(d1, d2) {
    console.log(Object.keys(d1))
    const data1 = [12, 19, 3, 5, 2];
    const data2 = [5, 7, 15, 10, 8];
    let ke = ""
    if(Object.keys(d1).length>=Object.keys(d2).length){
        ke = Object.keys(d1)
    }
    else{
        ke = Object.keys(d2)
    }
    const ctx = document.getElementById('myChart-1').getContext('2d');
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ke,
        datasets: [
          {
            label: 'Repurpose',
            data: Object.values(d1),
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor: 'rgba(255, 99, 132, 1)',
            borderWidth: 1,
          },
          {
            label: 'Recycle',
            data: Object.values(d2),
            backgroundColor: 'rgba(54, 162, 235, 0.2)',
            borderColor: 'rgba(54, 162, 235, 1)',
            borderWidth: 1,
          },
        ],
      },
      options: {
        scales: {
          xAxes: [
            {
              stacked: true,
            },
          ],
          yAxes: [
            {
              stacked: true,
              ticks: {
                beginAtZero: true,
              },
            },
          ],
        },
      },
    });
  }
//   document.addEventListener('DOMContentLoaded', function() {
//     materialCompositionChart();
//   });
  

function recycleAnalysis(callback) {
  fetch('http://127.0.0.1:8000/vis/supervis', {
    method: 'GET',
    headers: {
      'Authorization': 'Bearer ' + token,
      'Content-Type': 'application/json'
    }
  })
  .then(response => response.json())
  .then(data => {
    chartData['repurposeMat'] = data.repurposeMat;
    chartData['recycleMat'] = data.recycleMat;
    sum1 = Object.values(data.recycleMat).reduce((a, b) => a + b, 0);
    sum2 = Object.values(data.repurposeMat).reduce((a, b) => a + b, 0);
    callback();
  })
  .catch(error => {
    console.error('Error:', error);
  });
}

recycleAnalysis(function() {
    console.log(sum1);
    console.log(sum2);
    recycleAnalysisChart(sum1, sum2)
    materialCompositionChart(chartData['repurposeMat'], chartData['recycleMat'])
});



async function healParts(option) {
    try {
      const response = await fetch(`http://127.0.0.1:8000/vis/${option}/`, {
        method: 'GET',
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json'
        },
      });
      const data = await response.json();
      if (response.status !== 200) {
        alert('Please relogin');
        window.location.href = 'index.html';
      }
      return data;
    } catch (error) {
      console.error(error);
    }
  }
  
  // Fetch recent customer data and populate the table
  async function populateTable(option) {
    const objectData = await healParts(option);
    let tableData = "";
    let i=1;

    objectData.map((values)=>{
        tableData+=`<tr>
        <th scope="row">${values.pid}</th>
        <td>${values.part_name}</td>
        <td>${values.manufacturer}</td>
        <td>${values.aircraft_mod}</td>
        <td>${values.age}</td>
        <td>${values.condi}</td>
        <td>${values.mat_comp}</td>
      </tr>`;
    })
    document.getElementById("fillTable").innerHTML=tableData;
  }
  
  // Call the function to populate the table on page load
  populateTable('recycle');

const button = document.getElementById('table-btn');
const heading = document.getElementById('table-header');

button.addEventListener('click', () => {
  if (button.textContent === 'Parts Best For Repurpose') {
    button.textContent = 'Parts Best For Recycle';
    heading.textContent = 'Parts Best For Repurpose';
    populateTable('repurpose');

  } else {
    button.textContent = 'Parts Best For Repurpose';
    heading.textContent = 'Parts Best For Recycle';
    populateTable('recycle');
    }
});

const goHomeBtn = document.getElementById('goHome');

goHomeBtn.addEventListener('click', () => {
  // Set sessionStorage 'token' to null
  sessionStorage.setItem('token', null);
  // Redirect to index.html
  window.location.href = 'index.html';
});
