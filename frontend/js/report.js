async function submitIncident(event) {
  event.preventDefault();

  const data = {
    type: document.getElementById("type").value,
    description: document.getElementById("description").value,
    location: document.getElementById("location").value,
    state: document.getElementById("state").value,
    pin: parseInt(document.getElementById("pin").value)
  };

  console.log("Sending incident:", data); // 🔥 DEBUG LINE

  const res = await fetch("http://127.0.0.1:8000/incidents", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(data)
  });

  if (!res.ok) {
    const err = await res.text();
    alert("Failed: " + err);
    return;
  }

  alert("Incident submitted successfully");
}
