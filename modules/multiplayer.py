#Connexion principale

import socket

host = ' 172.20.10.9.'
port = 9006

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#création d'un réseau
connexion_principale.listen(2)#pour choisir un nombre de joueur max
connexion_principale.bind((host, port))#connecter le socket
print("le serveur est à présent ouvertsur le port ....".format(port))
connexion_avec_joueur, infos_connexion = connexion_principale.accept()#qui va se lancer uniquement quand il y aura une connexion avec quelqu'un d'autre

msg_recu = ""
while msg_recu != "fin":
    msg_recu = connexion_avec_joueur.recv(1024)
    connexion_avec_joueur.send("connecté avec les serveur")

                                          

print("fermeture de la connexion")
connexion_avec_joueur.close()  #Pour fermer la connexion de notre socket
connexion_principale.close() 

###Connexion avec l'autre personne, connexion secondaire
"""
import socket

host = ""
port = 

connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect((host,port))
print("connexion établie".format(port))
msg_a_envoyer = b""
while msg_a_envoyer != b"fin":
    msg_a_envoyer = input(">")
    msg_a_envoyer = msg_a_envoyer.encode()
    connexion_avc_serveur.send(msg_a_envoyer)
    msg_recu = connexion_avc_serveur.recv(1024)
    print(msg_recu.decode())
print("fermeture de la connexion")
connexion_avec_serveur.close()
"""
