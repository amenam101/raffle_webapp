# Mi web de sorteos
En esta web puedes subir un archivo .csv y hacer un sorteo.

La web está hecha netamente con Reflex, un framework de Python.

## Instalación:

```bash
python -m venv env

# Activación en Unix
source env/bin/activate

# Activación en Windows
env\Scripts\activate

pip install -r requirements.txt
```
## Run:

```bash
# Para iniciar el proyecto
cd final_project
reflex init

# Para correr la webapp
reflex run
```

## Archivo:

```
El formato del .csv debe ser en este formato:

id;Nombre
1;Juan
2;Pedro
3;Maria
4;Luis
5;Ana
6;Jose
```