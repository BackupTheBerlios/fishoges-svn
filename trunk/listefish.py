import re, urllib, getdata

htmlSource = urllib.urlopen("http://www.aquabase.org/fish/dump.php3").read()
listeDeLiens= re.findall('">(.*?)</A>',htmlSource)
listeDeLiensurl= re.findall('<A HREF="(.*?)">',htmlSource)
nop=0
for lien in listeDeLiens :
    nop=nop+1
    if nop!=1:
        #print lien 
        
        #print listeDeLiensurl[(nop-1)]
        
        print( "INSERT INTO Fiche_POISSON ( id , nom , url ) VALUES ( " + str(nop-1) + " , '" + lien + "' , 'http://www.aquabase.org" + listeDeLiensurl[(nop-1)] + "' ) " )
        getdata.query( "INSERT INTO Fiche_POISSON ( id , nom , url ) VALUES ( " + str(nop-1) + " , '" + lien + "' , 'http://www.aquabase.org" + listeDeLiensurl[(nop-1)] + "' ) " )


