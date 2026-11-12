# app.py
def login(user, password):
    # ERROR SAST: Contraseña hardcodeada (en el código)
    #admin_password = "SuperSecretPassword123" 
    if password == admin_password:
        return "Acceso concedido"
    return "Acceso denegado"
