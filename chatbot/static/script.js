document.addEventListener('DOMContentLoaded', function () {
    // Dummy data for code complexity and code duplication
    var codeComplexityData = {
        labels: ['Function A', 'Function B', 'Function C', 'Function D'],
        datasets: [{
            label: 'Code Complexity',
            data: [8, 5, 10, 7],
            backgroundColor: 'rgba(54, 162, 235, 0.5)',
            borderColor: 'rgba(54, 162, 235, 1)',
            borderWidth: 1
        }]
    };

    var codeDuplicationData = {
        labels: ['File 1', 'File 2', 'File 3', 'File 4'],
        datasets: [{
            label: 'Code Duplication',
            data: [3, 2, 4, 1],
            backgroundColor: 'rgba(255, 99, 132, 0.5)',
            borderColor: 'rgba(255, 99, 132, 1)',
            borderWidth: 1
        }]
    };

    // Dummy data for issues and improvements
    var issues = ['Syntax error', 'Performance issue', 'Security vulnerability'];
    var improvements = ['Refactor function A', 'Optimize database query'];

    // Create charts
    createChart('codeComplexityChart', 'Code Complexity', codeComplexityData);
    createChart('codeDuplicationChart', 'Code Duplication', codeDuplicationData);

    // Display issues and improvements
    displayList('issuesList', 'Issues with code', issues);
    displayList('improvementsList', 'Potential improvements', improvements);
});

function createChart(canvasId, label, data) {
    var ctx = document.getElementById(canvasId).getContext('2d');
    new Chart(ctx, {
        type: 'bar',
        data: data,
        options: {
            plugins: {
                title: {
                    display: true,
                    text: label
                }
            }
        }
    });
}

function displayList(containerId, title, items) {
    var container = document.getElementById(containerId);
    container.innerHTML = '<h2>' + title + '</h2>';
    var ul = document.createElement('ul');
    items.forEach(function (item) {
        var li = document.createElement('li');
        li.textContent = item;
        ul.appendChild(li);
    });
    container.appendChild(ul);
}
