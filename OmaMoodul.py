from random import*

def Lisa_andmed(s:list,t:list):
    """Sportlase ja tema tulemuste lisamine järjendise
    :param list s: Sportlaste järend
    :param list t: Tulemuste järend
    :rtype: list, list
    """

    n=int(input("Mitu inimest: "))
    for j in range(n):
        nimi=input("Sisesta nimi: ")
        tulemus = [randint(1, 100) for n in range(3)]
        max_index = tulemus.index(max(tulemus))
        s.append(nimi)
        t.append(max_index)
    return s, t

def top(s:list,t:list): 
    """Sportlase ja tema tulemuste top näitamine
    :param list s: Sportlaste järend
    :param list t: Tulemuste järend
    :rtype: list, list
    """
    toppos=int(input("Palju parimate tulemuste tahad näha? "))
    kopia=t.copy()
    for j in range(toppos):
        ind=kopia.index(max(kopia))
        print(f"{j+1} inimene - {s[ind]} parima tulemuse: {t[ind]}")
        kopia.pop(ind)
        kopia.insert(ind,min(t)+1)

def Suurim_tulemus(s:list,t:list):
    """Maksimaalse tulemuste leidmine
    :param list s: Sportlaste järend
    :param list t: Tulemuste järend
    :rtype: list, list
    """
    n=len(t)
    for j in range(0,n-1):
            for k in range(j+1,n):
                if t[j]>t[k]:
                    abi=t[j]
                    t[j]=t[k]
                    t[k]=abi
                    abi=s[j]
                    s[j]=s[k]
                    s[k]=abi
    return s, t     

def näita_tulemused(s:list,t:list):
    """Tulemuste näitamine
    :param list s: Sportlaste järend
    :param list t: Tulemuste järend
    :rtype: str, int
    """
    tulemus=[]
    nimi=input("Kelle tulemuse tahad leia? \n")
    n=s.count(nimi)
    ind=s.index(nimi)
    print(f'{nimi} saab {t[ind]} \n')
    return tulemus
    
def diskvalifitseerimine(s:list,t:list):
    """Diskvalifitseerimine
    :param list s: Sportlaste järend
    :param list t: Tulemuste järend
    :rtype: list, list
    """
    nimi=(input("Sisesta nimi "))
    if nimi in s:
        n=s.count(nimi)
        for j in range(n):
            ind=s.index(nimi)
            s.pop(ind)
            t.pop(ind)
        return s, t

def boonuspunktid(s:list,t:list):
    """Boonuspunktide lisamine
    :param list s: Sportlaste järend
    :param list t: Tulemuste järend
    :rtype: list, list
    """
    T = int(input('Palju boonus on? '))
    for j in range(len(t)):
        t[j] = t[j] + T
    return s,t
