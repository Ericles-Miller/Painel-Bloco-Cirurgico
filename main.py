from dados_cir import receiver_agenda_cir
from dados_obs import receiver_agenda_obs
from dados_end import receiver_agenda_end
import time, os


def consult_agenda():
    x =1
    while x==1:
        receiver_agenda_cir()
        receiver_agenda_obs()
        receiver_agenda_end()
        time.sleep(300) #renova a consulta a cada tres minutos
        os.system("cls")
    
consult_agenda()