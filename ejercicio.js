fetch('http://localhost:8000/usuarios/clientes', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        // Tus datos aquí
        nombre_completo: "Matias Anovazzi",
        dni: "46839756",
        edad: 19,
        telefono:"3476598984"
    })
})
.then(response => response.json())
.then(data => {
    console.log('Respuesta:', data);
})
.catch(error => {
    console.error('Error:', error);
});



fetch('http://localhost:8000/usuarios/clientes', {
    method: 'GET',
    headers: {
        'Content-Type': 'application/json'
    },
    
})
.then(response => response.json())
.then(data => {
    console.log('Respuesta:', data);
})
.catch(error => {
    console.error('Error:', error);
});