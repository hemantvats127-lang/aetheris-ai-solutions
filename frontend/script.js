const BASE_URL = 'https://aetheris-ai-solutions.onrender.com/api';

async function fetchLeadsData() {
  const tableBody = document.getElementById('leadTable');
  tableBody.innerHTML = `<tr><td colspan="6" class="p-4 text-center text-slate-500">Connecting to Aetheris AI Engine...</td></tr>`;

  try {
    const response = await fetch(`${BASE_URL}/leads`);
    const data = await response.json();

    if (data.success && data.leads) {
      document.getElementById('stat-pipeline').innerText = `$${data.total_pipeline.toLocaleString()}`;
      document.getElementById('stat-leads-count').innerText = `${data.leads.length} Active`;

      tableBody.innerHTML = data.leads.map(lead => `
        <tr class="hover:bg-slate-900/80">
          <td class="p-3.5 font-medium text-slate-100">${lead.name}<br><span class="text-xs text-slate-500">${lead.email}</span></td>
          <td class="p-3.5 font-bold text-emerald-400">${lead.budget}</td>
          <td class="p-3.5 text-slate-300">${lead.timeline}</td>
          <td class="p-3.5"><span class="bg-slate-800 text-slate-300 text-xs px-2 py-0.5 rounded border border-slate-700">${lead.region}</span></td>
          <td class="p-3.5 font-bold text-xs">${lead.score}</td>
          <td class="p-3.5 text-xs text-slate-400">${lead.desk}</td>
        </tr>
      `).join('');
    }
  } catch (err) {
    tableBody.innerHTML = `<tr><td colspan="6" class="p-4 text-center text-red-400">Failed to sync live data.</td></tr>`;
  }
}

async function fetchSafetyData() {
  try {
    const response = await fetch(`${BASE_URL}/safety`);
    const data = await response.json();

    if (data.success && data.agents) {
      const sosStat = document.getElementById('stat-sos-status');
      if (data.active_alerts > 0) {
        sosStat.innerText = `${data.active_alerts} EMERGENCY ALERT!`;
        sosStat.className = "text-3xl font-extrabold text-red-500 animate-bounce mt-2";
      } else {
        sosStat.innerText = "All Safe ✅";
        sosStat.className = "text-3xl font-extrabold text-sky-400 mt-2";
      }

      const grid = document.getElementById('safetyGrid');
      grid.innerHTML = data.agents.map(agent => `
        <div class="p-4 rounded-lg bg-slate-950 border ${agent.sos_alert ? 'border-red-500 bg-red-950/20' : 'border-slate-800'}">
          <div class="flex justify-between items-start">
            <h4 class="font-bold text-slate-200">${agent.agent}</h4>
            <span class="text-[10px] px-2 py-0.5 rounded ${agent.sos_alert ? 'bg-red-500 text-white font-bold' : 'bg-slate-800 text-slate-400'}">${agent.battery} Battery</span>
          </div>
          <p class="text-xs text-slate-400 mt-1">📍 ${agent.location}</p>
          <div class="mt-3 flex justify-between items-center text-xs">
            <span class="font-medium ${agent.sos_alert ? 'text-red-400 animate-pulse font-bold' : 'text-emerald-400'}">${agent.status}</span>
          </div>
        </div>
      `).join('');
    }
  } catch (err) {
    console.error("Safety Engine fetch error:", err);
  }
}

async function triggerEmergencySOS() {
  try {
    const res = await fetch(`${BASE_URL}/safety/sos`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ agent_id: 101 })
    });
    const data = await res.json();
    if (data.success) {
      alert("🚨 EMERGENCY SOS SIGNAL SENT TO FIELD TEAM & POLICE DISPATCH!");
      fetchSafetyData();
    }
  } catch (err) {
    alert("SOS Dispatch failed.");
  }
}

function openModal() { document.getElementById('leadModal').classList.remove('hidden'); }
function closeModal() { document.getElementById('leadModal').classList.add('hidden'); }

async function submitLead(e) {
  e.preventDefault();
  const leadPayload = {
    name: document.getElementById('inputName').value,
    contact: document.getElementById('inputContact').value,
    budget: document.getElementById('inputBudget').value,
    timeline: document.getElementById('inputTimeline').value,
    region: document.getElementById('inputRegion').value
  };

  try {
    const res = await fetch(`${BASE_URL}/leads`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(leadPayload)
    });
    if (res.ok) {
      closeModal();
      document.getElementById('leadForm').reset();
      fetchLeadsData();
    }
  } catch (err) {
    alert("Error submitting lead.");
  }
}

// Initial Data Load
fetchLeadsData();
fetchSafetyData();




