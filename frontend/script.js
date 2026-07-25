const API_URL = "https://aetheris-ai-solutions.onrender.com/revenue";

async function fetchRevenueData() {
    const tableBody = document.getElementById("revenue-table-body");
    tableBody.innerHTML = `<tr><td colspan="3" style="text-align: center; color: #6b7280;">Loading analytics data... (Render cold start can take 30s)</td></tr>`;

    try {
        const response = await fetch(API_URL);
        const data = await response.json();

        if (data.success && data.analytics) {
            tableBody.innerHTML = ""; // Clear loading text
            
            data.analytics.forEach(item => {
                const row = document.createElement("tr");
                row.innerHTML = `
                    <td>${item.forecast_rev || 'N/A'}</td>
                    <td>${item.broker_split || 'N/A'}</td>
                    <td>${item.agent_split || 'N/A'}</td>
                `;
                tableBody.appendChild(row);
            });
        } else {
            tableBody.innerHTML = `<tr><td colspan="3" style="text-align: center; color: red;">Failed to load data structure.</td></tr>`;
        }
    } catch (error) {
        console.error("Error fetching revenue data:", error);
        tableBody.innerHTML = `<tr><td colspan="3" style="text-align: center; color: red;">Error connecting to backend server.</td></tr>`;
    }
}

// Run on page load
document.addEventListener("DOMContentLoaded", fetchRevenueData);
