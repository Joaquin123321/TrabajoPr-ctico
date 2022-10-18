from datetime import datetime
import sqlite3 as sql
from datetime import date

class Conexiones:
    
    def abrirConexion(self):
        self.conexion = sql.connect("DBTrabajoPráctico.db")
        self.puntero = self.conexion.cursor()
        
    def cerrarConexion(self):
        self.conexion.close() 

class ProgramaPrincipal:

    def crearTabla(self, comandoSQL: str):
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.puntero.execute(comandoSQL)
        conexion.conexion.commit()
        conexion.cerrarConexion()
        
        
    def menu(self):
        while True:
            print("Sistema de ventas de Monopatines Eléctricos")
            print("---" * 30)
            print("1- Cargar un monopatín")
            print("2- Modificar el precio de un monopatín")
            print("3- Borrar un monopatín")
            print("4- Cargar disponibilidad")
            print("5- Listado de productos")
            print("6- Agregar datos del monopatín")
            print("7- Actualizar precios y fechas")
            print("8- Mostrar registros anteriores")
            print("0- Salir del menú")
            
            while True:
                    try:
                        opcion = int(input("Por favor, ingrese una opción: "))
                        break
                    except ValueError:
                        print("Se debe ingresar una opción válida")

            if (opcion == 1):
                while True:
                    try:
                        marca = str(input("Por favor, ingrese la marca del monopatín: "))
                        break
                    except ValueError:
                        print("Se debe ingresar un texto")
    
                while True:
                    try:
                        precio = float(input("Por favor, ingrese el precio del monopatín: "))
                        break
                    except ValueError:
                        print("Se debe ingresar un número")
                
                while True:
                    try:
                        cantidadDisponibles = int(input("Por favor, ingrese la cantidad de monopatines: "))
                        break
                    except ValueError:
                        print("Se debe ingresar un número entero")
                
                
                nuevo_monopatin = monopatin(marca, precio, cantidadDisponibles)
                nuevo_monopatin.cargar_monopatin()
            
            if (opcion == 2):
                while True:
                    try:
                        marca = str(input("Por favor, ingrese la marca del monopatín: "))
                        break
                    except ValueError:
                        print("Se debe ingresar un texto")
                while True:
                    try:
                        precio = float(input("Por favor, ingrese el precio del monopátin: "))
                        break
                    except ValueError:
                        print("Se debe ingresar un número")
                
                conexion = Conexiones()
                conexion.abrirConexion()
        
                try:
                    conexion.puntero.execute("UPDATE DATOS SET precio='{}' WHERE marca='{}'" .format(precio, marca))
                    conexion.puntero.execute("UPDATE MONOPATIN SET precio='{}' WHERE marca='{}'" .format(precio, marca))
                    conexion.conexion.commit()
                    print("El precio se actualizó correctamente")
                except:
                    print("No se pudo actualizar el precio")
                finally:
                    conexion.cerrarConexion()

            if (opcion == 3):
                while True:
                    try:
                        marca = str(input("Por favor, ingrese la marca del monopatín: "))
                        break
                    except ValueError:
                        print("Se debe ingresar un texto")
                
                conexion = Conexiones()
                conexion.abrirConexion()

                try:
                    conexion.puntero.execute("DELETE FROM DATOS WHERE marca='{}'" .format(marca))
                    conexion.puntero.execute("DELETE FROM MONOPATIN WHERE marca='{}'" .format(marca))
                    conexion.conexion.commit()
                    print("El monopatín se eliminó correctamente")
                except:
                    print("No se pudo eliminar el monopatín")
                finally:
                    conexion.cerrarConexion()
            
            if (opcion == 4):
                while True:
                    try:
                        marca = str(input("Por favor, ingrese la marca del monopatín: "))
                        break
                    except ValueError:
                        print("Se debe ingresar un texto")

                while True:
                    try:
                        cantidadDisponibles = int(input("Por favor, ingrese la cantidad de monopatines: "))
                        break
                    except ValueError:
                        print("Se debe ingresar un número entero")

                conexion = Conexiones()
                conexion.abrirConexion()
        
                try:
                    conexion.puntero.execute("UPDATE DATOS SET cantidadDisponibles='{}' + cantidadDisponibles WHERE marca='{}'" .format(cantidadDisponibles, marca))
                    conexion.conexion.commit()
                    print("La cantidad disponible se actualizó correctamente")
                except:
                    print("No se pudo actualizar la cantidad disponible")
                finally:
                    conexion.cerrarConexion()
                
                
            if (opcion == 5):
                conexion = Conexiones()
                conexion.abrirConexion()
                try:
                    conexion.puntero.execute("SELECT * FROM DATOS ORDER BY PRECIO DESC")
                    ordenado = conexion.puntero.fetchall()
                    print(ordenado)
                except:
                    print("No se pudo mostrar la lista ordenada")
                finally:
                    conexion.cerrarConexion()
                
            if (opcion == 6):

                while True:
                    try:
                        marca = str(input("Por favor, ingrese la marca del monopatín: "))
                        break
                    except ValueError:
                        print("Se debe ingresar un texto")

                while True:
                    try:
                        modelo = str(input("Por favor, ingrese el modelo del monopatín: "))
                        break
                    except ValueError:
                        print("Se debe ingresar un texto")
    
                while True:
                    try:
                        color = str(input("Por favor, ingrese el color del monopátin: "))
                        break
                    except ValueError:
                        print("Se debe ingresar un texto")
                
                while True:
                    try:
                        potencia = float(input("Por favor, ingrese la potencia de monopatines: "))
                        break
                    except ValueError:
                        print("Se debe ingresar un número")
                
                while True:
                    try:
                        fechaUltimoPrecio = str(input("Por favor, ingrese la fecha correspondiente: "))
                        break
                    except ValueError:
                        print("Se debe ingresar una fecha")

                
                conexion = Conexiones()
                conexion.abrirConexion()

                try:
                    conexion.puntero.execute("UPDATE MONOPATIN SET modelo='{}', color='{}', potencia='{}', FECHA_ULTIMOPRECIO='{}' WHERE marca='{}'" .format(modelo, color, potencia, fechaUltimoPrecio, marca))
                    conexion.puntero.execute("INSERT INTO HISTORICOPRECIOS SELECT PRECIO FROM MONOPATIN")
                    conexion.puntero.execute("INSERT INTO HISTORICO_MONO (MODELO, MARCA, POTENCIA, PRECIO, COLOR, FECHA_ULTIMOPRECIO) SELECT MODELO, MARCA, POTENCIA, PRECIO, COLOR, FECHA_ULTIMOPRECIO FROM MONOPATIN")

                    conexion.conexion.commit()
                    print("Los datos del monopatín se actualizaron y se copiaron correctamente a la tabla HISTORICOPRECIOS")
                except:
                    print("Los datos no se pudieron copiar")
                finally:
                    conexion.cerrarConexion()
    
                
            if (opcion == 7):

                conexion = Conexiones()
                conexion.abrirConexion()

                while True:
                    try:
                        fechaUltimoPrecio = str(input("Por favor, ingrese la fecha correspondiente: "))
                        break
                    except ValueError:
                        print("Se debe ingresar una fecha")

                try:
                    conexion.puntero.execute("UPDATE MONOPATIN SET precio=precio+(precio*0.23)")
                    conexion.puntero.execute("UPDATE MONOPATIN SET FECHA_ULTIMOPRECIO='{}'" .format(fechaUltimoPrecio))
                    conexion.conexion.commit()
                    print("Precio y fecha actualizados correctamente en la tabla MONOPATIN")
                except:
                    print("No se pudo actualizar el 23 por ciento o la fecha")
                finally:
                    conexion.cerrarConexion()
            
            if (opcion == 8):
                conexion = Conexiones()
                conexion.abrirConexion()
                conexion.puntero.execute("SELECT * FROM MONOPATIN WHERE FECHA_ULTIMOPRECIO BETWEEN '2022/10/20' AND '2022/10/30'")
                conexion.conexion.commit()
                fechasOrdenadas = conexion.puntero.fetchall()
                print(fechasOrdenadas)
                conexion.cerrarConexion()
            

            if (opcion == 0):
                print("El programa ha finalizado. Gracias por utilizar el software.")
                break

class monopatin:
    
    def __init__(self, marca, precio=0, cantidadDisponibles=0):
        self.marca = marca
        self.precio = precio
        self.cantidadDisponibles = cantidadDisponibles

    def cargar_monopatin(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        
        try:    
            conexion.puntero.execute("INSERT INTO DATOS (marca, precio, cantidadDisponibles) VALUES('{}', '{}', '{}')" .format(self.marca, self.precio, self.cantidadDisponibles))
            conexion.puntero.execute("INSERT INTO MONOPATIN (marca, precio) VALUES('{}', '{}')" .format(self.marca, self.precio))
            conexion.conexion.commit()
            print("El monopatín se cargó correctamente")
        except:
            print("El monopatín no se pudo cargar")
        finally:
            conexion.cerrarConexion()


programa = ProgramaPrincipal()
programa.crearTabla("CREATE TABLE IF NOT EXISTS DATOS (ID INTEGER PRIMARY KEY AUTOINCREMENT, MARCA VARCHAR(30) UNIQUE, PRECIO FLOAT NOT NULL, CANTIDADDISPONIBLES INTEGER)")
programa.crearTabla("CREATE TABLE IF NOT EXISTS MONOPATIN (ID_MONO INTEGER PRIMARY KEY AUTOINCREMENT, MODELO VARCHAR(30), MARCA VARCHAR(30), POTENCIA VARCHAR(30), PRECIO INTEGER, COLOR VARCHAR(30), FECHA_ULTIMOPRECIO DATETIME)")
programa.crearTabla("CREATE TABLE IF NOT EXISTS HISTORICOPRECIOS (PRECIO INTEGER)")
programa.crearTabla("CREATE TABLE IF NOT EXISTS HISTORICO_MONO (ID_MONO INTEGER PRIMARY KEY AUTOINCREMENT, MODELO VARCHAR(30), MARCA VARCHAR(30), POTENCIA VARCHAR(30), PRECIO INTEGER, COLOR VARCHAR(30), FECHA_ULTIMOPRECIO DATETIME)")
programa.menu()
