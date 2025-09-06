import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Quiz: Richard Stallman", page_icon="🖥️", layout="centered")

st.title("🖥️ Quiz: Richard Stallman")
st.write("Responde las siguientes 10 preguntas sobre Richard Stallman. Marca la respuesta correcta en cada una.")

# Preguntas y respuestas
preguntas = [
    {
        "pregunta": "¿Quién es Richard Stallman?",
        "opciones": ["Fundador de Microsoft", "Creador del movimiento de software libre", "Inventor de Internet", "CEO de Apple"],
        "respuesta": "Creador del movimiento de software libre"
    },
    {
        "pregunta": "¿Qué significa GNU?",
        "opciones": ["Global Network Utility", "GNU's Not Unix", "General New User", "Graphical Network Unit"],
        "respuesta": "GNU's Not Unix"
    },
    {
        "pregunta": "¿Cuál es la filosofía central de Stallman?",
        "opciones": ["El software debe ser gratuito siempre", "El software debe ser libre para usar, estudiar, modificar y compartir", "El software debe ser comercial", "El software debe ser cerrado"],
        "respuesta": "El software debe ser libre para usar, estudiar, modificar y compartir"
    },
    {
        "pregunta": "¿Qué licencia creó Stallman?",
        "opciones": ["MIT License", "GPL (General Public License)", "Apache License", "Creative Commons"],
        "respuesta": "GPL (General Public License)"
    },
    {
        "pregunta": "¿Qué organización fundó Stallman?",
        "opciones": ["Electronic Frontier Foundation", "Free Software Foundation", "Mozilla Foundation", "Linux Foundation"],
        "respuesta": "Free Software Foundation"
    },
    {
        "pregunta": "¿Cuál fue uno de los primeros proyectos GNU?",
        "opciones": ["GNU Emacs", "Linux Kernel", "Firefox", "Windows 95"],
        "respuesta": "GNU Emacs"
    },
    {
        "pregunta": "¿Qué relación tiene Stallman con Linux?",
        "opciones": ["Lo creó él mismo", "No tiene ninguna relación", "Promovió GNU/Linux como sistema libre", "Es CEO de RedHat"],
        "respuesta": "Promovió GNU/Linux como sistema libre"
    },
    {
        "pregunta": "¿En qué año se inició el Proyecto GNU?",
        "opciones": ["1983", "1991", "1975", "2000"],
        "respuesta": "1983"
    },
    {
        "pregunta": "¿Qué término insiste Stallman en usar para el sistema operativo?",
        "opciones": ["Linux", "GNU/Linux", "Unix", "BSD"],
        "respuesta": "GNU/Linux"
    },
    {
        "pregunta": "¿Cuál es el objetivo de la Free Software Foundation?",
        "opciones": ["Vender software libre", "Proteger y promover la libertad de los usuarios de software", "Competir con Microsoft", "Distribuir hardware libre"],
        "respuesta": "Proteger y promover la libertad de los usuarios de software"
    }
]

# Estado de sesión para respuestas
if "respuestas" not in st.session_state:
    st.session_state.respuestas = [None] * len(preguntas)
if "mostrar_resultado" not in st.session_state:
    st.session_state.mostrar_resultado = False

# Mostrar preguntas
for i, p in enumerate(preguntas):
    st.session_state.respuestas[i] = st.radio(
        f"{i+1}. {p['pregunta']}",
        p["opciones"],
        index=None,
        key=f"q{i}"
    )

# Botón para calcular puntaje
if st.button("Calcular Puntaje"):
    puntaje = 0
    for i, p in enumerate(preguntas):
        if st.session_state.respuestas[i] == p["respuesta"]:
            puntaje += 1
    st.session_state.mostrar_resultado = True
    st.session_state.puntaje = puntaje

# Mostrar resultados
if st.session_state.mostrar_resultado:
    st.subheader(f"Tu puntaje: {st.session_state.puntaje} / {len(preguntas)}")
    if st.session_state.puntaje == len(preguntas):
        st.success("¡Perfecto! 🎉 Obtuviste el puntaje máximo.")
        st.balloons()
    elif st.session_state.puntaje >= 7:
        st.info("¡Muy bien! Pero aún puedes mejorar.")
    else:
        st.warning("Necesitas repasar más sobre Richard Stallman.")

# Botón para reiniciar
if st.button("Reiniciar Juego"):
    st.session_state.respuestas = [None] * len(preguntas)
    st.session_state.mostrar_resultado = False
    for i in range(len(preguntas)):
        st.session_state[f"q{i}"] = None
    st.rerun()
