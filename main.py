from data.dao_salle import DataSalle
from models.salle import Salle
data=DataSalle()
s1 = Salle("z32", "Salle laboratoire chimique.", "chimique", 33)
data.insert_salle(s1)