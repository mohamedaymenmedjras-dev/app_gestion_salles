from data.dao_salle import DataSalle
from models.salle import Salle
data=DataSalle()
s1 = Salle("z32", "Salle laboratoire chimique.", "chimique", 12)
data.delete_salle("z32")