import pymysql
from databaseX import DatabaseX


class Medidas:
    def __init__(self):
        self.peso = 0
        self.cintura = 0
        self.cuello = 0

    def ingresarPeso(self, peso):
        self.peso = peso

    def ingresarCintura(self, cintura):
        self.cintura = cintura

    def ingresarCuello(self, cuello):
        self.cuello = cuello

    def enviarRegistro(self):
        database = DatabaseX()
        sql = (
            "INSERT INTO `myfitapp`.`registrodiario`(`id_registro`,`id_usuario`,`cintura`,`cuello`,`pesoActual`,`fecha`)"
            + "VALUES(0,1,"
            + str(self.cintura)
            + ","
            + str(self.cuello)
            + ","
            + str(self.peso)
            + ",curdate());"
        )
        database.executeNonQueryBool(sql)
        mensaje = print("El registro se guardó correctamente")
        return mensaje
