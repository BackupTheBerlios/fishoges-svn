# -*- coding: cp1252 -*-


import sqlite
#Pour créer une base de donnée en mémoire
#cx = sqlite.connect(":memory:")

# OU
#Sur disque (un seul fichier sera écrit)
cx = sqlite.connect("base.sqlite", autocommit=True)
cur = cx.cursor()

#création d'une table répertoire
#cur.execute("create table repertoire (rowid integer primary key, nom char(20), prenom char(20))")

#écriture de deux enregistrements
#cur.execute("insert into repertoire (nom,prenom) values (%s,%s)", ("toto", "lito"))
#cur.execute("insert into repertoire (nom,prenom) values (%s,%s)", ("titi", "liti"))

#affichage des enregistrements
cur.execute("select * from repertoire")
for row in cur.fetchall():
    print row.nom, row.prenom 


class SGBD:

    host = None
    user = None
    passwd = None
    database = None
    type = None

    def __init__(self):
        pass
  



    

def database(params): 
   
    
    #x=TransformXmlToSGBD()
    #print 
    #x=TransformXmlToSGBD()
    #print x.getSGBD()[0].user
    #x=TransformXmlToSGBD()
    #print x.getSGBD()[0].passwd
    try:
        if sgbd_host:
           #isset
            params[0]=sgbd_host
            params[1]=sgbd_user
            params[2]=sgbd_passwd
            params[3]=sgbd_database
            params[4]=sgbd_type
            
    except NameError      :
        #not set
        x=TransformXmlToSGBD()
        sgbd_host = x.getSGBD()[0].host
        x=TransformXmlToSGBD()
        sgbd_user = x.getSGBD()[0].user
        x=TransformXmlToSGBD()
        sgbd_passwd = x.getSGBD()[0].passwd
        x=TransformXmlToSGBD()
        sgbd_database = x.getSGBD()[0].database
        x=TransformXmlToSGBD()
        sgbd_type = x.getSGBD()[0].type
        params[0]=sgbd_host
        params[1]=sgbd_user
        params[2]=sgbd_passwd
        params[3]=sgbd_database
        params[4]=sgbd_type

