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
        os.path.join(base_path, f"Ms{proyecto.capitalize()}Application.java"): 
            "public class MsApplication { public static void main(String[] args) {} }",
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
        archivos_modelo = {
            os.path.join(base_path, f"application/dto/{modelo}Request.java"): f"public class {modelo}Request {{}}",
            os.path.join(base_path, f"application/dto/{modelo}Response.java"): f"public class {modelo}Response {{}}",
            os.path.join(base_path, f"application/handler/{modelo}Handler.java"): f"public class {modelo}Handler {{}}",
            os.path.join(base_path, f"application/handler/I{modelo}Handler.java"): f"public interface I{modelo}Handler {{}}",
            os.path.join(base_path, f"application/mapper/{modelo}RequestMapper.java"): f"public class {modelo}RequestMapper {{}}",
            os.path.join(base_path, f"application/mapper/{modelo}ResponseMapper.java"): f"public class {modelo}ResponseMapper {{}}",
            os.path.join(base_path, f"domain/api/I{modelo}ServicePort.java"): f"public interface I{modelo}ServicePort {{}}",
            os.path.join(base_path, f"domain/model/{modelo}.java"): f"public class {modelo} {{}}",
            os.path.join(base_path, f"domain/spi/I{modelo}PersistencePort.java"): f"public interface I{modelo}PersistencePort {{}}",
            os.path.join(base_path, f"domain/usecase/{modelo}UseCase.java"): f"public class {modelo}UseCase {{}}",
            os.path.join(base_path, f"infraestructure/input/rest/{modelo}Controller.java"): f"public class {modelo}Controller {{}}",
            os.path.join(base_path, f"infraestructure/output/jpa/adapter/{modelo}JpaAdapter.java"): f"public class {modelo}JpaAdapter {{}}",
            os.path.join(base_path, f"infraestructure/output/jpa/entity/{modelo}Entity.java"): f"public class {modelo}Entity {{}}",
            os.path.join(base_path, f"infraestructure/output/jpa/mapper/{modelo}EntityMapper.java"): f"public class {modelo}EntityMapper {{}}",
            os.path.join(base_path, f"infraestructure/output/jpa/repository/I{modelo}Repository.java"): f"public interface I{modelo}Repository {{}}"
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
