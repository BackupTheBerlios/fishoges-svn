# -*- coding: cp1252 -*-
import re, urllib, getdata, html2text, time
  #time.sleep(60)


rown=0

casereq=("descripteur","famille","synonyme","taille","origine","temperature","PH","durete","zone","description","vie","comportement","reproduction","dimorphisme")
while rown < 1199 :

#while rown < 938 :
    rown=rown+1
    requete = getdata.query("select url from Fiche_POISSON where id = " + str(rown))
    bcl=0
    htmlsanschar="<strong>Désolé 82.xxx.xxx.xxx, le site est en cours de maintenance...</strong><br/><small>Revenez dans 30 secondes.</small>"
    bibi = re.findall('</strong><br/><small>(.*?)</small>',htmlsanschar)
    try:
        while bibi[0] == "Revenez dans 30 secondes." :
            
            print requete.data[0][0]
            htmlSource = urllib.urlopen(requete.data[0][0]).read()
            htmlsanschar =  htmlSource.replace("\n"," ")
            print htmlsanschar
            bibi = re.findall('</strong><br/><small>(.*?)</small>',htmlsanschar)
            try:
                if bibi[0] == "Revenez dans 30 secondes." :
                    print "sleeping begin at id " + str(rown)
                    time.sleep(31)
                    print "sleeping end"
            except :
                print "IOerror"            

    except :
        print "IOerror"            
       
    listeDeLiens= re.findall('SPAN CLASS="ListLineOdd">(.*?)</SPAN>',htmlsanschar)
    #listeDeLiensurl= re.findall('<A HREF="(.*?)">',htmlSource)
    #print listeDeLiens
    nop=0
    for lien in listeDeLiens :
        nop=nop+1
        if nop!=1:
            #print str(nop)
            
            aremplir = html2text.html2text(lien)
            #print aremplir
            if nop < 16:
                print casereq[nop-2] + " : " + aremplir
                aremplir=aremplir.replace("'","''")
                print( "UPDATE Fiche_POISSON SET " + casereq[nop-2] + " = '" + aremplir + "' WHERE id = " + str(rown))
                getdata.query( "UPDATE Fiche_POISSON SET " + casereq[nop-2] + " = '" + aremplir + "' WHERE id = " + str(rown))
            #print listeDeLiensurl[(nop-1)]
            
            #print( "INSERT INTO Fiche_POISSON ( id , nom , url ) VALUES ( " + str(nop-1) + " , '" + lien + "' , 'http://www.aquabase.org" + listeDeLiensurl[(nop-1)] + "' ) " )
            #getdata.query( "INSERT INTO Fiche_POISSON ( id , nom , url ) VALUES ( " + str(nop-1) + " , '" + lien + "' , 'http://www.aquabase.org" + listeDeLiensurl[(nop-1)] + "' ) " )


