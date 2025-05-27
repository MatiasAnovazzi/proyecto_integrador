let str = "16, 43, 34, 32, 21, 44, 16, 28, 39, 41, 40, 30, 32, 42, 38, 37, 26, 25, 16, 15, 25, 19, 17, 27, 32, 43, 44, 40, 25, 24, 34, 31, 43, 42, 35, 40, 43, 42, 40, 31"
let array = str // Reemplaza todas las comas por puntos
    .split(",")         // Divide por ;
    .map(e => parseFloat(e)) // Quita espacios y convierte en float

let primer_rango = array.filter(e => e >= 15 && e < 25);
let segundo_rango = array.filter(e => e >= 25 && e < 35);
let tercer_rango = array.filter(e => e >= 35 && e < 45);

console.log("Primer rango (15-25):", primer_rango, "Total:", primer_rango.length);
console.log("Promedio primer rango:", (primer_rango.reduce((a, b) => a + b, 0) / primer_rango.length).toFixed(2));
console.log("")
console.log("Segundo rango (25-35):", segundo_rango, "Total:", segundo_rango.length);
console.log("Promedio segundo rango:", (segundo_rango.reduce((a, b) => a + b, 0) / segundo_rango.length).toFixed(2));
console.log("")
console.log("Tercer rango (35-45):", tercer_rango, "Total:", tercer_rango.length);
console.log("Promedio tercer rango:", (tercer_rango.reduce((a, b) => a + b, 0) / tercer_rango.length).toFixed(2));

console.log("Total de valores:", array.length);
