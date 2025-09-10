from selenium.webdriver.common.by import By

def obtener_clima(driver, consulta):
    driver.get(f"https://www.google.com/search?q=clima+{consulta}")

    try:
        # Nombre del lugar/ciudad
        ciudad = driver.find_element(By.ID, "wob_loc").text

        # Temperatura actual
        temperatura = driver.find_element(By.ID, "wob_tm").text

        # Descripción del clima (ej. Soleado, Nublado, etc.)
        descripcion = driver.find_element(By.ID, "wob_dc").text

        # Unidad de temperatura
        unidad = "°C"  # La unidad por defecto en Google en español

        return f"El clima en {ciudad} es {descripcion}, con una temperatura de {temperatura}{unidad}."
    
    except Exception as e:
        return f"No se pudo obtener el clima en este momento. Error: {e}"
