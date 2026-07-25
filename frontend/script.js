document.addEventListener("DOMContentLoaded", () => {
  const scraperForm = document.getElementById("scraper-form");
  const scrapeBtn = document.getElementById("scrape-btn");
  const tableBody = document.getElementById("leads-table-body");
  const leadCount = document.getElementById("lead-count");

  // Fixed Mock Leads Structure
  const mockLeads = [
    { company: "VinHomes Luxury Realty", email: "contact@vinhomes-luxury.vn", phone: "+84 90 123 4567", status: "Verified" },
    { company: "Saigon Premier Properties", email: "info@saigonpremier.com", phone: "+84 91 876 5432", status: "Verified" },
    { company: "HCMC Elite Estates", email: "sales@hcmcelite.vn", phone: "+84 93 333 2211", status: "Pending" }
  ];

  scraperForm.addEventListener("submit", (e) => {
    e.preventDefault();

    // Loading State UI
    scrapeBtn.disabled = true;
    scrapeBtn.innerHTML = `<i class="fa-solid fa-spinner animate-spin"></i> Scraping...`;

    setTimeout(() => {
      // Clear empty state / old rows
      tableBody.innerHTML = "";

      // Populate Table correctly
      mockLeads.forEach(lead => {
        const row = document.createElement("tr");
        row.className = "hover:bg-slate-800/40 transition-colors";
        row.innerHTML = `
          <td class="py-3 px-3 font-medium text-white">${lead.company}</td>
          <td class="py-3 px-3 text-slate-400">${lead.email}</td>
          <td class="py-3 px-3 text-slate-400">${lead.phone}</td>
          <td class="py-3 px-3">
            <span class="px-2 py-0.5 text-xs rounded ${
              lead.status === 'Verified' 
                ? 'bg-emerald-500/10 text-emerald-400 border border-emerald-500/20' 
                : 'bg-amber-500/10 text-amber-400 border border-amber-500/20'
            }">
              ${lead.status}
            </span>
          </td>
        `;
        tableBody.appendChild(row);
      });

      leadCount.textContent = `${mockLeads.length} Leads`;

      // Reset Button
      scrapeBtn.disabled = false;
      scrapeBtn.innerHTML = `<i class="fa-solid fa-magnifying-glass"></i> Start Scraping`;
    }, 1200);
  });
});
