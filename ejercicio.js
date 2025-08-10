// Si usas Node 18+ puedes usar global fetch sin instalar
const readline = require('readline');

const BASE_URL = 'http://localhost:8000';

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function question(prompt) {
  return new Promise(resolve => rl.question(prompt, resolve));
}

async function listarClientes() {
  const res = await fetch(`${BASE_URL}/usuarios/clientes`);
  const data = await res.json();
  console.log('Clientes:', data);
}

async function listarProfesionales() {
  const res = await fetch(`${BASE_URL}/usuarios/profesionales`);
  const data = await res.json();
  console.log('Profesionales:', data);
}


async function crearCliente() {
  const nombre_completo = await question('Nombre completo: ');
  const telefono = await question('Teléfono: ');
  const dni = await question('DNI: ');
  const edadStr = await question('Edad: ');
  const edad = Number(edadStr);

  const nuevoCliente = { nombre_completo, telefono, dni, edad };

  const res = await fetch(`${BASE_URL}/usuarios/clientes`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(nuevoCliente)
  });
  const data = await res.json();
  console.log('Cliente creado:', data);
}

async function crearProfesional() {
  const nombre_completo = await question('Nombre completo: ');
  const telefono = await question('Teléfono: ');
  const especialidad = await question('Especialidad: ');

  const nuevoProfesional = { nombre_completo, telefono, especialidad };

  const res = await fetch(`${BASE_URL}/usuarios/profesionales`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(nuevoProfesional)
  });
  const data = await res.json();
  console.log('Profesional creado:', data);
}

async function listarTurnosPorProfesional() {
  const idStr = await question('ID profesional: ');
  const id = Number(idStr);
  const res = await fetch(`${BASE_URL}/turnos/?id_profesional=${id}`);
  const data = await res.json();
  console.log(`Turnos del profesional ${id}:`, data);
}

async function crearTurno() {
  const titulo = await question('Título: ');
  const hora_inicio = await question('Hora inicio (YYYY-MM-DDTHH:mm:ss): ');
  const hora_fin = await question('Hora fin (YYYY-MM-DDTHH:mm:ss): ');
  const id_profesionalStr = await question('ID profesional: ');
  const id_clienteStr = await question('ID cliente: ');
  const descripcion = await question('Descripción (opcional): ');

  const id_profesional = Number(id_profesionalStr);
  const id_cliente = Number(id_clienteStr);

  const nuevoTurno = { titulo, hora_inicio, hora_fin, id_profesional, id_cliente };
  if (descripcion) nuevoTurno.descripcion = descripcion;

  const res = await fetch(`${BASE_URL}/turnos`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(nuevoTurno)
  });
  const data = await res.json();
  console.log('Turno creado:', data);
}

async function mainMenu() {
  while (true) {
    console.log('\nElige una opción:');
    console.log('1. Listar clientes');
    console.log('2. Listar profesionales')
    console.log('3. Crear cliente');
    console.log('4. Crear profesional');
    console.log('5. Listar turnos por profesional');
    console.log('6. Crear turno');
    console.log('0. Salir');

    const opcion = await question('Opción: ');

    switch (opcion.trim()) {
      case '1':
        await listarClientes();
        break;
      case '2':
        await listarProfesionales();
        break;
      case '3':
        await crearCliente();
        break;
      case '4':
        await crearProfesional();
        break;
      case '5':
        await listarTurnosPorProfesional();
        break;
      case '6':
        await crearTurno();
        break;
      case '0':
        console.log('Saliendo...');
        rl.close();
        return;
      default:
        console.log('Opción no válida.');
    }
  }
}

mainMenu();
