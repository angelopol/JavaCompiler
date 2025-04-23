from google import genai
from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener la clave de API desde las variables de entorno
api_key = os.getenv("GEMINI_API")

# Crear el cliente con la clave de API
client = genai.Client(api_key=api_key)

def compile(code):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents="transform this JAVA code to a python code, only response with the python code, the code is: \n" + code,
    )

    return (response.text.replace("```python", "").replace("```", "").replace("python", "").replace("java", "").replace("java:", "").replace("python:", ""))

def semantic(code):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents="Analyze this Java code semantically, give me errors divided by semicolons if the code has errors, the code is: \n" + code,
    )

    return (response.text.replace("```python", "").replace("```", "").replace("python", "").replace("java", "").replace("java:", "").replace("python:", ""))

if __name__ == '__main__':
    with open("example.java", "r", encoding="utf-8") as file:
        print(semantic(file.read()))