# CS2 Major Tracker

Aplicación de escritorio para el seguimiento de torneos oficiales de Counter-Strike 2 (CS2 Majors).  
Desarrollada con **Python** y **wxPython**, con persistencia de datos en archivos **JSON**.

> Universidad Nacional de Pilar · Programación Orientada a Objetos · 2026  
> Equipo: Bellochi Facundo, Leffler Santiago, Dalmazzo Julián, Alegre Thiago

---

## 1. Clonar el repositorio

Abrí una terminal, navegá a la carpeta donde querés guardar el proyecto y ejecutá:

```bash
git clone https://github.com/Facundo-Bellochi/CS2-Major-Tracker
```

---

## 2. Abrir el proyecto en Visual Studio Code

Una vez clonado, entrás a la carpeta del proyecto:

```bash
cd CS2-Major-Tracker
```

Y abrís VS Code desde ahí:

```bash
code .
```

Esto abre Visual Studio Code directamente con la carpeta del proyecto cargada.

---

## 3. Crear un entorno virtual (recomendado)

Un entorno virtual permite instalar las librerías del proyecto sin afectar el resto de tu sistema. Es una buena práctica y se recomienda hacerlo siempre.

**Crear el entorno virtual:**

```bash
python -m venv venv
```

**Activarlo:**

En Windows:
```bash
venv\Scripts\activate
```

En Mac / Linux:
```bash
source venv/bin/activate
```

Cuando está activo, vas a ver `(venv)` al principio de la línea en la terminal.

> En VS Code podés seleccionar el entorno virtual como intérprete de Python presionando `Ctrl+Shift+P` y buscando **"Python: Select Interpreter"**. Elegí el que dice `venv`.

---

## 4. Instalar las dependencias

Con el entorno virtual activado, instalá todas las librerías necesarias con un solo comando:

```bash
pip install -r requirements.txt
```

Esto instala automáticamente:
- **wxPython** — para la interfaz gráfica
- **reportlab** — para la exportación de PDF

Y alguna libreria necesaria mas para reportlab

---

## Estructura del proyecto

```
cs2_major_tracker/
│
├── main.py                  # Punto de entrada de la aplicación
│
├── data/                    # Archivos JSON de persistencia
│   ├── usuarios.json
│   ├── torneo.json
│   ├── equipos.json
│   └── posiciones.json
│
├── models/                  # Clases del dominio (POO)
│   ├── usuario.py
│   ├── equipo.py
│   ├── partido.py
│   └── torneo.py
│
├── services/                # Servicios de soporte
│   ├── gestor_json.py       # Lectura y escritura de JSON
│   └── exportador_pdf.py    # Generación de PDF con reportlab
│
├── views/                   # Interfaz gráfica con wxPython
│   ├── splash_frame.py
│   ├── acceso_frame.py
│   ├── login_dialog.py
│   ├── registro_dialog.py
│   ├── ventana_principal.py
│   ├── panel_inicio.py
│   ├── panel_fixture.py
│   ├── panel_posiciones.py
│   └── panel_equipos.py
│
├── assets/                  # Recursos visuales
│   ├── logo.png
│   ├── mapas/
│   └── equipos/
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Solución de problemas frecuentes

**`python` no se reconoce como comando**  
En Windows a veces hay que usar `python3` en vez de `python`. También verificá que Python esté agregado al PATH durante la instalación.

## Flujo de trabajo con Git (para el equipo)

Antes de ponerse a codear, siempre traer los últimos cambios:
```bash
git pull
```

Cuando terminás algo, subir los cambios:
```bash
git add .
git commit -m "Descripción corta de lo que hiciste"
git push
```
**IMPORTANTE**
> Se recomienda que cada integrante trabaje en su propia rama y haga un **Pull Request** para integrar al main, así evitamos conflictos.