# * IMPORTS * #
import time
import xml.etree.ElementTree as ET
from colorama import Fore as Walter
from clases.usuarios import Usuario
from Listas.enlazada.listaEnlazada import ListaEnlazada as LE
from Listas.doble.listaDoble import Lista_Doble as LD
from Listas.circular.listaCircular import listaDobleCircular as LDC

peliculas_fav = []
facturas = []
nombre_sesion = ""

# * MENÚ PRINCIPAL * #
def start_menu():
    print(Walter.WHITE + """
    *===================================*
    |            Bienvenido             |
    |                                   |
    |     1.     Iniciar sesión         |
    |     2.      Registrarse           |
    |     3. Ver listado de películas   |
    |     4.         Salir              |
    *===================================*
    """)

    print(Walter.LIGHTBLUE_EX + "Ingrese el número de la opción que desea:")
    entrada = input(Walter.WHITE + "")
    
    if entrada == "1":
        login_menu()
    elif entrada == "2":
        register_menu()
    elif entrada == "3":
        movie_menu()
    elif entrada == "4":
        exit()
    else:
        print(Walter.RED + "Opción inválida")
        time.sleep(1)
        start_menu()


# * INICIO DE SESIÓN * #
# MENÚ PRINCIPAL - INICIAR SESIÓN #
def login_menu():
    print(Walter.WHITE + """
    *===================================*
    |            Iniciar sesión         |
    |                                   |
    |     1.      Administrador         |
    |     2.         Cliente            |
    |     3.          Atrás             |
    *===================================*
    """)

    print(Walter.LIGHTBLUE_EX + "Ingrese el número de la opción que con la que desea iniciar sesión:")
    entrada_login = input(Walter.WHITE + "")

    if entrada_login == "1" or entrada_login == "2":
        print(Walter.GREEN + "Ingrese su correo electrónico:")
        correo_login = input(Walter.WHITE + "")
        print(Walter.GREEN + "Ingrese su contraseña:")
        contrasena_login = input(Walter.WHITE + "")

        login(correo_login, contrasena_login)

    elif entrada_login == "3":
        start_menu()
    else:
        print(Walter.RED + "Opción inválida")
        time.sleep(1)
        login_menu()

# LOGIN #
def login(correo, contrasena):
    global nombre_sesion
    lista_usuarios = LE()
    lista_usuarios.CargarXML(1)
    user = lista_usuarios.search(correo, contrasena)
    if user is not None:
        if user.rol == "administrador":
            print(Walter.GREEN + "Bienvenido " + Walter.WHITE + user.nombre + " " + user.apellido + Walter.RESET)
            nombre_sesion = user.nombre
            time.sleep(1)
            admin_menu()
        elif user.rol == "cliente":
            print(Walter.GREEN + "Bienvenido " + Walter.WHITE + user.nombre + " " + user.apellido + Walter.RESET)
            nombre_sesion = user.nombre
            time.sleep(1)
            client_menu()
    else:
        print(Walter.RED + "Correo o contraseña incorrectos")
        nombre_sesion = ""
        time.sleep(1)
        login_menu()



# MENÚ PRINCIPAL - INICIAR SESIÓN - ADMINISTRADOR #
def admin_menu():
    global nombre_sesion
    print(Walter.WHITE + """
    *===================================*
    |            Administrador          |
    |                                   |
    |     1.   Gestionar usuarios       |
    |     2.   Gestionar películas      |
    |     3.   Gestionar salas          |
    |     4.          Atrás             |
    *===================================*
    """)

    print(Walter.LIGHTBLUE_EX + "Ingrese el número de la opción que desea:")
    entrada_admin_menu = input(Walter.WHITE + "")

    if entrada_admin_menu == "1":
        gestionar_usuarios_admin_menu()
    elif entrada_admin_menu == "2":
        gestionar_peliculas_admin_menu()
    elif entrada_admin_menu == "3":
        gestionar_salas_admin_menu()
    elif entrada_admin_menu == "4":
        nombre_sesion = ""
        login_menu()
    else:
        print(Walter.RED + "Opción inválida")
        time.sleep(1)
        admin_menu()



# * GESTIÓN DE USUARIOS ADMINISTRADOR * #

# MENÚ PRINCIPAL - INICIAR SESIÓN - ADMINISTRADOR - GESTIONAR USUARIOS #
def gestionar_usuarios_admin_menu():
    print(Walter.WHITE + """
    *===================================*
    |            Administrador          |
    |                                   |
    |     1.      Ver usuarios          |
    |     2.      Agregar usuario       |
    |     3.      Modificar usuario     |
    |     4.      Eliminar usuario      |
    |     5.          Atrás             |
    *===================================*
    """)

    print(Walter.LIGHTBLUE_EX + "Ingrese el número de la opción que desea:")
    entrada_gestionar_usuarios_admin_menu = input(Walter.WHITE + "")
    
    if entrada_gestionar_usuarios_admin_menu == "1":
        ver_usuarios()
    elif entrada_gestionar_usuarios_admin_menu == "2":
        añadir_usuarios()
    elif entrada_gestionar_usuarios_admin_menu == "3":
        modificar_usuarios()
    elif entrada_gestionar_usuarios_admin_menu == "4":
        eliminar_usuarios()
    elif entrada_gestionar_usuarios_admin_menu == "5":
        admin_menu()
    else:
        print(Walter.RED + "Opción inválida")
        time.sleep(1)
        gestionar_usuarios_admin_menu()

# MENÚ PRINCIPAL - INICIAR SESIÓN - ADMINISTRADOR - GESTIONAR USUARIOS - VER USUARIOS #
def ver_usuarios():
    print("Cargando archivo XML...")
    lista = LE()
    lista.CargarXML(1)
    lista.Imprimir()
    print("\n" + Walter.LIGHTGREEN_EX + "Presione enter para regresar")
    input()
    gestionar_usuarios_admin_menu()

# MENÚ PRINCIPAL - INICIAR SESIÓN - ADMINISTRADOR - GESTIONAR USUARIOS - AÑADIR USUARIOS #
def añadir_usuarios():
    print(Walter.GREEN + " Ingrese el rol del usuario")
    print(Walter.GREEN + " 1. Administrador")
    print(Walter.GREEN + " 2. Cliente")
    rol = input(Walter.WHITE + "")
    if rol == "1":
        rol = "administrador"
    elif rol == "2":
        rol = "cliente"
    else:
        print(Walter.RED + "Opción inválida")
        time.sleep(1)
        gestionar_usuarios_admin_menu()

    print(Walter.GREEN + " Ingrese su nombre")
    nombre = input(Walter.WHITE + "")

    print(Walter.GREEN + " Ingrese su apellido")
    apellido = input(Walter.WHITE + "")

    print(Walter.GREEN + " Ingrese su teléfono")
    telefono = input(Walter.WHITE + "")

    print(Walter.GREEN + " Ingrese su correo electrónico")
    correo = input(Walter.WHITE + "")

    print(Walter.GREEN + " Ingrese su contraseña")
    contrasena = input(Walter.WHITE + "")
    
    tree = ET.parse('Archivos de Entrada\\usuarios.xml')
    root = tree.getroot()

    # Crear nuevo usuario
    new_user = ET.SubElement(root, "usuario")

    # Añadir detalles del usuario
    ET.SubElement(new_user, "rol").text = rol
    ET.SubElement(new_user, "nombre").text = nombre
    ET.SubElement(new_user, "apellido").text = apellido
    ET.SubElement(new_user, "telefono").text = telefono
    ET.SubElement(new_user, "correo").text = correo
    ET.SubElement(new_user, "contrasena").text = contrasena

    indent_usuarios(root)

    try:
        tree.write('Archivos de Entrada\\usuarios.xml')
        print(Walter.GREEN + "Usuario registrado con éxito")
    except Exception as e:
        print(Walter.RED + "Error al registrar usuario:")
        print(Walter.WHITE + str(e))

    time.sleep(3)
    gestionar_usuarios_admin_menu()

# MENÚ PRINCIPAL - INICIAR SESIÓN - ADMINISTRADOR - GESTIONAR USUARIOS - MODIFICAR USUARIOS #
def modificar_usuarios():
    print(Walter.GREEN + " Ingrese el correo electrónico del usuario que desea modificar")
    correo = input(Walter.WHITE + "")
    print(Walter.GREEN + " Ingrese el nuevo rol del usuario: ")
    new_rol = input(Walter.WHITE + "")
    print(Walter.GREEN + " Ingrese el nuevo nombre del usuario: ")
    new_nombre = input(Walter.WHITE + "")
    print(Walter.GREEN + " Ingrese el nuevo apellido del usuario: ")
    new_apellido = input(Walter.WHITE + "")
    print(Walter.GREEN + " Ingrese el nuevo teléfono del usuario: ")
    new_telefono = str(input(Walter.WHITE + ""))
    print(Walter.GREEN + " Ingrese la nueva contraseña del usuario: ")
    new_contrasena = input(Walter.WHITE + "")

    lista = LE()
    lista.editarXML(new_rol, new_nombre, new_apellido, new_telefono, correo, new_contrasena)

    print("\n" + Walter.LIGHTGREEN_EX + "Usuario modificado con éxito")

    gestionar_usuarios_admin_menu()

# MENÚ PRINCIPAL - INICIAR SESIÓN - ADMINISTRADOR - GESTIONAR USUARIOS - MODIFICAR USUARIOS #
def eliminar_usuarios():
    print(Walter.GREEN + " Ingrese el correo electrónico del usuario que desea eliminar")
    correo = input(Walter.WHITE + "")

    print(Walter.GREEN + f"¿Está seguro que desea eliminar el usuario asociado al correo {correo}? (s/n)")
    confirmacion = input(Walter.WHITE + "")

    if confirmacion == "s":
        try:
            lista = LE()
            lista.eliminarXML(correo)

            print("\n" + Walter.LIGHTGREEN_EX + "Usuario eliminado con éxito")
            time.sleep(1)
            gestionar_usuarios_admin_menu()
        except Exception as e:
            print(Walter.RED + "Error al eliminar usuario:")
            print(Walter.WHITE + str(e))
            print(Walter.RED + "Regresando al menú principal...")
            time.sleep(3)
            gestionar_usuarios_admin_menu()
    elif confirmacion == "n":
        print(Walter.RED + "Regresando al menú principal...")
        gestionar_usuarios_admin_menu()
    else:
        print(Walter.RED + "Opción inválida")
        time.sleep(1)
        gestionar_usuarios_admin_menu()
    


# * GESTIÓN DE PELÍCULAS ADMINISTRADOR * #

# MENÚ PRINCIPAL - INICIAR SESIÓN - ADMINISTRADOR - GESTIONAR PELÍCULAS #
def gestionar_peliculas_admin_menu():
    print(Walter.WHITE + """
    *===================================*
    |            Administrador          |
    |                                   |
    |     1.      Ver películas         |
    |     2.      Agregar película      |
    |     3.      Modificar película    |
    |     4.      Eliminar película     |
    |     5.          Atrás             |
    *===================================*
    """)

    print(Walter.LIGHTBLUE_EX + "Ingrese el número de la opción que desea:")
    entrada_gestionar_peliculas_admin_menu = input(Walter.WHITE + "")

    if entrada_gestionar_peliculas_admin_menu == "1":
        ver_peliculas()
    elif entrada_gestionar_peliculas_admin_menu == "2":
        agregar_peliculas()
    elif entrada_gestionar_peliculas_admin_menu == "3":
        modificar_peliculas()
    elif entrada_gestionar_peliculas_admin_menu == "4":
        eliminar_peliculas()
    elif entrada_gestionar_peliculas_admin_menu == "5":
        admin_menu()
    else:
        print(Walter.RED + "Opción inválida")
        time.sleep(1)
        gestionar_peliculas_admin_menu()

# MENÚ PRINCIPAL - INICIAR SESIÓN - ADMINISTRADOR - GESTIONAR PELÍCULAS - VER PELÍCULAS #
def ver_peliculas():
    print("Cargando archivo XML...")
    lista_doble_circular = LDC()
    lista_doble_circular.CargarXML_LDC(1)
    lista_doble_circular.Imprimir_LDC()
    print("\n" + Walter.LIGHTGREEN_EX + "Presione enter para regresar")
    input()
    gestionar_peliculas_admin_menu()

# MENÚ PRINCIPAL - INICIAR SESIÓN - ADMINISTRADOR - GESTIONAR PELÍCULAS - AGREGAR PELÍCULAS #
def agregar_peliculas():
    print(Walter.GREEN + "Ingrese la categoría de la película")
    categoria = input(Walter.WHITE + "")
    print(Walter.GREEN + "Ingrese el titulo de la película")
    titulo = input(Walter.WHITE + "")
    print(Walter.GREEN + "Ingrese el director de la película")
    director = input(Walter.WHITE + "")
    print(Walter.GREEN + "Ingrese el año de la película")
    anio = str(input(Walter.WHITE + ""))
    print(Walter.GREEN + "Ingrese la fecha de la función")
    fecha = input(Walter.WHITE + "")
    print(Walter.GREEN + "Ingrese la hora de la función")
    hora = input(Walter.WHITE + "")

    tree = ET.parse('Archivos de Entrada\\peliculas.xml')
    root = tree.getroot()

    elemento_categoria = None

    # Buscar la categoría
    for cat in root.findall('categoria'):
        if cat.find('nombre').text == categoria:
            elemento_categoria = cat
            break

    # Si no existe la categoría, crearla
    if elemento_categoria is None:
        elemento_categoria = ET.SubElement(root, 'categoria')
        ET.SubElement(elemento_categoria, 'nombre').text = categoria
        ET.SubElement(elemento_categoria, 'peliculas')
    
    # Encontrar elementos dentro de la categoría
    elemento_peliculas = elemento_categoria.find('peliculas')

    # Añadir detalles de la película
    elemento_categoria = ET.SubElement(elemento_peliculas, "pelicula")
    ET.SubElement(elemento_categoria, 'titulo').text = titulo
    ET.SubElement(elemento_categoria, 'director').text = director
    ET.SubElement(elemento_categoria, 'anio').text = anio
    ET.SubElement(elemento_categoria, 'fecha').text = fecha
    ET.SubElement(elemento_categoria, 'hora').text = hora

    indent_movies(root)

    try:
        tree.write('Archivos de Entrada\\peliculas.xml')
        print(Walter.GREEN + "Película registrada con éxito")
    except Exception as e:
        print(Walter.RED + "Error al registrar la película:")
        print(Walter.WHITE + str(e))

    time.sleep(3)
    gestionar_peliculas_admin_menu()

# MENÚ PRINCIPAL - INICIAR SESIÓN - ADMINISTRADOR - GESTIONAR PELÍCULAS - MODIFICAR PELÍCULAS #
def modificar_peliculas():
    print(Walter.GREEN + "Ingrese el nombre de la película de la que desea editar la función")
    titulo = input(Walter.WHITE + "")
    print(Walter.GREEN + "Ingrese la nueva fecha de la función")
    new_fecha = input(Walter.WHITE + "")
    print(Walter.GREEN + "Ingrese la nueva hora de la función")
    new_hora = input(Walter.WHITE + "")

    lista = LDC()
    lista.editarXML_LDC(titulo, new_fecha, new_hora)
    print("\n" + Walter.LIGHTGREEN_EX + "Usuario modificado con éxito")

    gestionar_peliculas_admin_menu()

# MENÚ PRINCIPAL - INICIAR SESIÓN - ADMINISTRADOR - GESTIONAR PELÍCULAS - ELIMINAR PELÍCULAS #
def eliminar_peliculas():
    print(Walter.GREEN + "Ingrese el nombre de la película que desea eliminar")
    titulo = input(Walter.WHITE + "")

    print(Walter.GREEN + f"¿Está seguro que desea eliminar {titulo}? (s/n)")
    confirmacion = input(Walter.WHITE + "")

    if confirmacion == "s":
        try:
            lista = LDC()
            lista.eliminarXML_LDC(titulo)
            print("\n" + Walter.LIGHTGREEN_EX + "Película eliminada con éxito")
            print(Walter.LIGHTGREEN_EX + "Regresando al menú principal...")
            time.sleep(1)
            gestionar_peliculas_admin_menu()
        except Exception as e:
            print(Walter.RED + "Error al eliminar la película:")
            print(Walter.WHITE + str(e))
            print(Walter.LIGHTGREEN_EX + "Regresando al menú principal...")
            time.sleep(1)
            gestionar_peliculas_admin_menu()
    elif confirmacion == "n":
        print(Walter.LIGHTGREEN_EX + "Regresando al menú principal...")
        time.sleep(1)
        gestionar_peliculas_admin_menu()
    else:
        print(Walter.RED + "Opción inválida")
        print(Walter.LIGHTGREEN_EX + "Regresando al menú principal...")
        time.sleep(1)
        gestionar_peliculas_admin_menu()



# * GESTIÓN DE SALAS ADMINISTRADOR * #

# MENÚ PRINCIPAL - INICIAR SESIÓN - ADMINISTRADOR - GESTIONAR SALAS #
def gestionar_salas_admin_menu():
    print(Walter.WHITE + """
    *===================================*
    |            Administrador          |
    |                                   |
    |     1.      Ver salas             |
    |     2.      Agregar sala          |
    |     3.      Modificar sala        |
    |     4.      Eliminar sala         |
    |     5.          Atrás             |
    *===================================*
    """)

    print(Walter.LIGHTBLUE_EX + "Ingrese el número de la opción que desea:")
    entrada_gestionar_salas_admin_menu = input(Walter.WHITE + "")

    if entrada_gestionar_salas_admin_menu == "1":
        ver_salas()
    elif entrada_gestionar_salas_admin_menu == "2":
        agregar_sala()
    elif entrada_gestionar_salas_admin_menu == "3":
        modificar_sala()
    elif entrada_gestionar_salas_admin_menu == "4":
        eliminar_sala()
    elif entrada_gestionar_salas_admin_menu == "5":
        admin_menu()
    else:
        print(Walter.RED + "Opción inválida")
        time.sleep(1)
        gestionar_salas_admin_menu()

def ver_salas():
    print("Cargando archivo XML...")
    lista_doble = LD()
    lista_doble.CargarXML_LD(1)
    lista_doble.Imprimir_LD()

    print("\n" + Walter.LIGHTGREEN_EX + "Presione enter para regresar")
    input()
    gestionar_salas_admin_menu()

def agregar_sala():
    print(Walter.GREEN + "Ingrese el número de la sala que desea agregar")
    numero = input(Walter.WHITE + "")
    print(Walter.GREEN + "Ingrese la cantidad de asientos de la sala")
    asientos = str(input(Walter.WHITE + ""))

    tree = ET.parse('Archivos de Entrada\\salas.xml')
    root = tree.getroot()
    
    elemento_salas = root.find('cine/salas')
    new_sala = ET.SubElement(elemento_salas, 'sala')
    ET.SubElement(new_sala, 'numero').text = numero
    ET.SubElement(new_sala, 'asientos').text = asientos

    indent_salas(root)

    try:
        tree.write('Archivos de Entrada\\salas.xml')
        print(Walter.GREEN + "Sala registrada con éxito")
    except Exception as e:
        print(Walter.RED + "Error al registrar la película:")
        print(Walter.WHITE + str(e))

    time.sleep(1)

    gestionar_salas_admin_menu()

def modificar_sala():
    print(Walter.GREEN + "Ingrese el número de la sala que desea modificar")
    numero = input(Walter.WHITE + "")
    print(Walter.GREEN + "Ingrese la nueva cantidad de asientos de la sala")
    asientos = input(Walter.WHITE + "")

    tree = ET.parse('Archivos de Entrada\\salas.xml')
    root = tree.getroot()

    try:
        lista_doble = LD()
        lista_doble.editarXML_LD(numero, asientos)
        print(Walter.GREEN + "Sala modificada con éxito")
    except Exception as e:
        print(Walter.RED + "Error al modificar la sala:")
        print(Walter.WHITE + str(e))

    time.sleep(1)

    gestionar_salas_admin_menu()

def eliminar_sala():
    print(Walter.GREEN + "Ingrese el número de la sala que desea eliminar")
    numero = input(Walter.WHITE + "")

    print(Walter.GREEN + f"¿Está seguro que desea eliminar la sala '{numero}'? (s/n)")
    confirmacion = input(Walter.WHITE + "")

    if confirmacion == "s":
        try:
            lista_doble = LD()
            lista_doble.eliminarXML_LD(numero)

            print("\n" + Walter.LIGHTGREEN_EX + "Sala eliminada con éxito")
            time.sleep(1)
            gestionar_salas_admin_menu()

        except Exception as e:
            print(Walter.RED + "Error al eliminar la sala:")
            print(Walter.WHITE + str(e))
            print(Walter.RED + "Regresando al menú...")
            gestionar_salas_admin_menu()

    elif confirmacion == "n":
        print(Walter.RED + "Regresando al menú...")
        gestionar_salas_admin_menu()

    else:
        print(Walter.RED + "Opción inválida")
        print(Walter.RED + "Regresando al menú...")
        gestionar_salas_admin_menu()






# * MENÚ DE CLIENTE * #

# MENÚ PRINCIPAL - INICIAR SESIÓN - CLIENTE #
def client_menu():
    global nombre_sesion
    print(Walter.WHITE + """
    *===================================*
    |               Cliente             |
    |                                   |
    |     1.   Ver listado películas    |
    |     2.    Películas favoritas     |
    |     3.      Comprar boletos       |
    |     4.    Historial de compras    |
    |     5.          Atrás             |
    *===================================*
    """)

    print(Walter.LIGHTBLUE_EX + "Ingrese el número de la opción que desea:")
    entrada_client_menu = input(Walter.WHITE + "")

    if entrada_client_menu == "1":
        ver_peliculas_user_menu()
    elif entrada_client_menu == "2":
        peliculas_favoritas_user()
    elif entrada_client_menu == "3":
        comprar_boletos()
    elif entrada_client_menu == "4":
        historial_facturas()
    elif entrada_client_menu == "5":
        nombre_sesion = ""
        login_menu()
    else:
        print(Walter.RED + "Opción inválida")
        time.sleep(1)
        client_menu()

def ver_peliculas_user_menu():
    lista_doble_circular = LDC()
    lista_doble_circular.CargarXML_LDC(1)
    lista_doble_circular.Imprimir_LDC()
    print("\n" + Walter.LIGHTGREEN_EX + "Presione enter para regresar")
    input()
    client_menu()

def peliculas_favoritas_user():
    global nombre_sesion
    global peliculas_fav
    print(Walter.WHITE + """
    *===================================*
    |               Cliente             |
    |                                   |
    |     1.    Películas favoritas     |
    |     2.     Agregar películas      |
    |     3.          Atrás             |
    *===================================*
    """)

    print(Walter.LIGHTBLUE_EX + "Ingrese el número de la opción que desea:")
    entrada_peliculas_favoritas_user = input(Walter.WHITE + "")

    if entrada_peliculas_favoritas_user == "1":
        for i in peliculas_fav:
            if i[1] == nombre_sesion:
                print(Walter.WHITE + i[0])
        print("\n" + Walter.LIGHTGREEN_EX + "Presione enter para regresar")
        input()
        peliculas_favoritas_user()
    elif entrada_peliculas_favoritas_user == "2":
        print(Walter.CYAN + """
    ========================= LISTADO DE PELÍCULAS =========================""")

        lista_circular = LDC()
        lista_circular.CargarXML_LDC(1)
        lista_circular.Imprimir_LDC()

        print(Walter.GREEN + "Ingrese el nombre de la película que desea agregar a favoritos")
        pelicula = input(Walter.WHITE + "")

        lista_circular.search(pelicula)
        
        obj_pelicula_fav = (pelicula, nombre_sesion)
        peliculas_fav.append(obj_pelicula_fav)
        peliculas_favoritas_user()
    elif entrada_peliculas_favoritas_user == "3":
        print(Walter.RED + "Regresando al menú...")
        time.sleep(1)
        client_menu()
    else:
        print(Walter.RED + "Opción inválida")
        time.sleep(1)
        peliculas_favoritas_user()
        

def comprar_boletos():
    global nombre_sesion
    global facturas
    print(Walter.CYAN + """
    ========================= LISTADO DE PELÍCULAS =========================""")

    lista_circular = LDC()
    lista_circular.CargarXML_LDC(1)
    lista_circular.Imprimir_LDC()

    print(Walter.GREEN + "Ingrese el nombre de la película para la que desea comprar boletos")
    input_pelicula = input(Walter.WHITE + "")

    pelicula = lista_circular.search(input_pelicula)

    if pelicula != None:
        titulo = pelicula.titulo
        fecha = pelicula.fecha
        hora = pelicula.hora

        print(Walter.CYAN + "Película: " + Walter.WHITE + titulo +
              Walter.CYAN +" Fecha: " + Walter.WHITE + hora +
              Walter.CYAN + " Hora: " + Walter.WHITE + fecha) 

        time.sleep(1)

        print(Walter.GREEN + "Ingrese la cantidad de boletos que desea comprar")
        cantidad_boletos = input(Walter.WHITE + "")

        lista_doble = LD()
        lista_doble.CargarXML_LD(1)
        lista_doble.Imprimir_LD()

        print(Walter.GREEN + "Ingrese el número de la sala en la que desea comprar los boletos")
        numero_sala = input(Walter.WHITE + "")

        sala = lista_doble.search(numero_sala)

        if sala != None:
            print(Walter.CYAN + "Sala: " + Walter.WHITE + numero_sala +
                  Walter.CYAN + " Asientos: " + Walter.WHITE + sala.asientos)

            time.sleep(1)

            print(Walter.GREEN + "Ingrese el número de sus asientos")
            numero_asientos = input(Walter.WHITE + "")

            if int(numero_asientos) < int(sala.asientos):
                monto_total = int(cantidad_boletos) * 42

                print(Walter.CYAN + "Monto total: " + Walter.WHITE + str(monto_total))
                print(Walter.GREEN + "¿Desea ingresar datos de factura? (s/n)")
                input_factura = input(Walter.WHITE + "")

                if input_factura.lower() == "s":
                    nombre_cliente = nombre_sesion
                    print(Walter.GREEN + "Ingrese su NIT")
                    nit_cliente = input(Walter.WHITE + "")
                    print(Walter.GREEN + "Ingrese su dirección")
                    direccion_cliente = input(Walter.WHITE + "")

                    obj_factura = (nombre_cliente, nit_cliente, direccion_cliente, titulo, fecha, hora, numero_sala, numero_asientos, monto_total)
                    facturas.append(obj_factura)

                    print("")
                    print(Walter.LIGHTGREEN_EX + "Factura generada con éxito")
                    print(Walter.LIGHTGREEN_EX + "--------------------------")
                    print(Walter.LIGHTGREEN_EX + "Nombre: " + Walter.WHITE + nombre_cliente)
                    print(Walter.LIGHTGREEN_EX + "NIT: " + Walter.WHITE + nit_cliente)
                    print(Walter.LIGHTGREEN_EX + "Dirección: " + Walter.WHITE + direccion_cliente)
                    print(Walter.LIGHTGREEN_EX + "Película: " + Walter.WHITE + titulo)
                    print(Walter.LIGHTGREEN_EX + "Fecha: " + Walter.WHITE + fecha)
                    print(Walter.LIGHTGREEN_EX + "Hora: " + Walter.WHITE + hora)
                    print(Walter.LIGHTGREEN_EX + "Sala: " + Walter.WHITE + numero_sala)
                    print(Walter.LIGHTGREEN_EX + "Asientos: " + Walter.WHITE + numero_asientos)
                    print(Walter.LIGHTGREEN_EX + "Monto total: " + Walter.WHITE + "Q." + str(monto_total))
                    print("")
                    print(Walter.LIGHTGREEN_EX + "Presione enter para regresar")
                    input()
                    client_menu()
                elif input_factura.lower() == "n":
                    obj_factura = (nombre_sesion, "CF", "CF", titulo, fecha, hora, numero_sala, numero_asientos, monto_total)
                    facturas.append(obj_factura)

                    print(Walter.LIGHTGREEN_EX + "Factura generada con éxito")
                    print(Walter.LIGHTGREEN_EX + "Nombre: " + Walter.WHITE + nombre_sesion)
                    print(Walter.LIGHTGREEN_EX + "NIT: " + Walter.WHITE + "CF")
                    print(Walter.LIGHTGREEN_EX + "Dirección: " + Walter.WHITE + "CF")
                    print(Walter.LIGHTGREEN_EX + "Película: " + Walter.WHITE + titulo)
                    print(Walter.LIGHTGREEN_EX + "Fecha: " + Walter.WHITE + fecha)
                    print(Walter.LIGHTGREEN_EX + "Hora: " + Walter.WHITE + hora)
                    print(Walter.LIGHTGREEN_EX + "Sala: " + Walter.WHITE + numero_sala)
                    print(Walter.LIGHTGREEN_EX + "Asientos: " + Walter.WHITE + numero_asientos)
                    print(Walter.LIGHTGREEN_EX + "Monto total: " + Walter.WHITE + "Q." + str(monto_total))

                    print(Walter.LIGHTGREEN_EX + "Presione enter para regresar")
                    input()
                    client_menu()
                else:
                    print(Walter.RED + "Opción inválida")
                    time.sleep(1)
                    client_menu()
            else:
                print(Walter.RED + "Número de asientos fuera del rango")
                time.sleep(1)
                client_menu()
        else:
            print(Walter.RED + "Sala no encontrada")
            time.sleep(1)
            client_menu()
    else:
        print(Walter.RED + "Película no encontrada")
        time.sleep(1)
        client_menu()

def historial_facturas():
    print(Walter.GREEN + "=============== HISTORIAL DE FACTURAS ===============")
    for i in facturas:
        if i[0] == nombre_sesion:
            print(Walter.LIGHTGREEN_EX + "Nombre: " + Walter.WHITE + i[0])
            print(Walter.LIGHTGREEN_EX + "NIT: " + Walter.WHITE + i[1])
            print(Walter.LIGHTGREEN_EX + "Dirección: " + Walter.WHITE + i[2])
            print(Walter.LIGHTGREEN_EX + "Película: " + Walter.WHITE + i[3])
            print(Walter.LIGHTGREEN_EX + "Fecha: " + Walter.WHITE + i[4])
            print(Walter.LIGHTGREEN_EX + "Hora: " + Walter.WHITE + i[5])
            print(Walter.LIGHTGREEN_EX + "Sala: " + Walter.WHITE + i[6])
            print(Walter.LIGHTGREEN_EX + "Asientos: " + Walter.WHITE + i[7])
            print(Walter.LIGHTGREEN_EX + "Monto total: " + Walter.WHITE + "Q." + str(i[8]))
            print(Walter.LIGHTGREEN_EX + "=======================================")

    print(Walter.GREEN + "Presione enter para regresar")
    input()
    client_menu()





# * REGISTRAR NUEVO USUARIO * #

# MENÚ PRINCIPAL - REGISTRARSE #
def register_menu():
    print(Walter.WHITE + """
    *===================================*
    |              Registro             |
    *-----------------------------------*
    |    Presione enter para continuar  |
    |       Ingrese 1 para regresar     |
    *===================================*
    """)

    entrada_registro = input("")
    if entrada_registro == "":
        register_form()
    elif entrada_registro == "1":
        start_menu()
    else:
        print(Walter.RED + "Opción inválida")
        time.sleep(1)
        register_menu()

# FORMULARIO DE REGISTRO #
def register_form():
    rol = "cliente"
    print(Walter.GREEN + " Ingrese su nombre")
    nombre = input(Walter.WHITE + "")
    print(Walter.GREEN + " Ingrese su apellido")
    apellido = input(Walter.WHITE + "")
    print(Walter.GREEN + " Ingrese su teléfono")
    telefono = input(Walter.WHITE + "")
    print(Walter.GREEN + " Ingrese su correo electrónico")
    correo = input(Walter.WHITE + "")
    print(Walter.GREEN + " Ingrese su contraseña")
    contrasena = input(Walter.WHITE + "")
    
    tree = ET.parse('Archivos de Entrada\\usuarios.xml')
    root = tree.getroot()

    # Crear nuevo usuario
    new_user = ET.SubElement(root, "usuario")

    # Añadir detalles del usuario
    ET.SubElement(new_user, "rol").text = rol
    ET.SubElement(new_user, "nombre").text = nombre
    ET.SubElement(new_user, "apellido").text = apellido
    ET.SubElement(new_user, "telefono").text = telefono
    ET.SubElement(new_user, "correo").text = correo
    ET.SubElement(new_user, "contrasena").text = contrasena

    indent_usuarios(root)

    try:
        tree.write('Archivos de Entrada\\usuarios.xml')
        print(Walter.GREEN + "Usuario registrado con éxito")
    except Exception as e:
        print(Walter.RED + "Error al registrar usuario:")
        print(Walter.WHITE + str(e))

    time.sleep(3)
    start_menu()



# * TABULACIÓN DE ARCHIVOS XML * #
# Tabulación de XML Usuarios #
def indent_usuarios(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent_usuarios(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

# Tabulación de XML Películas #
def indent_movies(elem, level=0):
        i = "\n" + level*"  "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "  "
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                indent_movies(elem, level+1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i

# Tabulación de XML salas #
def indent_salas(elem, level=0):
        i = "\n" + level*"  "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "  "
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                indent_salas(elem, level+1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i



# MENÚ PRINCIPAL - LISTADO DE PELÍCULAS #
def movie_menu():
    print(Walter.WHITE + """
    *===================================*
    |         Listado de películas      |
    |                                   |
    |     1.    Listado general         |
    |     2.    Listado por categoría   |
    |     3.          Atrás             |
    *===================================*
    """)
    
    print(Walter.LIGHTBLUE_EX + "Ingrese el número de la opción que desea:")
    entrada_movie_list = input(Walter.WHITE + "")

    if entrada_movie_list == "1":
        ver_peliculas_main_menu()
    elif entrada_movie_list == "2":
        ver_listado_categorias()
    elif entrada_movie_list == "3":
        start_menu()
    else:
        print(Walter.RED + "Opción inválida")
        time.sleep(1)
        movie_menu()

def ver_peliculas_main_menu():
    lista_doble_circular = LDC()
    lista_doble_circular.CargarXML_LDC(1)
    lista_doble_circular.Imprimir_LDC()
    print("\n" + Walter.LIGHTGREEN_EX + "Presione enter para regresar")
    input()
    movie_menu()

def ver_listado_categorias():
    lista_doble_circular = LDC()
    lista_doble_circular.show_categorias()
    print(Walter.GREEN + "Ingrese el número de la categoría que desea ver: ")
    indice = input(Walter.WHITE + "")
    
    if indice.isdigit():
        indice = int(indice)
        lista_doble_circular.show_peliculas(indice)
    else:
        print(Walter.RED + "Opción inválida")
        time.sleep(1)
        movie_menu()

    print("\n" + Walter.LIGHTGREEN_EX + "Presione enter para regresar")
    input()
    movie_menu()
    

# INICIO #
start_menu()