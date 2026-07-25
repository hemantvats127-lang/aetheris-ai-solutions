async function fetchRevenueData() {
  try {
    const response = await fetch(`${BASE_URL}/revenue`);
    const data = await response.json();

    if (data.success && data.analytics) {
      const revenueTable = document.getElementById('revenueTable');
      if (revenueTable) {
        revenueTable.innerHTML = data.analytics.map(item => `
          <tr class="hover:bg-slate-900/80">
            <td class="p-3 font-semibold text-slate-100">${item.region}</td>
            <td class="p-3 font-bold text-emerald-400">${item.forecast_rev}</td>
            <td class="p-3 text-xs text-slate-300">${item.broker_split}</td>
            <td class="p-3 text-xs text-amber-400">${item.agent_split}</td>
            <td class="p-3 text-xs font-bold text-sky-400">${item.deals_closed} Deals</td>
          </tr>
        `).join('');
      }
    }
  } catch (err) {
    console.error("Revenue Engine fetch error:", err);
  }
}

async function fetchEscrowData() {
  try {
    const response = await fetch(`${BASE_URL}/escrow`);
    const data = await response.json();

    if (data.success && data.deals) {
      const escrowTable = document.getElementById('escrowTable');
      if (escrowTable) {
        escrowTable.innerHTML = data.deals.map(deal => `
          <tr class="hover:bg-slate-900/80">
            <td class="p-3 font-semibold text-slate-200">${deal.property}</td>
            <td class="p-3 font-mono text-xs text-emerald-300">${deal.token_amt}</td>
            <td class="p-3 font-bold text-xs">${deal.escrow_status}</td>
            <td class="p-3 text-xs text-slate-300">${deal.doc_sign}</td>
            <td class="p-3 text-xs font-mono text-purple-400">${deal.closing_date}</td>
          </tr>
        `).join('');
      }
    }
  } catch (err) {
    console.error("Escrow Engine fetch error:", err);
  }
}

// Initial Data Fetch Execution
fetchRevenueData();
fetchEscrowData();
