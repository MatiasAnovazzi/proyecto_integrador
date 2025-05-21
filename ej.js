url = "http://127.0.0.1:8000/turnos/"
options = {
    method: "GET",
    headers: {
        "Content-Type": "application/json"
    },
    //body: JSON.stringify({
    //    "nombrecompleto": "Alberto Gonzalez",
    //    "fecha_hora": "2025-10-01T10:00:00"        
}
fetch(url, options).then(response => response.json()).then(
    data => {
        console.log(data)
    }
)