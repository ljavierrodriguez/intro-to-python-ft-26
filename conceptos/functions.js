// Funciones

/* 

Funciones Declarativas

function functionName(params...){
    codigo
}


Funciones Expresivas

const variableName = function(params...){
    condigo
}


Funciones de Flecha

const variableName = (params....) => result


*/


function sumar(a, b){
    return a + b
}

const restar = function(a, b){
    return a - b
}

const dividir = (a, b) => a / b


const result = sumar(1, 2)
console.log(result) // 3

/* Parametro Posicional */
function imprimirNombreCompleto(nombre, apellido){
    return `${nombre} ${apellido}`
}

console.log(imprimirNombreCompleto("Jane", "Doe"))

/* Parametro por valores por defecto */

function imprimirNombreCompleto2(nombre="John", apellido="Doe"){
    return `${nombre} ${apellido}`
}

console.log(imprimirNombreCompleto2())


/* Empaqutamiento de Argumentos */

function totalizar(...rest){
    return rest.reduce((total, valor) => total + valor, 0)
}

console.log(totalizar(1, 2, 3, 4, 5, 6))