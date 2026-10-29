import json
import urllib.request
import urllib.error

BASE_URL = "http://127.0.0.1:8000/api/proyectos/"


def enviar_peticion(metodo, url, datos=None):
    cuerpo = None
    if datos is not None:
        cuerpo = json.dumps(datos).encode("utf-8")

    peticion = urllib.request.Request(
        url,
        data=cuerpo,
        headers={"Content-Type": "application/json"},
        method=metodo
    )

    try:
        with urllib.request.urlopen(peticion) as respuesta:
            contenido = respuesta.read().decode("utf-8")
            print(f"\n{metodo} - Estado HTTP: {respuesta.status}")
            print(contenido)
            return json.loads(contenido) if contenido else {}

    except urllib.error.HTTPError as error:
        print(f"\n{metodo} - Estado HTTP: {error.code}")
        print(error.read().decode("utf-8"))
    except urllib.error.URLError as error:
        print("No se pudo conectar con Django:", error.reason)

    return None


# 1. GET: consultar todos los proyectos
enviar_peticion("GET", BASE_URL)

# 2. POST: crear un proyecto
creado = enviar_peticion(
    "POST",
    BASE_URL,
    {
        "nombre": "Proyecto de prueba",
        "descripcion": "Prueba de los métodos HTTP"
    }
)

# 3. PUT: modificar el proyecto recién creado
if creado and "id" in creado:
    proyecto_id = creado["id"]
    url_detalle = f"{BASE_URL}{proyecto_id}/"

    enviar_peticion(
        "PUT",
        url_detalle,
        {
            "nombre": "Proyecto actualizado",
            "descripcion": "Descripción modificada"
        }
    )

    # 4. DELETE: eliminar el proyecto de prueba
    enviar_peticion("DELETE", url_detalle)