class Curso:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre
        self.alumnos = []
        self.profesores = []

    def agregar_alumno(self, alumno):
        self.alumnos.append(alumno)

    def agregar_profesor(self, profesor):
        self.profesores.append(profesor)

    def promedio_notas(self):
        if not self.alumnos:
            return 0
        total_notas = sum(alumno.nota for alumno in self.alumnos)
        return total_notas / len(self.alumnos)

    def clasificar_alumnos(self):
        clasificacion = {'aprobados': [], 'aplazados': [], 'reprobados': []}
        for alumno in self.alumnos:
            if alumno.nota > 70:
                clasificacion['aprobados'].append(alumno)
            elif 60 <= alumno.nota <= 69:
                clasificacion['aplazados'].append(alumno)
            else:
                clasificacion['reprobados'].append(alumno)
        return clasificacion

    def alumnos_sobre_promedio(self):
        promedio = self.promedio_notas()
        return len([alumno for alumno in self.alumnos if alumno.nota > promedio])


class Alumno:
    def __init__(self, nombre, cedula, nota):
        self.nombre = nombre
        self.cedula = cedula
        self.nota = nota


class Profesor:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula



cursos = {}

# Funciones para agregar cursos alumnos profesores
def agregar_curso():
    codigo = input("Ingrese el código del curso: ")
    nombre = input("Ingrese el nombre del curso: ")
    cursos[codigo] = Curso(codigo, nombre)
    print(f"Curso '{nombre}' agregado exitosamente.\n")

def agregar_alumno():
    nombre = input("Ingrese el nombre del alumno: ")
    cedula = input("Ingrese la cédula del alumno: ")
    curso_codigo = input("Ingrese el código del curso: ")

    if curso_codigo not in cursos:
        print(f"Error: El curso '{curso_codigo}' no existe.\n")
        return

    try:
        nota = float(input("Ingrese la nota del alumno: "))
    except ValueError:
        print("Error: La nota debe ser un número.\n")
        return

    alumno = Alumno(nombre, cedula, nota)
    cursos[curso_codigo].agregar_alumno(alumno)
    print(f"Alumno '{nombre}' agregado exitosamente.\n")

def agregar_profesor():
    nombre = input("Ingrese el nombre del profesor: ")
    cedula = input("Ingrese la cédula del profesor: ")
    curso_codigo = input("Ingrese el código del curso: ")

    if curso_codigo not in cursos:
        print(f"Error: El curso '{curso_codigo}' no existe.\n")
        return

    profesor = Profesor(nombre, cedula)
    cursos[curso_codigo].agregar_profesor(profesor)
    print(f"Profesor '{nombre}' agregado exitosamente.\n")

# Menú
while True:
    print("\nMenú:")
    print("1. Agregar curso")
    print("2. Agregar alumno")
    print("3. Agregar profesor")
    print("4. Mostrar lista de alumnos")
    print("5. Mostrar promedio de notas")
    print("6. Mostrar clasificación de alumnos")
    print("7. Mostrar alumnos sobre el promedio")
    print("8. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_curso()
    elif opcion == "2":
        agregar_alumno()
    elif opcion == "3":
        agregar_profesor()
    elif opcion == "4":
        curso_codigo = input("Ingrese el código del curso: ")
        if curso_codigo in cursos:
            print("Lista de alumnos:", [alumno.nombre for alumno in cursos[curso_codigo].alumnos])
        else:
            print("Error: El curso no existe.\n")
    elif opcion == "5":
        curso_codigo = input("Ingrese el código del curso: ")
        if curso_codigo in cursos:
            print("Promedio de notas:", cursos[curso_codigo].promedio_notas())
        else:
            print("Error: El curso no existe.\n")
    elif opcion == "6":
        curso_codigo = input("Ingrese el código del curso: ")
        if curso_codigo in cursos:
            print("Clasificación de alumnos:", cursos[curso_codigo].clasificar_alumnos())
        else:
            print("Error: El curso no existe.\n")
    elif opcion == "7":
        curso_codigo = input("Ingrese el código del curso: ")
        if curso_codigo in cursos:
            print("Alumnos con nota sobre el promedio:", cursos[curso_codigo].alumnos_sobre_promedio())
        else:
            print("Error: El curso no existe.\n")
    elif opcion == "8":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida, intente nuevamente.")
        
