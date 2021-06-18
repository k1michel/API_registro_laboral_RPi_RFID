import dataset

class Conexion:
    fichero_sqlite: str = 'base_datos.db' 
    empleados = None

    def __init__(self):

        self.db = dataset.connect(
            f'sqlite:///{Conexion.fichero_sqlite}?check_same_thread=False')  # sirve para que varios procesos simultaneos se puedan ejecutar sin que salte warning
        # creamos instancia q mediante dataset la conectamos con nuestro fichero de la base de datos
        self.empleados = self.db['empleados']  # variable que alberga dentro de la instancia de la bd la lista vehiculos


    def busqueda_nombre(self,nombre) -> list:
        return [dict(registro) for registro in self.empleados.all() if dict(registro)["nombre"] == nombre]

    def busqueda_ano(self,ano) -> list:
        return [dict(registro) for registro in self.empleados.all() if dict(registro)["ano"] == ano]

    def busqueda_mes(self,mes) -> list:
        return [dict(registro) for registro in self.empleados.all() if dict(registro)["mes"] == mes]

    def busqueda_dia(self,dia) -> list:
        return [dict(registro) for registro in self.empleados.all() if dict(registro)["dia"] == dia]
    
    def busqueda_completa(self,nombre,ano,mes,dia) -> list:
        if nombre:
            