con_odontologia = 0
con_ginecologia = 0
con_consultorioGenl = 0
con_maternidad = 0
con_infancia = 0
sw = True

def fnt_selector(op):
         
        global con_odontologia
        global con_ginecologia 
        global con_consultorioGenl
        global con_maternidad
        global con_infancia
        
        if op ==1:
            con_odontologia += 1
        if op ==2:

            con_ginecologia += 1
        if op == 3:
            con_consultorioGenl += 1
        if op == 4:
            con_maternidad += 1
        if op ==5:
            con_infancia += 1
           
def fnt_reporte():
    print ('la cantidad de registros en odontologia fue: ', con_odontologia)
    print ('la cantidad de registros en ginecologia fue: ', con_ginecologia)
    print ('la cantidad de registros en consultorio general fue: ', con_consultorioGenl)
    print ('la cantidad de registros en maternidad fue: ', con_maternidad)
    print ('la cantidad de registros en infancia fue: ', con_infancia)

while sw == True:  
        import os
        op = int(input('selecione que especialidad va a asistir\n1. Odontologia\n2. Ginecologia\n3. consultorioGenl\n4. maternidad\n5. infancia\n6. reporte-->'))
        fnt_selector(op)
        os.system('cls')
        if op <= 0 or op >= 7:
            print = ('opcion invalidad')
        if op == 6:
            fnt_reporte()
            break