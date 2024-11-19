from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import nbformat
from nbconvert import HTMLExporter


app = FastAPI()

def convertir_notebook_a_html(ruta: str) -> str:
    """Convierte un notebook de Jupyter a HTML y devuelve el contenido HTML como una cadena."""
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            notebook = nbformat.read(f, as_version=4)
        
        exportador_html = HTMLExporter()
        cuerpo, recursos = exportador_html.from_notebook_node(notebook)
        return cuerpo
    except FileNotFoundError:
        return None
    except Exception as e:
        return str(e)

@app.get("/3501_Visualizacion-de-Datos", tags=["Jupyter"])
def leer_notebook_1():
    ruta = "/home/chilis/Documentos/3501_Visualizacion-de-Datos.ipynb"
    contenido_html = convertir_notebook_a_html(ruta)
    if contenido_html:
        return HTMLResponse(content=contenido_html)
    else:
        return HTMLResponse(content="<h1>Archivo no encontrado</h1>", status_code=404)

@app.get("/Regresion_Logistica", tags=["Jupyter"])
def leer_notebook_2():
    ruta = "/home/chilis/Documentos/Regresion_Logistica.ipynb"
    contenido_html = convertir_notebook_a_html(ruta)
    if contenido_html:
        return HTMLResponse(content=contenido_html)
    else:
        return HTMLResponse(content="<h1>Archivo no encontrado</h1>", status_code=404)

@app.get("/3501_Preparacion-del-DataSet", tags=["Jupyter"])
def leer_notebook_3():
    ruta = "/home/chilis/Documentos/3501_Preparacion-del-DataSet.ipynb"
    contenido_html = convertir_notebook_a_html(ruta)
    if contenido_html:
        print(contenido_html[:500])  # Imprimir los primeros 500 caracteres del contenido HTML para verificar
        return HTMLResponse(content=contenido_html, media_type="text/html")
    else:
        return HTMLResponse(content="<h1>Archivo no encontrado</h1>", status_code=404)

@app.get("/3501_Creacion_de_Transformadores_y_Pipelines_Personalizados", tags=["Jupyter"])
def leer_notebook_4():
    ruta = "/home/chilis/Documentos/3501_Creacion_de_Transformadores_y_Pipelines_Personalizados.ipynb"
    contenido_html = convertir_notebook_a_html(ruta)
    if contenido_html:
        print(contenido_html[:50000])  # Imprimir los primeros 500 caracteres del contenido HTML para verificar
        return HTMLResponse(content=contenido_html, media_type="text/html")
    else:
        return HTMLResponse(content="<h1>Archivo no encontrado</h1>", status_code=404)



@app.get("/3501_Evaluacion-de-Resultados", tags=["Jupyter"])
def leer_notebook_5():
    ruta = "/home/chilis/Documentos/3501_Evaluacion-de-Resultados.ipynb"
    contenido_html = convertir_notebook_a_html(ruta)
    if contenido_html:
        return HTMLResponse(content=contenido_html)
    else:
        return HTMLResponse(content="<h1>Archivo no encontrado</h1>", status_code=404)
