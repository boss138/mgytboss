// Simulated real-time data (replace this with your actual data source)
let currentFlowRate = 0;
let malfunction = false;

// Function to update the status display
function updateStatus() {
    document.getElementById('flow-rate').textContent = currentFlowRate + ' GPM';
    document.getElementById('malfunction').textContent = malfunction ? 'Yes' : 'No';
}

// Function to fetch real-time data (you should replace this with actual data retrieval)
function fetchData() {
    // Simulated data update
    currentFlowRate = Math.floor(Math.random() * 10) + 1; // Random flow rate between 1 and 10 GPM
    malfunction = Math.random() < 0.1; // 10% chance of malfunction

    updateStatus();
}

// Initial status update
updateStatus();

// Add event listener to refresh button
document.getElementById('refresh-button').addEventListener('click', () => {
    fetchData(); // Refresh the data when the button is clicked
});

// Set up periodic data updates (e.g., every 5 seconds)
setInterval(fetchData, 5000); // 5000 milliseconds = 5 seconds
