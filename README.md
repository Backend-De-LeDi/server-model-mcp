# 🧪 Proyecto app-mcp-tintas

Este proyecto es un agente conversacional que utiliza **FastAPI** para el backend, y **LangChain + Gemini (Google Generative AI)** para la lógica de IA.

---

## 🚀 Requisitos Previos

- **Python 3.11.8**: Esta versión es **crucial**.
  > ⚠️ **Importante:** LangChain y Pydantic (usado por FastAPI) tienen problemas de compatibilidad con versiones superiores de Python. Debes usar **exactamente 3.11.8** para evitar errores.
- **Git**
- Una clave de API de **Google Gemini**.
- Una instancia de **MongoDB** (local o remota).

---

## 🔑 Configuración de Entorno

Antes de instalar, clona el repositorio y configura tus variables de entorno.

1.  **Clonar el repositorio:**

    ```bash
    git clone [https://github.com/usuario/app-mcp-tintas.git](https://github.com/usuario/app-mcp-tintas.git)
    cd app-mcp-tintas
    ```

2.  **Crear archivo `.env`:**
    Crea un archivo llamado `.env` en la raíz del proyecto con el siguiente contenido:

    ```bash
    GEMINI_API_KEY=tu_api_key_de_google
    MONGO_URI=mongodb://localhost:27017
    ```

---

## 📦 Instalación

Puedes usar el gestor de paquetes estándar `pip` y `venv` o el más rápido `uv`.

### Opción 1: Usando `venv` y `pip` (Estándar)

1.  **Crear entorno virtual** (asegúrate de que tu sistema usa Python 3.11.8):

    ```bash
    python3.11 -m venv .venv
    ```

    _(Si `python3.11` no funciona, prueba con `python -m venv .venv` o `py -3.11 -m venv .venv` en Windows, asegurándote de que la versión base sea la 3.11.8)_

2.  **Activar entorno:**

    - Linux/Mac:
      ```bash
      source .venv/bin/activate
      ```
    - Windows (PowerShell):
      ```bash
      .venv\Scripts\Activate
      ```

3.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

### Opción 2: Usando `uv` (Recomendado)

`uv` es un gestor de entornos y dependencias moderno y muy rápido.

1.  **Instalar `uv`** (si no lo tienes):

    ```bash
    pip install uv
    ```

2.  **Crear entorno virtual:**

    ```bash
    uv venv --python 3.11.8 .venv
    ```

3.  **Activar entorno:**

    - Linux/Mac:
      ```bash
      source .venv/bin/activate
      ```
    - Windows (PowerShell):
      ```bash
      .venv\Scripts\Activate
      ```

4.  **Instalar dependencias:**
    ```bash
    uv pip install -r requirements.txt
    ```

---

## ▶️ Ejecución

Asegúrate de que tu entorno virtual esté activado (`source .venv/bin/activate`).

### Opción 1: Con Uvicorn (Estándar)

Esta es la forma estándar de ejecutar un servidor FastAPI. `uvicorn` se habrá instalado como dependencia desde `requirements.txt`.

```bash
uvicorn src.main:app --host 127.0.0.1 --port 8000 --reload
```

(El flag --reload es opcional y sirve para que el servidor se reinicie automáticamente al detectar cambios en el código).

### Opción 2: Con uv

Si tienes uv instalado, puedes usar su ejecutor de tareas.

```bash
uv run ./src/main.py
```

Acceso a la API
Una vez que el servidor esté en marcha, puedes acceder a:

- Documentación Interactiva (Swagger UI): http://localhost:8000/docs

- Documentación Alternativa (ReDoc): http://localhost:8000/redoc
