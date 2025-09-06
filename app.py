import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Quiz Software Libre", page_icon="🐧", layout="centered")

st.title("🐧 Quiz sobre Software Libre")

# -------------------
# Banco de preguntas
# -------------------

# Nivel 1: Richard Stallman
preguntas_nivel1 = [
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
        "opciones": [
            "El software debe ser gratuito siempre",
            "El software debe ser libre para usar, estudiar, modificar y compartir",
            "El software debe ser comercial",
            "El software debe ser cerrado"
        ],
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
        "opciones": [
            "Vender software libre",
            "Proteger y promover la libertad de los usuarios de software",
            "Competir con Microsoft",
            "Distribuir hardware libre"
        ],
        "respuesta": "Proteger y promover la libertad de los usuarios de software"
    }
]

# Nivel 2: FSF, Linus Torvalds y Licencias
preguntas_nivel2 = [
    {
        "pregunta": "¿Cuál de estas NO es una de las 4 libertades del software libre según la FSF?",
        "opciones": [
            "Libertad de ejecutar el programa con cualquier propósito",
            "Libertad de estudiar el programa y modificarlo",
            "Libertad de distribuir copias",
            "Libertad de vender la licencia propietaria"
        ],
        "respuesta": "Libertad de vender la licencia propietaria"
    },
    {
        "pregunta": "¿Quién es Linus Torvalds?",
        "opciones": ["Creador de Linux Kernel", "Fundador de GNU", "CEO de IBM", "Desarrollador de Windows"],
        "respuesta": "Creador de Linux Kernel"
    },
    {
        "pregunta": "¿En qué año publicó Linus Torvalds la primera versión de Linux?",
        "opciones": ["1983", "1991", "2000", "1995"],
        "respuesta": "1991"
    },
    {
        "pregunta": "¿Qué licencia usa el kernel de Linux?",
        "opciones": ["GPLv2", "GPLv3", "MIT", "Apache 2.0"],
        "respuesta": "GPLv2"
    },
    {
        "pregunta": "La Apache License 2.0 es conocida por...",
        "opciones": [
            "Ser copyleft fuerte",
            "Permitir uso comercial con cláusula de patentes",
            "Prohibir la distribución comercial",
            "Ser exclusiva para Java"
        ],
        "respuesta": "Permitir uso comercial con cláusula de patentes"
    },
    {
        "pregunta": "¿Cuál licencia coloca el software en dominio público?",
        "opciones": ["GPLv3", "Unlicense", "MIT", "EPL-2.0"],
        "respuesta": "Unlicense"
    },
    {
        "pregunta": "¿Qué significa LGPL?",
        "opciones": [
            "Licencia GNU para juegos",
            "Lesser General Public License",
            "Linux General Protection License",
            "Libre General Public License"
        ],
        "respuesta": "Lesser General Public License"
    },
    {
        "pregunta": "¿Qué licencia fue creada por la comunidad Mozilla?",
        "opciones": ["Apache 2.0", "MPL 2.0", "BSD 3-Clause", "MIT"],
        "respuesta": "MPL 2.0"
    },
    {
        "pregunta": "La AGPL obliga a liberar código cuando...",
        "opciones": [
            "Se distribuye como software de escritorio",
            "Se usa solo para investigación",
            "Se accede a través de una red (ej. web apps)",
            "Se vende en un CD"
        ],
        "respuesta": "Se accede a través de una red (ej. web apps)"
    },
    {
        "pregunta": "¿Cuál de estas es una licencia permisiva?",
        "opciones": ["MIT", "GPLv3", "AGPL", "LGPL"],
        "respuesta": "MIT"
    }
]

# -------------------
# Estado de sesión
# -------------------
if "nivel" not in st.session_state:
    st.session_state.nivel = 1
if "respuestas" not in st.session_state:
    st.session_state.respuestas = []
if "mostrar_resultado" not in st.session_state:
    st.session_state.mostrar_resultado = False

# Selección de preguntas según nivel
preguntas = preguntas_nivel1 if st.session_state.nivel == 1 else preguntas_nivel2

# Inicializar respuestas
if len(st.session_state.respuestas) != len(preguntas):
    st.session_state.respuestas = [None] * len(preguntas)

# -------------------
# Mostrar preguntas
# -------------------
st.header(f"Nivel {st.session_state.nivel}")

for i, p in enumerate(preguntas):
    st.session_state.respuestas[i] = st.radio(
        f"{i+1}. {p['pregunta']}",
        p["opciones"],
        index=None,
        key=f"q{st.session_state.nivel}_{i}"
    )

# -------------------
# Botón calcular puntaje
# -------------------
if st.button("Calcular Puntaje"):
    puntaje = 0
    for i, p in enumerate(preguntas):
        if st.session_state.respuestas[i] == p["respuesta"]:
            puntaje += 1
    st.session_state.mostrar_resultado = True
    st.session_state.puntaje = puntaje

# -------------------
# Mostrar resultados
# -------------------
if st.session_state.mostrar_resultado:
    st.subheader(f"Tu puntaje: {st.session_state.puntaje} / {len(preguntas)}")
    if st.session_state.puntaje == len(preguntas):
        st.success("¡Perfecto! 🎉 Obtuviste el puntaje máximo.")
        st.balloons()
    elif st.session_state.puntaje >= 7:
        st.info("¡Muy bien! Pero aún puedes mejorar.")
    else:
        st.warning("Necesitas repasar más sobre este tema.")

    # Botón siguiente nivel
    if st.session_state.nivel == 1:
        if st.button("Ir al siguiente nivel ➡️"):
            st.session_state.nivel = 2
            st.session_state.respuestas = [None] * len(preguntas_nivel2)
            st.session_state.mostrar_resultado = False
            st.rerun()
