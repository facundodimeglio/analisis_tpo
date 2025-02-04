import re

def validar_usuario(usuario):
    """Valida si el usuario cumple con las normas del banco (8-20 caracteres, letras y números)."""
    if not (8 <= len(usuario) <= 20):
        return "Error: El usuario debe tener entre 8 y 20 caracteres."
    if not usuario.isalnum():
        return "Error: El usuario solo puede contener letras y números."
    return "Usuario válido."

def validar_contraseña(contraseña):
    """Valida la seguridad de la contraseña (8-20 caracteres, mayúsculas, minúsculas, números y un carácter especial)."""
    if not (8 <= len(contraseña) <= 20):
        return "Error: La contraseña debe tener entre 8 y 20 caracteres."
    if not re.search(r'[A-Z]', contraseña):
        return "Error: La contraseña debe incluir al menos una letra mayúscula."
    if not re.search(r'[a-z]', contraseña):
        return "Error: La contraseña debe incluir al menos una letra minúscula."
    if not re.search(r'[0-9]', contraseña):
        return "Error: La contraseña debe incluir al menos un número."
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', contraseña):
        return "Error: La contraseña debe incluir al menos un carácter especial (!@#$%^&*...)."
    return "Contraseña segura."

#  Datos ficticios para pruebas automáticas
usuarios_prueba = ["usuario1", "ClienteVIP2024", "123456", "Us3rInv@lido!", "BancoSantander23"]
contraseñas_prueba = ["Abc123!", "segura123*", "PASSWORD", "Santander2024!", "abcdEFGH123$"]

print("\n Resultados de validación automática:")

for usuario in usuarios_prueba:
    print(f"Usuario '{usuario}': {validar_usuario(usuario)}")

for contraseña in contraseñas_prueba:
    print(f"Contraseña '{contraseña}': {validar_contraseña(contraseña)}")

#  Inputs para pruebas manuales
print("\n Prueba manual (ingresa datos para validar en tiempo real):")
usuario_input = input("Ingrese un usuario: ")
print(validar_usuario(usuario_input))

contraseña_input = input("Ingrese una contraseña: ")
print(validar_contraseña(contraseña_input))
