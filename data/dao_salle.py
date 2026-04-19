import mysql.connector
import json




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
    def update_salle(self,salle):
        con = self.get_connection()
        cursor = con.cursor()
        sql = ("update salle set description = %s, categorie = %s,capacite = %s where code = %s")
        values = (salle.description,salle.categorie,salle.capacite,salle.code)
        cursor.execute(sql,values)

        con.commit()
        cursor.close()
        con.close()
