import os

# ==============================
#  HEXAGONAL PROJECT GENERATOR
# ==============================

print("\n")
print("               █████╗ ██████╗  ██████╗██╗  ██╗     ")
print("  *******     ██╔══██╗██╔══██╗██╔════╝██║  ██║     ")
print(" *********    ███████║██████╔╝██║     ███████║     ")
print(" *********    ██╔══██║██╔══██╗██║     ██╔══██║     ")
print("  *******     ██║  ██║██║  ██║╚██████╗██║  ██║     ")
print("              ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝     ")
print("             ARCH - HEXAGONAL PROJECT GENERATOR    ")
print("\n")


def capitalizar_modelo(modelo):
    """ Capitaliza la primera letra del modelo si no está en mayúsculas """
    return modelo[:1].upper() + modelo[1:]


def crear_estructura(proyecto, modelos):
    base_path = os.path.join(os.getcwd(), proyecto)
    
    # Crear la carpeta base del proyecto si no existe
    os.makedirs(base_path, exist_ok=True)

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
        os.makedirs(os.path.join(base_path, carpeta), exist_ok=True)

    # Archivos base (corregida la ruta)
    archivos_base = {
        os.path.join(base_path, "infraestructure/configuration/BeanConfiguration.java"): 
            "public class BeanConfiguration {}",
        os.path.join(base_path, "infraestructure/exception/NoDataFoundException.java"): 
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
            os.path.join(base_path, f"application/dto/{modelo_capitalizado}Request.java"): f"public class {modelo_capitalizado}Request {{}}",
            os.path.join(base_path, f"application/dto/{modelo_capitalizado}Response.java"): f"public class {modelo_capitalizado}Response {{}}",
            os.path.join(base_path, f"application/handler/{modelo_capitalizado}Handler.java"): f"public class {modelo_capitalizado}Handler {{}}",
            os.path.join(base_path, f"application/handler/I{modelo_capitalizado}Handler.java"): f"public interface I{modelo_capitalizado}Handler {{}}",
            os.path.join(base_path, f"application/mapper/{modelo_capitalizado}RequestMapper.java"): f"public class {modelo_capitalizado}RequestMapper {{}}",
            os.path.join(base_path, f"application/mapper/{modelo_capitalizado}ResponseMapper.java"): f"public class {modelo_capitalizado}ResponseMapper {{}}",
            os.path.join(base_path, f"domain/api/I{modelo_capitalizado}ServicePort.java"): f"public interface I{modelo_capitalizado}ServicePort {{}}",
            os.path.join(base_path, f"domain/model/{modelo_capitalizado}.java"): f"public class {modelo_capitalizado} {{}}",
            os.path.join(base_path, f"domain/spi/I{modelo_capitalizado}PersistencePort.java"): f"public interface I{modelo_capitalizado}PersistencePort {{}}",
            os.path.join(base_path, f"domain/usecase/{modelo_capitalizado}UseCase.java"): f"public class {modelo_capitalizado}UseCase {{}}",
            os.path.join(base_path, f"infraestructure/input/rest/{modelo_capitalizado}Controller.java"): f"public class {modelo_capitalizado}Controller {{}}",
            os.path.join(base_path, f"infraestructure/output/jpa/adapter/{modelo_capitalizado}JpaAdapter.java"): f"public class {modelo_capitalizado}JpaAdapter {{}}",
            os.path.join(base_path, f"infraestructure/output/jpa/entity/{modelo_capitalizado}Entity.java"): f"public class {modelo_capitalizado}Entity {{}}",
            os.path.join(base_path, f"infraestructure/output/jpa/mapper/{modelo_capitalizado}EntityMapper.java"): f"public class {modelo_capitalizado}EntityMapper {{}}",
            os.path.join(base_path, f"infraestructure/output/jpa/repository/I{modelo_capitalizado}Repository.java"): f"public interface I{modelo_capitalizado}Repository {{}}"
        }

        for ruta, contenido in archivos_modelo.items():
            os.makedirs(os.path.dirname(ruta), exist_ok=True)  # Asegurar que la carpeta exista
            with open(ruta, "w") as file:
                file.write(contenido)

    print(f"\n✅ Estructura del proyecto '{proyecto}' creada con éxito!\n")


# ==============================
#  SOLICITAR DATOS AL USUARIO
# ==============================
if __name__ == "__main__":
    nombre_proyecto = input("📌 Ingrese el nombre del proyecto: ")
    modelos_input = input("📌 Ingrese los modelos a implementar (separados por coma): ")
    modelos_lista = [modelo.strip() for modelo in modelos_input.split(",")]

    # Llamar a la función para generar la estructura
    crear_estructura(nombre_proyecto, modelos_lista)
