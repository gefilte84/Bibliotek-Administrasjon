#Obligatorisk oppgave 2 programmering, gruppe 9                                                                              #
#Importerer tkinter og pymysql og datetime                                                                                   #
import datetime                                                                                                              #
import pymysql                                                                                                               #
from tkinter import *                                                                                                        #
from tkinter import ttk                                                                                                      #
mindatabase = pymysql.connect(host='localhost', port=3306,user='Biblioteksjef', passwd='bibliotek2018', db='Fagbokbibliotek')#
#----------------------------------------------------------------------------------------------------------------------------#




#-----------------------------------------------------------------------------#
#1 - Registrerings Oppgaver                                                   #
#-----------------------------------------------------------------------------#
def registrere_bruker():
    
    def oprett_bruker():
        cursor=min_database.cursor()
        Fornavn=fornavn.get()
        Etternavn=etternavn.get()
        cursor.execute("SELECT LNr FROM Laaner")
        #default lnr på 1000
        j=1001
        #leser rad for rad og tildeler lnr 1000 + lengden av listen
        bol=False
        if Fornavn =='' or Etternavn =='':
            utdata.set('Mangler felt')
            bol=True
        if bol == False:
            for row in cursor:
                j+=1
            lnr_nummer=str(j)
            cursor.close()
            cursor=min_database.cursor()
            settin_bruker = ("INSERT INTO Laaner"
                             "(LNr, Fornavn, Etternavn)"
                             "VALUES(%s,%s,%s)")
            data_bruker = (lnr_nummer,Fornavn,Etternavn)
            cursor.execute(settin_bruker,data_bruker)
            min_database.commit()
            cursor.close()
            utdata.set('Bruker registrert')
            utdata2.set(lnr_nummer)
        

    min_database = pymysql.connect(host='localhost', port=3306,user='Biblioteksjef', passwd='bibliotek2018', db='Fagbokbibliotek')
        
    window=Toplevel()
    window.title('Registrer Bruker')
    #Label

    lbl_fornavn=Label(window,text='Fornavn:')
    lbl_fornavn.grid(row=0,column=0,padx=5,pady=5,sticky=W)

    lbl_etternavn=Label(window,text='Etternavn:')
    lbl_etternavn.grid(row=1,column=0,padx=5,pady=5,sticky=W)

    lbl_lnr=Label(window,text='LNr:')
    lbl_lnr.grid(row=3,column=0,padx=5,pady=5,sticky=W)

    lbl_resultat=Label(window,text='Resultat:')
    lbl_resultat.grid(row=2,column=0,padx=5,pady=5,sticky=W)

    #Entry

    fornavn=StringVar()
    ent_fornavn=Entry(window,width=15,textvariable=fornavn)
    ent_fornavn.grid(row=0,column=1,padx=5,pady=5,sticky=W)

    etternavn=StringVar()
    ent_etternavn=Entry(window,width=30,textvariable=etternavn)
    ent_etternavn.grid(row=1,column=1,padx=5,pady=5)

    #Buttons
    lbl_kommentar=Label(window,text="Trykk 'Legg til bruker' flere ganger")
    lbl_kommentar.grid(row=2, column=2,padx=5,pady=0,sticky=W)

    lbl_kommentar=Label(window,text="etter du har endret navn for å registrere flere brukere")
    lbl_kommentar.grid(row=3, column=2,padx=5,pady=0,sticky=W)


    btn_legg_til=Button(window,width=10,text='Legg til Bruker',command=oprett_bruker)
    btn_legg_til.grid(row=7,column=1,padx=5,pady=5,sticky=W)

    btn_avslutte=Button(window,width=10, text='Avslutt',command=window.destroy)
    btn_avslutte.grid(row=7,column=2,padx=10, pady=15)

    #utdata
    utdata = StringVar()
    ent_LNrEks = Entry(window, width=20, state='readonly', textvariable=utdata)
    ent_LNrEks.grid(row=2, column=1, padx=5,sticky=W)

    utdata2 = StringVar()
    ent_LNrEks = Entry(window, width=4, state='readonly', textvariable=utdata2)
    ent_LNrEks.grid(row=3, column=1, padx=5,sticky=W)



    window.mainloop()


#------------------------------------------------------------------------------
def legge_til_bok():
    def legg_til():
        min_database = pymysql.connect(host='localhost', port=3306,user='Biblioteksjef', passwd='bibliotek2018', db='Fagbokbibliotek')
        #opretter markør
        markor = min_database.cursor()
        inndata_markor=min_database.cursor()
        #overfører data fra entry feltene til funksjonsvariablene
        ISBN = bisbn.get()
        Tittel = btittel.get()
        Forfatter = bforfatter.get()
        Forlag = bforlag.get()
        UtgittAar = butgittaar.get()
        AntallSider = bantallsider.get()

        markor.execute("SELECT ISBN FROM Eksemplar")
        bol=False
        j=1
        for row in markor:
            if row[0] == ISBN:
                bol=True
                j+=1
        markor.close()
        eksemplar_nummer=str(j)

        if Tittel == '' or Forfatter =='' or Forlag =='' or UtgittAar ==''\
           or AntallSider =='':
            utdata.set('Ops du har glemt å fylle et felt')
            bol = True
        
        elif bol != True:
            #legger til data for bok tabell
            settin_bok = ("INSERT INTO Bok"
                                "(ISBN, Tittel, Forfatter, Forlag, UtgittAar, Antallsider)"
                                "VALUES(%s, %s, %s, %s, %s, %s)")
            data_bok = (ISBN, Tittel, Forfatter, Forlag, UtgittAar, AntallSider)

            inndata_markor.execute(settin_bok, data_bok)
            min_database.commit()
            
            #legger til data for Ekemplar tabell
            settin_eks=("INSERT INTO Eksemplar"
                        "(ISBN,EksNr)"
                        "VALUES(%s,%s)")
            
            data_eks=(ISBN,eksemplar_nummer)
            inndata_markor.execute(settin_eks,data_eks)
            min_database.commit()
            #stenger markor og database
            min_database.close()
            inndata_markor.close()
            utdata.set('Bok er registrert')
        else:
             utdata.set('Bok finnes før gå til eksemplar for å registrere et nytt')
            


    window=Toplevel()
    window.title('Registrer Bok')
    
    #Labels
    lbl_isbn=Label(window,text='ISBN:')
    lbl_isbn.grid(row=0,column=0,padx=5,pady=5,sticky=W)

    lbl_tittel=Label(window,text='Tittel:')
    lbl_tittel.grid(row=1,column=0,padx=5,pady=5,sticky=W)

    lbl_forfatter=Label(window,text='Forfatter:')
    lbl_forfatter.grid(row=2,column=0,padx=5,pady=5,sticky=W)

    lbl_forlag=Label(window,text='Forlag:')
    lbl_forlag.grid(row=3,column=0,padx=5,pady=5,sticky=W)

    lbl_utgittaar=Label(window,text='Utgittår:')
    lbl_utgittaar.grid(row=4,column=0,padx=5,pady=5,sticky=W)

    lbl_antallsider=Label(window,text='Antallsider:')
    lbl_antallsider.grid(row=5,column=0,padx=5,pady=5,sticky=W)

    #Entry
    bisbn = StringVar()
    ent_isbn=Entry(window,width=13,textvariable=bisbn)
    ent_isbn.grid(row=0,column=2,padx=5,pady=5,sticky=W)

    btittel = StringVar()
    ent_tittel=Entry(window,width=35,textvariable=btittel)
    ent_tittel.grid(row=1,column=2,padx=5,sticky=W)

    bforfatter = StringVar()
    ent_forfatter=Entry(window,width=20,textvariable=bforfatter)
    ent_forfatter.grid(row=2,column=2,padx=5,sticky=W)

    bforlag = StringVar()
    ent_forlag=Entry(window,width=20,textvariable=bforlag)
    ent_forlag.grid(row=3,column=2,padx=5,sticky=W)

    butgittaar = StringVar()
    ent_utgittaar=Entry(window,width=4,textvariable=butgittaar)
    ent_utgittaar.grid(row=4,column=2,padx=5,pady=5,sticky=W)

    bantallsider = StringVar()
    ent_antallsider=Entry(window,width=3,textvariable=bantallsider)
    ent_antallsider.grid(row=5,column=2,padx=5,pady=5,sticky=W)


    btn_legg_til=Button(window,width=10,text='Legg til bok',command=legg_til)
    btn_legg_til.grid(row=8,column=2,padx=5,pady=5,sticky=W)

    btn_avslutte=Button(window,width=10, text='Avslutt',command=window.destroy)
    btn_avslutte.grid(row=8,column=10,padx=10, pady=15)

    #utdata
    utdata = StringVar()
    ent_LNrEks = Entry(window, width=50, state='readonly', textvariable=utdata)
    ent_LNrEks.grid(row=7, column=2, padx=5)

    window.mainloop()

def legge_til_eksemplar():
    def legg_til():
        min_database = pymysql.connect(host='localhost', port=3306,user='Biblioteksjef', passwd='bibliotek2018', db='Fagbokbibliotek')
        #opretter markør
        markor = min_database.cursor()
        #overfører data fra entry feltene til funksjonsvariablene
        ISBN = bisbn.get()
        Antall = antall.get()
        markor.execute("SELECT * FROM Eksemplar")
        j=1
        bol=False
        var=len(ISBN)
        if var == 13 and Antall !='':
            for row in markor:
                if row[0] == ISBN:
                    bol=True
                    j+=1
            eksemplar_nummer=str(j)
            number=int(Antall)
            if bol == True and int(eksemplar_nummer) < 9:
                #lager eksemplarer i forhold til antall du vil ha av boken
                for row in range(number):
                    settin_eks=("INSERT INTO Eksemplar"
                                "(ISBN,EksNr)"
                                "VALUES(%s,%s)")
                    #lager eksemplar nummer ut i fra hvor mange treff på isbn i eksemplar tabellen
                    data_eks=(ISBN,eksemplar_nummer)
                    markor.execute(settin_eks,data_eks)
                    min_database.commit()
                    j+=1
                    eksemplar_nummer=str(j)
                variabel=int(eksemplar_nummer)
                variabel2=variabel-1
                eksemplar_nummer=str(variabel2)
                if int(eksemplar_nummer) <= 9:
                    utdata.set(eksemplar_nummer + ' Eksemplarer finnes nå')
                else:
                    int(eksemplar_nummer) == 9
                    utdata.set(eksemplar_nummer + ' Eksemplarer finnes nå')
            elif int(eksemplar_nummer) > 9:
                utdata.set('Eksemplar oversteget kapasitet')
                        
            else:
                utdata.set('ISBN Finnes ikke gå til "legg til bok"')
                
        elif Antall=='' and var != 13:
            utdata.set('Feil Antall og ISBN')

        elif Antall =='':
            utdata.set('Antall Kreves')
        else:
            utdata.set('Kreves 13 kar for ISBN')
        
        min_database.close()
        markor.close()
        

    window=Toplevel()
    window.title('Registrer Eksemplar')
    #Labels
    lbl_isbn=Label(window,text='ISBN:')
    lbl_isbn.grid(row=0,column=0,padx=5,pady=5,sticky=W)

    lbl_tittel=Label(window,text='Antall Eksemplarer:')
    lbl_tittel.grid(row=1,column=0,padx=5,pady=5,sticky=W)


    #Entry
    bisbn = StringVar()
    ent_isbn=Entry(window,width=13,textvariable=bisbn)
    ent_isbn.grid(row=0,column=2,padx=5,pady=5,sticky=W)

    antall = StringVar()
    ent_antallsider=Entry(window,width=1,textvariable=antall)
    ent_antallsider.grid(row=1,column=2,padx=5,pady=5,sticky=W)


    btn_legg_til=Button(window,width=20,text='Legg til Eksemplar',command=legg_til)
    btn_legg_til.grid(row=8,column=2,padx=5,pady=5,sticky=W)

    btn_avslutte=Button(window,width=10, text='Avslutt',command=window.destroy)
    btn_avslutte.grid(row=8,column=10,padx=10, pady=15)

    #utdata
    utdata = StringVar()
    ent_LNrEks = Entry(window, width=40, state='readonly', textvariable=utdata)
    ent_LNrEks.grid(row=7, column=2, padx=5)
    window.mainloop()

#-----------------------------------------------------------------------------#
#2 - Innleveringer og Utlån                                                   #
#-----------------------------------------------------------------------------#
def innleveringer1():
    def LeverBok():
        cursor = mindatabase.cursor()

        #variabler
        ISBN = entISBN.get()
        EksemplarNr = entEksemplarNr.get()
        Leverings_dato = datetime.date.today()

        cursor.execute("SELECT * FROM Utlaan")
        
        bol1=False
        bol2=False
        bol3=False
        for row in cursor:
            if row[2] == ISBN:
                bol1=True
                if row[3] == EksemplarNr:
                    bol2=True
                    if row[5] != '':
                        bol3=True

        if bol1 == True and bol2 == True and bol3 == True:
            
            #Oppdatere innleveringsdato (levere inn bok)
            oppdatere_leveringsdato = ("UPDATE Utlaan SET Innleveringsdato = %s WHERE ISBN = %s AND EksNr = %s AND Innleveringsdato IS NULL")
            ny_data = (Leverings_dato, ISBN, EksemplarNr)
            cursor.execute(oppdatere_leveringsdato, ny_data)
            utdata.set('Boken er innlevert!')

        elif bol1 == False:
            utdata.set('Bok finnes ikke')
        elif bol2 == False:
            utdata.set('Eksemplaret av boken finnes ikke')
        elif bol3 == False:
            utdata.set('Boken tastet inn er allerede levert')
        
        mindatabase.commit()
        mindatabase.close()
        cursor.close()

    window=Toplevel()
    window.title('Innlevering av bøker')

    #Label
    lbl_ISBN=Label(window,text='ISBN:')
    lbl_ISBN.grid(row=0,column=0,padx=5,pady=5,sticky=W)

    lbl_EksemplarNr=Label(window,text='EksemplarNr:')
    lbl_EksemplarNr.grid(row=1,column=0,padx=5,pady=5,sticky=W)

    lbl_resultat=Label(window,text="Resultat = ")
    lbl_resultat.grid(row=2, column=0, padx=5,pady=5,sticky=W)

    #Entry
    entISBN = StringVar()
    ent_ISBN=Entry(window,width=13, textvariable=entISBN)
    ent_ISBN.grid(row=0,column=1,padx=5,pady=5,sticky=W)

    entEksemplarNr = StringVar()
    ent_EksemplarNr=Entry(window,width=1, textvariable=entEksemplarNr)
    ent_EksemplarNr.grid(row=1,column=1,padx=5,pady=5,sticky=W)

    #Output
    utdata = StringVar()
    ent_utdata = Entry(window, width=30, state='readonly', textvariable=utdata)
    ent_utdata.grid(row=2, column=1, padx=5)

    #Button
    btn_LeverBok=Button(window,width=10,text='Lever Bok',command=LeverBok)
    btn_LeverBok.grid(row=3,column=1,padx=5,pady=5,sticky=W)

    #Knapp for å lukke vinduet
    btn_return = Button(window, text='Avslutt', command=window.destroy)
    btn_return.grid(row=3,column=2,padx=5,pady=5,sticky=W)

    window.mainloop()

#------------------------------------------------------------------------------
def Registrere_utlån():
    def laanebok():
        markor=mindatabase.cursor()
        Fornavn= fornavn.get()
        Etternavn= etternavn.get()
        ISBN=isbn.get()
        EksNr=eksnr.get()
        
        markor.execute("SELECT * FROM Laaner")
        bol=False
        #skaffer lnr nummer
        for row in markor:
            if Fornavn == row[1] and Etternavn == row[2]:
                bol=True
                LNr=row[0]# lnr
                utdata.set(LNr)
            elif bol == False:
                utdata.set('Navn finnes ikke')
        markor.execute("SELECT ISBN,EksNr FROM Eksemplar")
        #sjekker om bok eksemplaret finnes i eksemplar
        if bol == True:
            for row in markor:
                if row[0] == ISBN and row[1] == EksNr:
                    markor.execute("SELECT UtlaansNr FROM Utlaan")
                    j=5000
                    for row in markor:
                        j+=1
                    Utlaansdato=datetime.date.today()
                    utlaan_nummer=str(j)
                    utdata2.set('Lån gjennomført. UtlånNr = '+utlaan_nummer)
                    settin_data = ("INSERT INTO Utlaan"
                                   "(UtlaansNr,LNr,ISBN,EksNr,Utlaansdato)"
                                   "VALUES (%s, %s, %s, %s, %s)")
                    data_utlaan = (utlaan_nummer,LNr,ISBN,EksNr,Utlaansdato)
                    markor.execute(settin_data, data_utlaan)
                    mindatabase.commit()

    #------GUI------#
    window=Toplevel()
    window.title('Utlån av bok')

    #Label
    lbl_fornavn=Label(window,text='Fornavn:')
    lbl_fornavn.grid(row=0,column=0,padx=5,pady=5,sticky=W)

    lbl_etternavn=Label(window,text='Etternavn:')
    lbl_etternavn.grid(row=1,column=0,padx=5,pady=5,sticky=W)

    lbl_isbn=Label(window,text='ISBN:')
    lbl_isbn.grid(row=2,column=0,padx=5,pady=5,sticky=W)

    lbl_eksnr=Label(window,text='EksNr:')
    lbl_eksnr.grid(row=3,column=0,padx=5,pady=5,sticky=W)

    lbl_LNr=Label(window,text='LåneNr =')
    lbl_LNr.grid(row=6,column=0,padx=5,pady=5,sticky=W)

    #Entry
    fornavn=StringVar()
    ent_fornavn=Entry(window,width=15,textvariable=fornavn)
    ent_fornavn.grid(row=0,column=1,padx=5,pady=5,sticky=W)

    etternavn=StringVar()
    ent_etternavn=Entry(window,width=30,textvariable=etternavn)
    ent_etternavn.grid(row=1,column=1,padx=5,pady=5,sticky=W)

    isbn=StringVar()
    ent_etternavn=Entry(window,width=13,textvariable=isbn)
    ent_etternavn.grid(row=2,column=1,padx=5,pady=5,sticky=W)

    eksnr=StringVar()
    ent_etternavn=Entry(window,width=1,textvariable=eksnr)
    ent_etternavn.grid(row=3,column=1,padx=5,pady=5,sticky=W)                   

    #Buttons
    btn_legg_til=Button(window,width=15,text='Registrer Utlån',command=laanebok)
    btn_legg_til.grid(row=5,column=0,padx=5,pady=5,sticky=W)

    btn_avslutte=Button(window,width=10, text='Avslutt',command=window.destroy)
    btn_avslutte.grid(row=7,column=1,padx=10, pady=15,sticky=E)

    #Utdata
    utdata = StringVar()
    ent_LNrEks = Entry(window, width=30, state='readonly', textvariable=utdata)
    ent_LNrEks.grid(row=6, column=1, padx=5,sticky=W)

    utdata2 = StringVar()
    ent_LNrEks = Entry(window, width=30, state='readonly', textvariable=utdata2)
    ent_LNrEks.grid(row=5, column=1, padx=5,sticky=W)

    window.mainloop()
#------------------------------------------------------------------------------
def ikke_levert():
    #Gjør tilkoblingen mot database
    mindatabase = pymysql.connect(host='localhost', port=3306, user='Biblioteksjef', passwd='bibliotek2018', db='Fagbokbibliotek')
    
    #Cursor er en variabel og mindatabase.cursor tillater at man gjennomfør sql kommandoer
    cursor = mindatabase.cursor()
    
    #Execute gjør at det kan utføres SQL spørringer
    cursor.execute("SELECT Utlaan.*, Laaner.Fornavn, Laaner.Etternavn FROM Utlaan LEFT JOIN Laaner ON Utlaan.LNr = Laaner.LNr WHERE Innleveringsdato IS NULL")

    #------GUI------#
    #Lager hovedvindu
    root = Toplevel()
    
    #Oppretter tittel for vindu
    root.title('Oversikt over bøker ikke returnert')
    
    #Lager tabellen inn i vindu
    Tabell = ttk.Treeview(root)
    
    #Fjerner første boksen
    Tabell['show'] = 'headings'
    
    #Lager kolonner
    Tabell["columns"]=("en","to","tre","fire","fem","seks", "syv", "åtte")
    
    #Bestemmer lengde på kolonner
    Tabell.column("en", width=70)
    Tabell.column("to", width=50)
    Tabell.column("tre", width=90)
    Tabell.column("fire", width=25)
    Tabell.column("fem", width=80)
    Tabell.column("seks", width=100)
    Tabell.column("syv", width=70)
    Tabell.column("åtte", width=70)

    #Bestemmer hva kolonnene skal hete
    Tabell.heading("en", text="UtlånsNR")
    Tabell.heading("to", text="LNr")
    Tabell.heading("tre", text="ISBN")
    Tabell.heading("fire", text="EksNr")
    Tabell.heading("fem", text="Utlånsdato")
    Tabell.heading("seks", text="Innleveringsdato")
    Tabell.heading("syv", text="Fornavn")
    Tabell.heading("åtte", text="Etternavn")

    #For loop for å sette inn verdier i radene
    #Row er hver linje inn i cursor
    for row in cursor:
        Tabell.insert("", 0, values=(row))

    Tabell.pack()
    #Gjør at vindu holder seg oppe
    root.mainloop()

#-----------------------------------------------------------------------------#
#3 - Statistikk og Oversikt                                                   #
#-----------------------------------------------------------------------------#
def ulante_boker():
    #Cursor er en variabel og mindatabase.cursor tillater at man gjennomfør sql kommandoer
    mindatabase = pymysql.connect(host='localhost', port=3306, user='Biblioteksjef', passwd='bibliotek2018', db='Fagbokbibliotek')
    cursor = mindatabase.cursor()
    #Execute gjør at det kan utføres SQL spørringer
    cursor.execute("SELECT Bok.*, Eksemplar.EksNr FROM Bok LEFT JOIN Utlaan ON Bok.ISBN = Utlaan.ISBN LEFT JOIN Eksemplar ON Eksemplar.ISBN = Bok.ISBN WHERE Utlaan.UtlaansNR IS NULL")

    #------GUI------#
    #Lager hovedvindu
    root = Toplevel()
    
    #Oppretter tittel for vindu
    root.title('Oversikt over bøker som ikke er utlånt')
    
    #Lager tabellen inn i vindu
    Tabell = ttk.Treeview(root)
    
    #Fjerner første boksen
    Tabell['show'] = 'headings'
    
    #Lager kolonner
    Tabell["columns"]=("en","to","tre","fire","fem","seks", "syv")
    
    #Bestemmer lengde på kolonner
    Tabell.column("en", width=90)
    Tabell.column("to", width=120)
    Tabell.column("tre", width=110)
    Tabell.column("fire", width=100)
    Tabell.column("fem", width=70)
    Tabell.column("seks", width=70)
    Tabell.column("syv", width=70)

    #Bestemmer hva kolonnene skal hete
    Tabell.heading("en", text="ISBN")
    Tabell.heading("to", text="Tittel")
    Tabell.heading("tre", text="Forfatter")
    Tabell.heading("fire", text="Forlag")
    Tabell.heading("fem", text="UtgittAar")
    Tabell.heading("seks", text="AntallSider")
    Tabell.heading("syv", text="EksNr")

    #For loop for å sette inn verdier i radene
    #Row er hver linje inn i cursor
    for row in cursor:
        Tabell.insert("", 0, values=(row))

    Tabell.pack()
    
    #Gjør at vindu holder seg oppe
    root.mainloop()
    
#------------------------------------------------------------------------------
def statistikk_utlaan():
    mindatabase = pymysql.connect(host='localhost', port=3306, user='Biblioteksjef', passwd='bibliotek2018', db='Fagbokbibliotek')
    cursor = mindatabase.cursor()
    cursor.execute("SELECT Utlaan.*, Bok.Tittel FROM Utlaan JOIN Bok ON Utlaan.ISBN = Bok.ISBN")

    #Lager mainvindow med tittel
    root = Toplevel()
    root.title('Utlånsstatistikk for alle bøker samlet')

    #------GUI------#
    #Lager Treeview tabell som viser resultatet
    Tabell = ttk.Treeview(root)

    #Fjerner stor stygg hvit boks
    Tabell["show"] = "headings"

    #Angir antall columns og gir de angitt bredde
    Tabell["columns"]=("en","to","tre","fire","fem","seks", "sju")
    Tabell.column("en", width=60)
    Tabell.column("to", width=50)
    Tabell.column("tre", width=100)
    Tabell.column("fire", width=50)
    Tabell.column("fem", width=75)
    Tabell.column("seks", width=100)
    Tabell.column("sju", width=200)

    #Lager headings som sier hva dataen under er
    Tabell.heading("en", text="UtlånsNR")
    Tabell.heading("to", text="LNr")
    Tabell.heading("tre", text="ISBN")
    Tabell.heading("fire", text="EksNr")
    Tabell.heading("fem", text="Utlånsdato")
    Tabell.heading("seks", text="Innleveringsdato")
    Tabell.heading("sju", text="Tittel")

    #Forloop som inserter dataen i tabellen(Treeviewet)
    for row in cursor:
        Tabell.insert("", 0, values=(row))        

    #Packer Tabellen
    Tabell.pack()

    #Looper Mainvindu
    root.mainloop()
    
#------------------------------------------------------------------------------
def oversikt_laanetaker1():
    def oversikt_laanetaker2(event):
        valg = lst_laanetaker.get(lst_laanetaker.curselection())

        oversiktlaanetaker_markor = mindatabase.cursor()
        oversiktlaanetaker_markor.execute('SELECT LNr, Fornavn, Etternavn FROM Laaner')

        #Finne riktig lånetaker
        #Bruker FOR-løkke

        for row in oversiktlaanetaker_markor:
            if valg == row[0]:
                LNr.set(row[0])
                Fornavn.set(row[1])
                Etternavn.set(row[2])
        oversiktlaanetaker_markor.close()

    # Koble mot databasen
    mindatabase = pymysql.connect(host='localhost', port=3306, user='Biblioteksjef', passwd='bibliotek2018', db='Fagbokbibliotek')

    # Opprette courser/markør
    laanetaker_markor = mindatabase.cursor()

    # Henter vare data
    laanetaker_markor.execute('SELECT * FROM Laaner')

    # Oppretter liste
    laaner = []
    for row in laanetaker_markor:
        laaner +=[row[0]]

    #------GUI------#
    window = Toplevel()
    #Gir vinduet navn å lager scrollbar
    window.title("Oversikt Lånetaker")
    lbl_lånenummer=Label(window,text='Lånenummer:')
    lbl_lånenummer.grid(row=0,column=1,padx=5,sticky=N)
    y_scroll = Scrollbar(window, orient=VERTICAL)
    y_scroll.grid(row=0, column=2, rowspan=10, padx=(0, 100), pady=27, sticky=NS)

    #Fikser på scrollbar
    innhold_i_lst_laanetaker = StringVar()
    lst_laanetaker = Listbox(window, width=50, height=9, listvariable=innhold_i_lst_laanetaker, yscrollcommand=y_scroll.set)
    lst_laanetaker.grid(row=0, column=1, rowspan=50, padx=(20, 0), pady=5, sticky=E)
    innhold_i_lst_laanetaker.set(tuple(laaner))
    y_scroll["command"] = lst_laanetaker.yview

    #Overskrift
    lbl_Trykk=Label(window,text='Informasjon om lånetaker når du trykker på lånenummer:')
    lbl_Trykk.grid(row=0,column=3,padx=5,pady=5,sticky=W)

    #Ledertekster
    lbl_LNr = Label(window, text='Lånenummer:')
    lbl_LNr.grid(row=2, column=3, padx=5, pady=5, sticky=W)
    lbl_Fornavn = Label(window, text='Fornavn:')
    lbl_Fornavn.grid(row=3, column=3, padx=5, pady=5, sticky=W)
    lbl_Etternavn = Label(window, text='Etternavn:')
    lbl_Etternavn.grid(row=4, column=3, padx=5, pady=5, sticky=W)

    #Knytting av data til variabelen og utdatafelt
    LNr = StringVar()
    ent_LNr = Entry(window, width=4, state='readonly', textvariable=LNr)
    ent_LNr.grid(row=2, column=3, padx=90, pady=5, sticky=W)

    Fornavn = StringVar()
    ent_Fornavn = Entry(window, width=15, state="readonly", textvariable=Fornavn)
    ent_Fornavn.grid(row=3, column=3, padx=90, pady=5, sticky=W)

    Etternavn = StringVar()
    ent_Etternavn = Entry(window, width=30, state="readonly", textvariable=Etternavn)
    ent_Etternavn.grid(row=4, column=3, padx=90, pady=5, sticky=W)

    lst_laanetaker.bind('<<ListboxSelect>>', oversikt_laanetaker2)

    #Knapp for å lukke vinduet
    btn_return = Button(window, text='Avslutt', command=window.destroy)
    btn_return.grid(row=7, column=4, padx=5, pady=26, sticky=E)

    laanetaker_markor.close()


#------------------------- MAIN WINDOW GUI -------------------------#
window = Tk()

#Vi gir vinduet et navn
window.title('Fagbokbibliotek')

#Boks1
#Labels
lbl_Registrering=Label(window,text='Registrerings Oppgaver', font='Arial 9 bold')
lbl_Registrering.grid(row=0,column=0,padx=5,pady=5,sticky=N)

#Knapper
bt_beregn = Button(window,width=30, text='Registrere bruker', command= registrere_bruker)
bt_beregn.grid(row=1,column=0, padx=5, pady=3, sticky=N)

bt_beregn = Button(window,width=30, text='Registrere bok', command=legge_til_bok)
bt_beregn.grid(row=2,column=0, padx=5, pady=3, sticky=N)

bt_beregn = Button(window,width=30, text='Registrere eksemplar', command=legge_til_eksemplar)
bt_beregn.grid(row=3,column=0, padx=5, pady=3, sticky=N)
#Boks2
#Labels
lbl_Innlevering=Label(window,text='Innleveringer og Utlån', font='Arial 9 bold')
lbl_Innlevering.grid(row=0,column=1,padx=5,pady=5,sticky=N)

#Knapper
bt_beregn = Button(window,width=30, text='Innlevering av bøker', command=innleveringer1)
bt_beregn.grid(row=1,column=1, padx=5, pady=3, sticky=N)

bt_beregn = Button(window,width=30, text='Utlån av bøker', command=Registrere_utlån)
bt_beregn.grid(row=2,column=1, padx=5, pady=3, sticky=N)

bt_beregn = Button(window,width=30, text='Utlån som ikke er levert tilbake', command=ikke_levert)
bt_beregn.grid(row=3,column=1, padx=5, pady=3, sticky=N)
            

#Boks3
#Labels
lbl_SoO=Label(window,text='Statistikk og Oversikt', font='Arial 9 bold')
lbl_SoO.grid(row=0,column=2,padx=5,pady=5,sticky=N)

#Knapper
bt_beregn = Button(window,width=30, text='Bøker som ikke er utlånt', command=ulante_boker)
bt_beregn.grid(row=1,column=2, padx=5, pady=3, sticky=N)

bt_beregn = Button(window,width=30, text='Utlånsstatistikk alle bøker', command=statistikk_utlaan)
bt_beregn.grid(row=2,column=2, padx=5, pady=3, sticky=N)

bt_beregn = Button(window,width=30, text='Oversikt Lånetaker', command=oversikt_laanetaker1)
bt_beregn.grid(row=3,column=2, padx=5, pady=3, sticky=N)

#Knapp for å avslutte
btn_avslutte = Button(window, text='Avslutt', command=window.destroy)
btn_avslutte.grid(row=4, column=1, padx=2, pady=2, sticky=S)

window.mainloop()
#------------------------------------------------------------------------------
#End of Program
