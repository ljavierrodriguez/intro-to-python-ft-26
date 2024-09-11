// Condicionales

/* 

if(condition){
codigo;
}

if(condition){
    codigo
} else {
    condigo
}


if(condtion){

} else if (condition){
 
} else {
 
}


variable = condition ? verdadero : falso


switch(variable){
    case value:
        codigo;
        break;

    default: 
        codigo; 
        break;
}


*/

let a = 5;
let b = 10;
let c = 8

if(a > b){
    console.log("A > B")
}


if (a > c){
    console.log("A > C")
} else {
    console.log("A < C")
}


if(a > b && a > c){
    console.log("A > B y C")
} else if (b > c){
    console.log("B > A y C")
} else {
    console.log("C > A y B")
}


mayor = a > 18 ? true : false

if(mayor){
    console.log("Puedes Pasar")
}