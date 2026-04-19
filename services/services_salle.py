from data.dao_salle import DataSalle
from models.salle import Salle


class ServiceSalle:
    def __init__(self):
        self.dao_salle = DataSalle()
    def ajouter_salle(self, salle):
        if not salle.code or not salle.description or not salle.categorie or salle.capacite is None:
            return False, "merci de remplir tous les champs."


        if salle.capacite < 1:
            return False, "valeur invalide : La capacite minimale d une salle doit etre superieur ou egal a 1"

        self.dao_salle.insert_salle(salle)
        return True, "Ajout de la salle reussi"
    def modifier_salle(self, salle):
        if not salle.code or not salle.description or not salle.categorie or salle.capacite is None:
            return False, "merci de remplir tous les champs."

        if salle.capacite < 1:
            return False, "valeur invalide : La capacite minimale d une salle doit etre superieur ou egal a 1"
        self.dao_salle.update_salle(salle)

        return True, "modification de la salle reussi"
    def supprimer_salle(self, code):
        code_exists = self.dao_salle.get_salle(code)
        if code_exists is False:
            print("aucun code correspondant n a ete trouve")
        else:
            self.dao_salle.delete_salle(code)
            print("suppression de la salle reussi")
    def rechercher_salle(self, code):
        code_exists = self.dao_salle.get_salle(code)
        if code_exists is False:
            print("aucun code correspondant n a ete trouve")
        else:
            print(code_exists)
    def recuperer_salles(self):
        table = self.dao_salle.get_salles()
        if table is False:
            print("aucune information disponible")
        else:
            for salle in table:
                Salle.afficher_infos(salle)

