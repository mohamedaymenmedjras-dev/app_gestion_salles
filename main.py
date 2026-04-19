from data.dao_salle import DataSalle
from models.salle import Salle
from services.services_salle import ServiceSalle

data=DataSalle()
salle=Salle("s302","Salle 24 metres carres","Informatique",30)
s2=Salle("z104","Salle 10 metres carres","Chimie",0)
s3=Salle("z104","Salle 10 metres carres","Chimie",15)

service = ServiceSalle()
service.recuperer_salles()





