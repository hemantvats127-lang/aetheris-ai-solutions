JavaScript
// Render API Backend Endpoint
const BACKEND_URL = "http://localhost:5000";

async function fetchLeadsData() {
    const tableBody = document.getElementById("leadsTable");
    const pipelineValElement = document.getElementById("pipelineVal");
    const leadsCountElement = document.getElementById("leadsCount");

    if (tableBody) {
        tableBody.innerHTML = `<tr><td colspan="6" class="p-4 text-center text-slate-400">Syncing live pipeline...</td></tr>`;
    }

    try {
        const response = await fetch(`${BACKEND_URL}/api/admin/leads`);
        const data = await response.json();

        if (data && data.leads) {
            renderTable(data.leads);
            if (pipelineValElement) pipelineValElement.innerText = data.pipeline_value_usd || "$22,300,000";
            if (leadsCountElement) leadsCountElement.innerText = `${data.leads.length} Active`;
        }
    } catch (error) {
        console.warn("Backend warming up, using fallback data:", error);
        
        // Dynamic Fallback
        const fallbackLeads = [
            { id: 1, name: "Sheikh Mansoor", contact: "mansoor@dubailuxury.ae", budget: "$15,000,000", timeline: "30 Days", score: "HOT LEAD 🔥", assigned_agent: "VIP Desk (Dubai)", location: "UAE" },
            { id: 2, name: "Alexander Vance", contact: "+1 (305) 892-1102", budget: "$4,500,000", timeline: "Immediate", score: "WARM LEAD 🟡", assigned_agent: "Sarah Jenkins", location: "USA" },
            { id: 3, name: "Nguyen Minh", contact: "minh.nguyen@saigonprop.vn", budget: "$2,800,000", timeline: "60 Days", score: "HOT LEAD 🔥", assigned_agent: "Tran Le", location: "Vietnam" }
        ];
        
        renderTable(fallbackLeads);
        if (pipelineValElement) pipelineValElement.innerText = "$22,300,000";
        if (leadsCountElement) leadsCountElement.innerText = "3 Active";
    }
}

function renderTable(leads) {
    const tableBody = document.getElementById("leadsTable");
    if (!tableBody) return;

    tableBody.innerHTML = leads.map(lead => `
        <tr class="hover:bg-slate-800/40 transition-colors">
            <td class="p-3.5 font-semibold text-white">
                ${lead.name}
                <div class="text-xs text-slate-400 font-normal">${lead.contact}</div>
            </td>
            <td class="p-3.5 text-emerald-400 font-extrabold">${lead.budget}</td>
            <td class="p-3.5 text-slate-300">${lead.timeline}</td>
            <td class="p-3.5"><span class="px-2 py-0.5 rounded bg-slate-800 text-xs">${lead.location}</span></td>
            <td class="p-3.5 font-bold">${lead.score || lead.status}</td>
            <td class="p-3.5 text-slate-400">${lead.assigned_agent || lead.agent}</td>
        </tr>
    `).join("");
}

// Initial Auto Fetch on Page Load
document.addEventListener("DOMContentLoaded", fetchLeadsData);
