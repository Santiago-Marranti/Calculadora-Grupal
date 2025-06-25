import streamlit as st

#Agregamos todas las funciones
import division
import logaritmo
import logaritmonatural
import Multiplicacion
import Potencia
import resta
import suma
import RaizCuadrada

st.title("🧮 Calculadora Científica")

opciones = ["Suma", "Resta", "Multiplicación", "División", "Raíz Cuadrada", "Potencia", "Logaritmo Natural", "Logaritmo base 10"]
op = st.selectbox("Selecciona la operación:", opciones)

a = st.number_input("Primer número:", format="%.5f")
b = st.number_input("Segundo número (si aplica):", format="%.5f")

if st.button("Calcular"):
    if op == "Suma":
        st.success(suma.sumar_numeros(a, b));
    elif op == "Resta":
        st.success(resta.resta(a, b))
    elif op == "Multiplicación":
        st.success(Multiplicacion.multiplicar(a, b))
    elif op == "División":
        st.success(division.dividir(a, b))
    elif op == "Raíz Cuadrada":
        st.success(RaizCuadrada.raiz_cuadrada(a))
    elif op == "Potencia":
        st.success(Potencia.calcular_potencia(a, b))
    elif op == "Logaritmo Natural":
        st.success(logaritmonatural.calcular_ln(a))
    elif op == "Logaritmo base 10":
        st.success(logaritmo.calcular_logaritmo_base10(a));