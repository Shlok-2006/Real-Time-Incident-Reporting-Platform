async function loadIncidents() {
  const res = await fetch(`${API_BASE}/incidents`);
  const incidents = await res.json();

  const container = document.getElementById("incidentList");
  container.innerHTML = "";

  incidents.forEach(i => {
    const div = document.createElement("div");
    div.innerHTML = `
      <strong>${i.type}</strong><br/>
      ${i.description}<br/>
      Severity: ${i.severity}<br/>
      Votes: ${i.votes}<br/>
      Status: ${i.status}<br/>
      <button onclick="upvote('${i.id}')">Upvote</button>
      <hr/>
    `;
    container.appendChild(div);
  });
}

async function upvote(id) {
  await fetch(`${API_BASE}/incidents/${id}/upvote`, { method: "POST" });
  loadIncidents();
}

setInterval(loadIncidents, 3000);
loadIncidents();
