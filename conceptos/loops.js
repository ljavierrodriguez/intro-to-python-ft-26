// Loops
/*  

for(iterador; condicion; increment){
    codigo
}

for(indice in coleccion){
    codigo
}

for(value of coleccion){
    codigo
}

while(condition){
    codigo
}

do {
    codigo
} while(condition)


*/

let nombres = ["Hugo", "Paco", "Luis"]

for(let i = 1; i <= 10; i++){
    console.log(i)
}

for(let i = 0; i < nombres.length; i++){
    console.log(nombres[i])
}

for(let indice in nombres){
    console.log(nombres[indice])
}

for(let valor of nombres){
    console.log(valor)
}

let indice = 0
while (indice < nombres.length){
    console.log(nombres[indice])
    indice++
}