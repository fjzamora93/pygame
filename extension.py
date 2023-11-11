# Solicitar al usuario el nombre del archivo
file_name = input("Ingrese el nombre del archivo: ")

# Convertir el nombre del archivo a minúsculas para hacer la comparación insensible a mayúsculas y minúsculas
file_name_lower = file_name.lower()

# Diccionario que mapea las extensiones a los tipos de medios
extension_to_media_type = {
    ".gif": "image/gif",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip"
}

# Comprobar si el nombre del archivo termina con una de las extensiones especificadas
for extension, media_type in extension_to_media_type.items():
    if file_name_lower.endswith(extension):
        print(f"El tipo de medios del archivo es: {media_type}")
        break
else:
    # Si no se encontró una coincidencia, imprimir el valor predeterminado
    print("El tipo de medios del archivo es: application/octet-stream (predeterminado)")