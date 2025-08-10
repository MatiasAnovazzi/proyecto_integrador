const BASE_URL = 'http://localhost:8000';  // Cambiar según tu API

async function testAPI() {
  try {
    // GET /usuarios
    console.log('GET /usuarios/clientes');
    let res = await fetch(`${BASE_URL}/usuarios/clientes`);
    let usuarios = await res.json();
    console.log('Usuarios:', usuarios);

    // POST /usuarios/cliente
    console.log('POST /usuarios/clientes');
    let nuevoCliente = {
      nombre_completo: "Juan Pérez",
      telefono: "123456789",
      dni: "12345678",
      edad: 30
    };
    res = await fetch(`${BASE_URL}/usuarios/clientes`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(nuevoCliente)
    });
    let clienteCreado = await res.json();
    console.log('Cliente creado:', clienteCreado);

    // POST /usuarios/profesional
    console.log('POST /usuarios/profesionales');
    let nuevoProfesional = {
      nombre_completo: "María Gómez",
      telefono: "987654321",
      especialidad: "Cardiología"
    };
    res = await fetch(`${BASE_URL}/usuarios/profesionales`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(nuevoProfesional)
    });
    let profesionalCreado = await res.json();
    console.log('Profesional creado:', profesionalCreado);

    // GET /turnos

    // POST /turnos
    console.log('POST /turnos');
    let nuevoTurno = {
      titulo: "Consulta cardiológica",
      hora_inicio: "2025-08-15T09:00:00",
      hora_fin: "2025-08-15T09:30:00",
      id_profesional: profesionalCreado.id,
      descripcion: "Chequeo anual",
      id_cliente: clienteCreado.id
    };
    res = await fetch(`${BASE_URL}/turnos`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(nuevoTurno)
    });
    let turnoCreado = await res.json();
    console.log('Turno creado:', turnoCreado);

  } catch (error) {
    console.error('Error:', error.message);
  }
}

testAPI();
