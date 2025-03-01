import os

# ==============================
#  HEXAGONAL PROJECT GENERATOR
# ==============================

print("\n")
print("    *********       █████╗ ██████╗  ██████╗██╗  ██╗     ")
print("   ***********     ██╔══██╗██╔══██╗██╔════╝██║  ██║     ")
print("  *****   *****    ███████║██████╔╝██║     ███████║     ")
print(" *****     *****   ██╔══██║██╔══██╗██║     ██╔══██║     ")
print("  *****   *****    ██║  ██║██║  ██║╚██████╗██║  ██║     ")
print("   ***********     ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝     ")
print("    *********     ARCH - HEXAGONAL PROJECT GENERATOR    ")
print("                          BY: GUSTAVO TOLEDO            ")
print("\n")


def capitalizar_modelo(modelo):
    """ Capitaliza la primera letra del modelo si no está en mayúsculas """
    return modelo[:1].upper() + modelo[1:]


def crear_estructura(ruta_base, modelos):
    # Obtener el nombre del proyecto desde la ruta
    proyecto = os.path.basename(os.path.normpath(ruta_base))

    # Crear la carpeta base del proyecto si no existe
    os.makedirs(ruta_base, exist_ok=True)

    # Estructura de carpetas
    estructura = [
        "application/dto",
        "application/handler",
        "application/mapper",
        "domain/api",
        "domain/model",
        "domain/spi",
        "domain/usecase",
        "infraestructure/configuration",
        "infraestructure/exception",
        "infraestructure/input/rest",
        "infraestructure/output/jpa/adapter",
        "infraestructure/output/jpa/entity",
        "infraestructure/output/jpa/mapper",
        "infraestructure/output/jpa/repository"
    ]

    # Crear carpetas
    for carpeta in estructura:
        os.makedirs(os.path.join(ruta_base, carpeta), exist_ok=True)

    # Archivos base (corregida la ruta)
    archivos_base = {
        os.path.join(ruta_base, "infraestructure/configuration/BeanConfiguration.java"): 
            "public class BeanConfiguration {}",
        os.path.join(ruta_base, "infraestructure/exception/NoDataFoundException.java"): 
            "public class NoDataFoundException extends RuntimeException {}"
    }

    # Crear archivos base
    for ruta, contenido in archivos_base.items():
        os.makedirs(os.path.dirname(ruta), exist_ok=True)  # Asegurar que la carpeta exista
        with open(ruta, "w") as file:
            file.write(contenido)

    # Crear archivos para cada modelo
    for modelo in modelos:
        modelo_capitalizado = capitalizar_modelo(modelo)  # Asegurar que la primera letra sea mayúscula
        archivos_modelo = {
            os.path.join(ruta_base, f"application/dto/{modelo_capitalizado}Request.java"): f"public class {modelo_capitalizado}Request {{}}",
            os.path.join(ruta_base, f"application/dto/{modelo_capitalizado}Response.java"): f"public class {modelo_capitalizado}Response {{}}",
            os.path.join(ruta_base, f"application/handler/{modelo_capitalizado}Handler.java"): f"public class {modelo_capitalizado}Handler {{}}",
            os.path.join(ruta_base, f"application/handler/I{modelo_capitalizado}Handler.java"): f"public interface I{modelo_capitalizado}Handler {{}}",
            os.path.join(ruta_base, f"application/mapper/{modelo_capitalizado}RequestMapper.java"): f"public class {modelo_capitalizado}RequestMapper {{}}",
            os.path.join(ruta_base, f"application/mapper/{modelo_capitalizado}ResponseMapper.java"): f"public class {modelo_capitalizado}ResponseMapper {{}}",
            os.path.join(ruta_base, f"domain/api/I{modelo_capitalizado}ServicePort.java"): f"public interface I{modelo_capitalizado}ServicePort {{}}",
            os.path.join(ruta_base, f"domain/model/{modelo_capitalizado}.java"): f"public class {modelo_capitalizado} {{}}",
            os.path.join(ruta_base, f"domain/spi/I{modelo_capitalizado}PersistencePort.java"): f"public interface I{modelo_capitalizado}PersistencePort {{}}",
            os.path.join(ruta_base, f"domain/usecase/{modelo_capitalizado}UseCase.java"): f"public class {modelo_capitalizado}UseCase {{}}",
            os.path.join(ruta_base, f"infraestructure/input/rest/{modelo_capitalizado}Controller.java"): f"public class {modelo_capitalizado}Controller {{}}",
            os.path.join(ruta_base, f"infraestructure/output/jpa/adapter/{modelo_capitalizado}JpaAdapter.java"): f"public class {modelo_capitalizado}JpaAdapter {{}}",
            os.path.join(ruta_base, f"infraestructure/output/jpa/entity/{modelo_capitalizado}Entity.java"): f"public class {modelo_capitalizado}Entity {{}}",
            os.path.join(ruta_base, f"infraestructure/output/jpa/mapper/{modelo_capitalizado}EntityMapper.java"): f"public class {modelo_capitalizado}EntityMapper {{}}",
            os.path.join(ruta_base, f"infraestructure/output/jpa/repository/I{modelo_capitalizado}Repository.java"): f"public interface I{modelo_capitalizado}Repository {{}}"
        }

        for ruta, contenido in archivos_modelo.items():
            os.makedirs(os.path.dirname(ruta), exist_ok=True)  # Asegurar que la carpeta exista
            with open(ruta, "w") as file:
                file.write(contenido)

    print(f"\n✅ Estructura generada con éxito en: {ruta_base}\n")


# ==============================
#  SOLICITAR DATOS AL USUARIO
# ==============================
if __name__ == "__main__":
    ruta_base = input("📌 Ingrese la ruta donde desea generar la estructura del proyecto:\nEjemplo: C:\\Users\\TuUsuario\\Documents o /home/tuusuario/proyectos\n: ")
    
    # Validar que la ruta ingresada exista
    while not os.path.exists(ruta_base):
        print("❌ La ruta ingresada no existe. Intente nuevamente.")
        ruta_base = input("📌 Ingrese una ruta válida: ")

    modelos_input = input("📌 Ingrese los modelos a implementar (separados por coma): ")
    modelos_lista = [modelo.strip() for modelo in modelos_input.split(",")]

    # Llamar a la función para generar la estructura en la ruta especificada
    crear_estructura(ruta_base, modelos_lista)
