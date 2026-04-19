from data.dao_salle import DataSalle
from models.salle import Salle
data=DataSalle()
salle=Salle("s302","Salle 24 metres carres","Informatique",30)

print(data.get_salle("s302"))



