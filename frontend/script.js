const API_URL = 'https://aetheris-ai-solutions.onrender.com/api/leads';

async function fetchLeadsData() {
  const tableBody = document.getElementById('leadTable');
  tableBody.innerHTML = `<tr><td colspan="6" class="p-4 text-center text-slate-500">Connecting to Aetheris AI Engine...</td></tr>`;

  try {
    const response = await fetch(API_URL);
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
    tableBody.innerHTML = `<tr><td colspan="6" class="p-4 text-center text-red-400">Failed to sync live data. Retrying...</td></tr>`;
  }
}

function openModal() {
  document.getElementById('leadModal').classList.remove('hidden');
}

function closeModal() {
  document.getElementById('leadModal').classList.add('hidden');
}

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
    const res = await fetch(API_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(leadPayload)
    });
    
    if (res.ok) {
      closeModal();
      document.getElementById('leadForm').reset();
      fetchLeadsData(); // Instant Refresh Table
    }
  } catch (err) {
    alert("Error submitting lead to AI Engine.");
  }
}

// Initial fetch on page load
fetchLeadsData();


