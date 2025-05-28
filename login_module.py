# login_module.py

# Simulación de base de datos de usuarios
usuarios = {
    "juan": "clave123",
    "maria": "pass456",
    "admin": "admin123"
}

def iniciar_sesion():
    intentos_restantes = 3

    while intentos_restantes > 0:
        usuario = input("Ingrese su usuario: ")
        contrasena = input("Ingrese su contraseña: ")

        # ---------------------
        # DEFECTO (bug):
        # Aquí cometemos un error intencional:
        # Usamos 'usuarios["usuario"]' en lugar de 'usuarios[usuario]'.
        # Esto causará un ERROR (KeyError) en tiempo de ejecución
        # cuando el usuario sea válido pero la clave 'usuario' no exista.
        # ---------------------
        try:
            if usuario in usuarios and contrasena == usuarios["usuario"]:
                print("¡Inicio de sesión exitoso!")
                return True
            else:
                intentos_restantes -= 1
                print(f"Credenciales incorrectas. Intentos restantes: {intentos_restantes}")
        except KeyError:
            # ---------------------
            # ERROR: Este es el error en tiempo de ejecución causado por el defecto.
            # Lo capturamos para explicar el fallo al usuario.
            # ---------------------
            print("Ha ocurrido un error interno en el sistema. Por favor, intente nuevamente.")
            intentos_restantes -= 1
            print(f"Intentos restantes: {intentos_restantes}")

    # ---------------------
    # FALLO: El sistema no permite iniciar sesión aún si las credenciales son correctas,
    # debido al defecto y error en el código. Esto es el fallo visible para el usuario.
    # además, no se puede distinguir el tipo de caracter mayúscula o minúscula, lo que
    # genera otro fallo.
    # ---------------------
    print("Ha excedido el número máximo de intentos. Acceso denegado.")
    return False

if __name__ == "__main__":
    iniciar_sesion()