# -*- coding: cp1252 -*-


import sqlite,globalfunc


class query:
    def __init__(self,requete=None):
        try:
            connection = sqlite.connect("base.sqlite", autocommit=True)
            #connection = MySQLdb.connect(paramconec[0], paramconec[1], paramconec[2], paramconec[3])
            cursor = connection.cursor()
            cursor.execute( requete )
        except sqlite.OperationalError, message:
            errorMessage = "Error %d:\n%s" % ( message[ 0 ], message[ 1 ] )
            print errorMessage
            qb=globalfunc.MessageBox(style='hand ok')
            ans=qb.show(errorMessage)
            return
        else:
             self.data = cursor.fetchall()
             self.fields = cursor.description
             cursor.close()
             connection.close()



