// Graph will be stored in this variable

let chart;

// Start graph. This function ensures the graph is plotted when
//the script runs. That is before the user starts typing for values.

document.getElementById("value-a").addEventListener('input', function () {
    showRootsAndGraph();
});

document.getElementById("value-b").addEventListener('input', function () {
    showRootsAndGraph();
});

document.getElementById("value-c").addEventListener('input', function () {
    showRootsAndGraph();
});


function showRootsAndGraph() {
    // This function starts by finding the roots of the graph.
    // Formular: Solve Quadratic: x = (-b ± √(b² - 4ac)) / 2a
    // The values of a, b, c are typed by the user on the screen
    
    let a = Number(document.getElementById("value-a").value.trim());
    let b = Number(document.getElementById("value-b").value.trim());
    let c = Number(document.getElementById("value-c").value.trim());
    
    let discrim; // Stores the discriminant
    let root1; // Stores the first root
    let root2; // Stores the second root
    let realpart; // Real part of the roots
    let imagpart; // Imaginary part
    let root1text; // Store first root in user readable format
    let root2text; // Store the second root in user readable format
    
    discrim = Math.pow(b, 2) - 4 * a * c; // Calculates the discriminant
    
    if (discrim === 0) {
        root1 = -b / (2 * a);
        root2 = root1;
        root1text = `Roots (x1 = x2) = ${root1.toFixed(4)}`;
        root2text = "Roots are real and the same.";
        
    } else if (discrim > 0) {
        root1 = (-b + Math.sqrt(discrim)) / (2 * a);
        root2 = (-b - Math.sqrt(discrim)) / (2 * a);
        root1text = `Roots 1 (x1) = ${root1.toFixed(4)}`;
        root2text = `Roots 2 (x2) = ${root2.toFixed(4)}`;
        
    } else {
        realpart = -b / (2 * a);
        imagpart = Math.sqrt(-discrim / (2 * a));
        root1text = `Roots 1 (x1): ${realpart.toFixed(2)} + ${imagpart.toFixed(2)}i`;
        root2text = `Roots 2 (x2): ${realpart.toFixed(2)} - ${imagpart.toFixed(2)}i`;
        
    }
    
    // X values 
    
    let xValues = [-4, -3, -2, -1, 0, 1, 2, 3, 4];
    
    // Generate Y values based on the values X 
    
    let yValues = [];
    
    for (let x of xValues) {
        let y;
        y = a * Math.pow(x,2) + b * x + c;
        yValues.push(y);
    }
    
    // Draw chart 
    
  if (chart) {chart.destroy();}
  
  chart = new Chart("myChart", {
     type: "line",
     data: {
        labels: xValues,
        datasets: [{
        label: "Quadratic Graph: y = ax² + bx + c", // Label for the dataset
        fill: false, // Do not fill under the line
        lineTension: 0.1, // Smoothing of line. 0 for straight lines
        backgroundColor: "rgba(0,0,255,1.0)",
        borderColor: "rgba(0,0,255,0.1)", // Line color
        data: yValues
      }]
    },
  
    options: {
       responsive: true, // Make chart responsive
       legend: {display: false},
       title: {
          display: true,
          text: "Quadratic Equation Graph"
       }
     }
   });
   
   // Write the values to be plotted
   
   document.getElementById("xvalues").textContent = `x: ${xValues.join(", ")}`;
   document.getElementById("yvalues").textContent = `y: ${yValues.join(", ")}`;
   
   // Write The Roots as output so that the user can see the roots
   
   document.getElementById("roots1").textContent = root1text;
   document.getElementById("roots2").textContent = root2text;
   
}
