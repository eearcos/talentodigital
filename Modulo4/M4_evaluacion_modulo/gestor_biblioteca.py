import os

class Libro:
    def __init__(self, titulo, autor, anio):
        self._titulo = titulo
        self._autor = autor
        self._anio = anio
        self._estado = "disponible" 

    def get_titulo(self):
        return self._titulo

    def get_estado(self):
        return self._estado

    def set_estado(self, nuevo_estado):
        self._estado = nuevo_estado

    def __str__(self):
        return f"[Físico] Título: {self._titulo} | Autor: {self._autor} | Año: {self._anio} | Estado: {self._estado.upper()}"

class LibroDigital(Libro):
    """Herencia: Clase hija que hereda de Libro"""
    def __init__(self, titulo, autor, anio, formato):
        super().__init__(titulo, autor, anio)
        self._formato = formato

    def __str__(self):
        return f"[Digital] Título: {self._titulo} | Autor: {self._autor} | Año: {self._anio} | Formato: {self._formato} | Estado: {self._estado.upper()}"
    
    def get_formato(self):
        return self._formato
    
class Biblioteca:
    def __init__(self):
        self.lista_libros = []
        self.nombre_archivo = "biblioteca.txt"
        self.cargar_datos()

    def agregar_libro(self, libro):
        self.lista_libros.append(libro)
        print(f"Libro '{libro.get_titulo()}' agregado con éxito.")
        self.guardar_datos()

    def listar_libros(self):
        print("\n--- 📚 LISTA DE LIBROS ---")
        if not self.lista_libros:
            print("(No hay libros registrados)")
        for libro in self.lista_libros:
            print(libro)

    def buscar_libro(self, titulo_buscado):
        encontrado = False
        for libro in self.lista_libros:
            if libro.get_titulo().lower() == titulo_buscado.lower():
                print("\n🔎 Libro Encontrado:")
                print(libro)
                encontrado = True
                break
        if not encontrado:
            print("No se encontró ningún libro con ese título.")

    def cambiar_estado_libro(self, titulo, nuevo_estado):
        """Maneja tanto el préstamo como la devolución"""
        try:
            libro_encontrado = None
            for libro in self.lista_libros:
                if libro.get_titulo().lower() == titulo.lower():
                    libro_encontrado = libro
                    break
            
            if not libro_encontrado:
                raise ValueError("El libro no existe en la biblioteca.")

            if libro_encontrado.get_estado() == nuevo_estado:
                raise Exception(f"El libro ya está en estado '{nuevo_estado}'.")

            libro_encontrado.set_estado(nuevo_estado)
            accion = "prestado" if nuevo_estado == "prestado" else "devuelto"
            print(f"Libro marcado como {accion} exitosamente.")
            self.guardar_datos()

        except (ValueError, Exception) as e:
            print(f"Error: {e}")

    def eliminar_libro(self, titulo):
        try:
            libro_a_borrar = None
            for libro in self.lista_libros:
                if libro.get_titulo().lower() == titulo.lower():
                    libro_a_borrar = libro
                    break
            
            if libro_a_borrar:
                self.lista_libros.remove(libro_a_borrar)
                print(f"🗑️ Libro '{titulo}' eliminado.")
                self.guardar_datos()
            else:
                print("No se encontró el libro para eliminar.")
        except Exception as e:
            print(f"Error inesperado: {e}")

    # --- PERSISTENCIA (ARCHIVOS) ---

    def guardar_datos(self):
        """Guarda en formato: TIPO,TITULO,AUTOR,ANIO,ESTADO,FORMATO_SI_APLICA"""
        with open(self.nombre_archivo, "w", encoding="utf-8") as f:
            for l in self.lista_libros:
                tipo = "D" if isinstance(l, LibroDigital) else "F"
                extra = l.get_formato() if tipo == "D" else "N/A"
                linea = f"{tipo}::{l.get_titulo()}::{l._autor}::{l._anio}::{l.get_estado()}::{extra}\n"
                f.write(linea)

    def cargar_datos(self):
        if not os.path.exists(self.nombre_archivo):
            return
        try:
            with open(self.nombre_archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    datos = linea.strip().split("::")
                    if len(datos) >= 5:
                        tipo, titulo, autor, anio, estado, extra = datos
                        
                        if tipo == "D":
                            nuevo_libro = LibroDigital(titulo, autor, int(anio), extra)
                        else:
                            nuevo_libro = Libro(titulo, autor, int(anio))
                        
                        nuevo_libro.set_estado(estado)
                        self.lista_libros.append(nuevo_libro)
        except Exception as e:
            print("Error al cargar archivo. Se iniciará una biblioteca nueva.")

def main():
    biblio = Biblioteca()
    
    while True:
        print("\n" + "="*30)
        print("   GESTOR DE BIBLIOTECA")
        print("="*30)
        print("1. Agregar libro")
        print("2. Eliminar libro")
        print("3. Ver todos los libros")
        print("4. Buscar libro")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Salir")
        
        opcion = input("\n Elige una opción: ")

        if opcion == "1":
            tipo = input("¿Es libro digital? (s/n): ").lower()
            tit = input("Título: ")
            aut = input("Autor: ")
            ani = input("Año: ")
            
            if tipo == "s":
                fmt = input("Formato (PDF/ePub): ")
                biblio.agregar_libro(LibroDigital(tit, aut, ani, fmt))
            else:
                biblio.agregar_libro(Libro(tit, aut, ani))

        elif opcion == "2":
            tit = input("Título a eliminar: ")
            biblio.eliminar_libro(tit)

        elif opcion == "3":
            biblio.listar_libros()

        elif opcion == "4":
            tit = input("Título a buscar: ")
            biblio.buscar_libro(tit)

        elif opcion == "5":
            tit = input("Título a prestar: ")
            biblio.cambiar_estado_libro(tit, "prestado")

        elif opcion == "6":
            tit = input("Título a devolver: ")
            biblio.cambiar_estado_libro(tit, "disponible")

        elif opcion == "7":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()