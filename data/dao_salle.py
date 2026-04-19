import mysql.connector
import json

from models.salle import Salle


class DataSalle:
    def get_connection(self):
        with open("./data/config.json","r",encoding="utf-8") as f:
            config = json.load(f)
        connection = mysql.connector.connect(
            host = config["host"],
            user = config["user"],
            password = config["password"],
            database = config["database"])


        return connection
    def insert_salle(self,salle):
        con = self.get_connection()
        cursor = con.cursor()
        sql = "insert into salle values (%s,%s,%s,%s)"
        values = (salle.code,salle.description,salle.categorie,salle.capacite)
        cursor.execute(sql,values)
        con.commit()
        cursor.close()
        con.close()

    def update_salle(self,salle):
        con = self.get_connection()
        cursor = con.cursor()
        sql = ("update salle set description = %s, categorie = %s,capacite = %s where code = %s")
        values = (salle.description,salle.categorie,salle.capacite,salle.code)
        cursor.execute(sql,values)

        con.commit()
        cursor.close()
        con.close()

    def delete_salle(self, code):
        con = self.get_connection()
        cursor = con.cursor()
        sql = "delete from salle where code = %s"
        values = (code,)
        cursor.execute(sql, values)
        con.commit()
        cursor.close()
        con.close()

    def get_salle(self,code):
        con = self.get_connection()
        cursor = con.cursor()
        sql = "select * from salle where code = %s"
        values = (code,)
        cursor.execute(sql, values)
        salle = cursor.fetchall()
        cursor.close()
        con.close()
        return salle

    def get_salles(self):
        con = self.get_connection()
        cursor = con.cursor()
        sql = "select * from salle"
        cursor.execute(sql)
        salle = cursor.fetchall()
        con.commit()
        cursor.close()
        con.close()


        salles = []
        for s in salle:
            salle_ajout = Salle(s[0],s[1],s[2],s[3])
            salles.append(salle_ajout)


        if len(salles) == 0:
            return False
        else:
            return salles



        if len(salles) == 0:
            return False
        else:
            return salles