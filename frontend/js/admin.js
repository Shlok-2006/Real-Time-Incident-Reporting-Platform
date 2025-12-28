const API_BASE = "http://127.0.0.1:8000";

async function loadAdminIncidents() {
  const res = await fetch(`${API_BASE}/incidents`);
  const incidents = await res.json();

  const container = document.getElementById("adminIncidents");
  container.innerHTML = "";

  incidents.forEach(i => {
    const div = document.createElement("div");
    div.innerHTML = `
      <strong>${i.type}</strong><br/>
      ${i.description}<br/>
      Severity: ${i.severity}<br/>
      <b>Status:</b> ${i.status}<br/>

      <select onchange="updateStatus('${i.id}', this.value)">
        <option value="">Change Status</option>
        <option value="unverified">Unverified</option>
        <option value="in_progress">In Progress</option>
        <option value="resolved">Resolved</option>
      </select>
      <hr/>
    `;
    container.appendChild(div);
  });
}

async function updateStatus(id, status) {
  if (!status) return;

  const res = await fetch(
    `${API_BASE}/admin/incident/${id}/status?status=${status}`,
    {
      method: "PUT",
      headers: {
        "token": "admin"
      }
    }
  );

  if (!res.ok) {
    const err = await res.json();
    alert("❌ Failed to update: " + JSON.stringify(err));
    return;
  }

  alert("✅ Status updated!");
  loadAdminIncidents();
}

loadAdminIncidents();
