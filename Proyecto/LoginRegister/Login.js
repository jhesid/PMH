document.getElementById("btn iniciar-sesion").addEventListener("click", login);

document.getElementById("btn Register").addEventListener("click", register);

var contenedorLoginRegister = document.querySelector(".contenedorLoginRegister");
var formularioLogin = document.querySelector(".formularioLogin");
var formularioRegister = document.querySelector(".formularioRegister");
var cajaAtrasLogin = document.querySelector(".cajaAtrasLogin");
var cajaAtrasRegister = document.querySelector(".cajaAtrasRegister");

function login(){
    if(window.innerWidth > 850){
        formularioRegister.style.display="none";
        contenedorLoginRegister.style.left="10px";
        formularioLogin.style.display="block";
        cajaAtrasRegister.style.opacity="1";
        cajaAtrasLogin.style.opacity="0";
    }else{
        formularioRegister.style.display="none";
        contenedorLoginRegister.style.left="0px";
        formularioLogin.style.display="block";
        cajaAtrasRegister.style.opacity="block";
        cajaAtrasLogin.style.opacity="none";
    }
}

function register(){
    if(window.innerWidth > 850){
        formularioRegister.style.display="block";
        contenedorLoginRegister.style.left="410px";
        formularioLogin.style.display="none";
        cajaAtrasRegister.style.opacity="0";
        cajaAtrasLogin.style.opacity="1";
    }else{
        formularioRegister.style.display="block";
        contenedorLoginRegister.style.left="0px";
        formularioLogin.style.display="none";
        cajaAtrasRegister.style.opacity="none";
        cajaAtrasLogin.style.display="block";
        cajaAtrasLogin.style.opacity="1";
    }
}