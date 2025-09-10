from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from funciones_agentes.obtener_clima import obtener_clima
from funciones_agentes.obtener_precio_accion import obtener_precio_accion

from utils.sanitizar import sanitizar

# Configuración de Selenium
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
options.add_argument('--disable-blink-features=AutomationControlled')

# Inicialización del driver
driver = webdriver.Chrome(
    service=Service("/usr/lib/chromium-browser/chromedriver"),
    options=options
)

# Función para mapear input del usuario a la función correspondiente
def procesar_input(user_input):
    if "clima" in user_input or "temperatura" in user_input:
        return obtener_clima
    elif "precio" in user_input or "accion" in user_input or "valor" in user_input:
        # Función que mantiene la misma firma que los agentes
        def accion_con_simbolo(driver, _):
            symbol = input("Ingresa el símbolo de la acción (ej. AAPL, TSLA): ").upper()
            return obtener_precio_accion(symbol)
        return accion_con_simbolo
    return None

# Bucle principal
print("Hola, soy tu asistente virtual. ¿En qué puedo ayudarte hoy?")
try:
    while True:
        user_input = sanitizar(input("---> "))
        
        if user_input.lower() in ["salir", "exit", "quit"]:
            print("Cerrando asistente...")
            break
        
        funcion_agente = procesar_input(user_input)
        
        if funcion_agente is None:
            print("No entendí tu solicitud. Intenta nuevamente.")
        else:
            respuesta = funcion_agente(driver, user_input)
            print(f">>> {respuesta}")
finally:
    driver.quit()
