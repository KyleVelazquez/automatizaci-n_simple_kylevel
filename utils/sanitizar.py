import unicodedata

def sanitizar(texto: str):
    # Convertir a minúsculas
    texto = texto.lower()

    # Normalizar para quitar acentos/diéresis
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")

    # Reemplazar ñ por n
    texto = texto.replace("ñ", "n")

    return texto