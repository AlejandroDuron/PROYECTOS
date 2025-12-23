import pymysql

class ModeloCliente:
    def __init__(self, host='localhost', database='siger', user='root', password='1234'):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def conectar(self):
        """
        Conectar a la base de datos MySQL.
        """
        try:
            return pymysql.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except pymysql.MySQLError as e:
            print(f"Error al conectar con la base de datos: {e}")
            return None

    def insertar_cliente(self, nombre, direccion, telefono, email, fecha_registro):
        """
        Inserta un nuevo cliente en la base de datos.
        """
        try:
            connection = self.conectar()
            if connection:
                with connection.cursor() as cursor:
                    sql = """
                        INSERT INTO clientes (nombre, direccion, telefono, email, fecha_registro)
                        VALUES (%s, %s, %s, %s, %s)
                    """
                    cursor.execute(sql, (nombre, direccion, telefono, email, fecha_registro))
                    connection.commit()
                connection.close()
                return True
            else:
                return False
        except pymysql.MySQLError as e:
            print(f"Error al insertar el cliente: {e}")
            return False
