import graphviz

def cargar_datos_desde_archivo(archivo):
    try:
        with open(archivo, 'r') as file:
            datos = [list(map(float, linea.strip().split(','))) for linea in file.readlines()]
        return datos
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return None

def ingresar_manualmente():
    print("Ingresa manualmente los datos separados por comas (,).")
    print("Para terminar, ingresa 'fin'.")
    columnas = input("Ingrese los nombres de las columnas separados por comas: ").split(',')
    datos = []
    print("Ingrese los datos fila por fila:")
    while True:
        fila = input().strip()
        if fila.lower() == 'fin':
            break
        datos.append([float(x) for x in fila.split(',')])
    return datos

def visualizar_datos(datos):
    print("Los datos son:")
    for fila in datos:
        print(fila)

def generar_matriz_dispersa(datos):
    matriz = [[str(valor) if valor != 0 else '' for valor in fila] for fila in datos]
    return matriz

def visualizar_matriz_dispersa(matriz):
    graph = graphviz.Digraph()
    for i, fila in enumerate(matriz):
        for j, valor in enumerate(fila):
            if valor:
                graph.node(f"{i}_{j}", label=valor)
                if i > 0 and matriz[i-1][j]:
                    graph.edge(f"{i-1}_{j}", f"{i}_{j}")
                if j > 0 and matriz[i][j-1]:
                    graph.edge(f"{i}_{j-1}", f"{i}_{j}")
    graph.render('matriz_dispersa', format='png', cleanup=True)
    print("La representación visual de la matriz dispersa se ha generado como matriz_dispersa.png")

def visualizar_matriz_dispersa_dot(matriz):
    dot_code = 'digraph G {\n'
    for i, fila in enumerate(matriz):
        for j, valor in enumerate(fila):
            if valor:
                dot_code += f'  {i}_{j} [label="{valor}"];\n'
                if i > 0 and matriz[i-1][j]:
                    dot_code += f'  {i-1}_{j} -> {i}_{j};\n'
                if j > 0 and matriz[i][j-1]:
                    dot_code += f'  {i}_{j-1} -> {i}_{j};\n'
    dot_code += '}\n'
    print("El código DOT para la representación visual de la matriz dispersa es:")
    print(dot_code)
    return dot_code

def guardar_grafico_dot(dot_code, nombre_archivo):
    with open(nombre_archivo, 'w') as file:
        file.write(dot_code)
    print(f"El código DOT se ha guardado en '{nombre_archivo}'.")

def main():
    print("Bienvenido al programa de creación de matriz dispersa.")
    while True:
        print("\nOpciones:")
        print("1. Cargar datos desde un archivo")
        print("2. Ingresar datos manualmente")
        print("3. Visualizar datos")
        print("4. Generar matriz dispersa")
        print("5. Visualizar matriz dispersa")
        print("6. Guardar código DOT de la matriz dispersa")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            archivo = input("Ingrese el nombre del archivo CSV: ")
            datos = cargar_datos_desde_archivo(archivo)
            if datos is not None:
                print("Datos cargados exitosamente.")
        elif opcion == '2':
            datos = ingresar_manualmente()
        elif opcion == '3':
            if 'datos' in locals():
                visualizar_datos(datos)
            else:
                print("Primero carga o ingresa los datos.")
        elif opcion == '4':
            if 'datos' in locals():
                matriz_dispersa = generar_matriz_dispersa(datos)
                print("Matriz dispersa generada.")
            else:
                print("Primero carga o ingresa los datos.")
        elif opcion == '5':
            if 'matriz_dispersa' in locals():
                visualizar_matriz_dispersa(matriz_dispersa)
            else:
                print("Primero genera la matriz dispersa.")
        elif opcion == '6':
            if 'matriz_dispersa' in locals():
                dot_code = visualizar_matriz_dispersa_dot(matriz_dispersa)
                nombre_archivo_dot = 'matriz_dispersa.dot'
                guardar_grafico_dot(dot_code, nombre_archivo_dot)
                print("Ahora puedes ejecutar 'dot -Tpng matriz_dispersa.dot -o matriz_dispersa.png' para generar la imagen.")
            else:
                print("Primero genera la matriz dispersa.")
        elif opcion == '7':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()

