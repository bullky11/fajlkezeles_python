def beolvas(fajlnev):
    fajlom=open(fajlnev,"r", encoding='utf-8')
    print(fajlom)
    """fajtltartalom=fajlom.read()
    print(fajtltartalom)"""
    fejlec=fajlom.readline()
    print(fejlec)
    sorok=fajlom.readlines()
    print(sorok)
    fajlom.close()
    fajlfeldolgozas(sorok)

nevek=[]
nemek=[]
korok=[]

def fajlfeldolgozas(sorok):
    """itt dolgozom fel a kapott listát"""
    i=0
    while i<len(sorok):
        print(sorok[i].strip())
        sor = sorok[i].strip().split(', ')
        print(sor)
        nevek.append(sor[0])
        nemek.append(sor[1])
        korok.append(sor[2])
        i+=1
    print(nevek,nemek,korok)




    """ez a fejléc"""
"""    fajlom.readline()
    fajl_tartalom=fajlom.readlines()
    fajlom.close()"""