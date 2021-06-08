import  json
x=False
while not x:
    try:
        archivoUsuarios= open("usuarios.json","r", encoding= "utf-8") #Se abre el archivo de usuarios en modo lectura y se arregla el error de la ortografía
        x=True
    except IOError:
        print("Error de entrada/salida")

Usuarios= json.load (archivoUsuarios) #Se guarda el archivo en una variable
y=False
while not y:
    try:
        archivoParqueaderos = open("tiposParqueaderos.json","r") #Se abre el archivo de tipos de parqueaderos en modo lectura 
        y=True
    except IOError:    
       print("Error de entrada/salida") 

parqueaderos= json.load(archivoParqueaderos)#Se guarda el archivo en una variable
z=False
while not z:
    try:
        archivOParqueaderos= open("ocupacionParqueaderos.json","r")#Se abre el archivo de tipos de parqueaderos en modo lectura 
        z=True
    except IOError:
        print("Error de entrada/salida") 

OcupacionParqueaderos= json.load(archivOParqueaderos)#Se guarda el archivo en una variable
 
def f_registroPersona (basedeusuarios):
    lista=[]#se crea lista que tendra los datos que el usuario ingrese
    print("*Bienvenido al registro de tu vehiculo*")
    pregunta=eval(input("¿eres estudiante,profesor o personal administrativo?\n1.Si\n2.No\n"))#se valida porqué solo se puede registrar si es uno de estos tres 
    if pregunta==1:
        print("Por favor ingresa: ")
        nombre=input("nombre y apellidos: ")
        lista.append(nombre)
        id=eval(input("número de indentificación: "))
        lista.append(id)
        Tusuario=eval(input("Tipo de usuario:\n1.Estudiante\n2.Profesor\n3.Personal Administrativo\n"))
        if (Tusuario==1):
            Tusuario="Estudiante"
        elif Tusuario==2:
            Tusuario="Profesor"
        elif Tusuario==3:
            Tusuario="Personal Administrativo" 
        lista.append(Tusuario)
        Placa=input("Placa: ")
        lista.append(Placa)
        Tvehiculo=eval(input("ingresa el número correspondiente al tipo de vehiculo que va entrar:\n1.Automóvil\n2.Automóvil Eléctrico\n3.Motocicleta\n4.Discapacitado\n"))
        if Tvehiculo==1:
            Tvehiculo="Automóvil"
        elif Tvehiculo==2:
            Tvehiculo="Automóvil Eléctrico"
        elif Tvehiculo==3:
            Tvehiculo="Motocicleta"
        elif Tvehiculo==4:
            Tvehiculo="Discapacitado"
        lista.append(Tvehiculo)
        Ppago=input("ingresa el número correspondiente al plan de pago del vehiculo que va entrar:\n1.Mensualidad\n2.Diario\n")
        if Ppago=="1":
            Ppago="Mensualidad"
        elif Ppago=="2":
            Ppago="Diario"
        lista.append(Ppago)# se terminan de ingresar todos los datos a la lista
        datosUsuarios=basedeusuarios["usuarios"] #se define la variable que tendra la lista de las listas de cada usuario
        aux1=0 #se inicializa la variable
        aux2=0#se inicializa la variable
        aux3=0#se inicializa la variable
        for y in datosUsuarios:
            aux1+=1# aux1 contara todos los usuarios que hay
            if id!=y[1]:#este condicional valida que la identificación del usuario de este vehiculo sea distinta a los vehiculos ya registrados
                aux2+=1 #contara todos los vehiculos que tengan id diferente al vehiculo nuevo
            else:
                aux3+=1#si la id del usuario nuevo es igual a la de un auto ya registrado, se suma 1
        if aux1==aux2:# valida que todos los autos ya registrados tengan un id diferente al auto que se desea registrar
            datosUsuarios.append(lista)#se añade al final la lista de los datos del vehiculo nuevo
            basedeusuarios["usuarios"]=datosUsuarios# se redefine la base de usuarios actualizada con el vehiculo nuevo
            with open ("usuarios.json","w",  encoding="utf-8") as file:#se abre el archivo json que queremos actualizar
                json.dump(basedeusuarios,file,indent=4,ensure_ascii = False)#se actualiza la base de usuarios con el vehiculo nuevo en el archivo json
                print("Se han ingresado sus datos a la base de usuarios.")

        if aux3!=0: #si hay aunque sea un carro ya registrado con la id, no puede ingresar otro vehiculo
            print("Lo siento, no puedes ingresar más de un vehiculo.")
    else:#la persona no es estudiante, personal administrativo o profesor, por lo tanto no se puede registrar
        print("Lo siento, si no eres estudiante, personal administrativo o profesor NO puedes registrarte.")



def f_ingresoVehiculo(basedeusuarios,OcupacionParqueaderos):#la que retorna la funcion anterior
    res1=False #variable que controla el ciclo
    while not res1: #validamos que la placa no esté más de una vez en el parqueadero
        lista=[]#se inicializa la lista
        print("*Bienvenido al ingreso del vehiculo*, por favor ingresa: ")
        Placa=input("Placa: ")
        datosUsuarios=basedeusuarios["usuarios"]#se define la variable que tendra la lista de las listas de cada usuario
        aux1=0
        aux2=0
        aux3=0
        res=0
        for piso in OcupacionParqueaderos:
            w=OcupacionParqueaderos[piso]
            for parqueaderos in w:
                for parqueadero in parqueaderos:
                    if parqueadero[1]!=0:
                        if parqueadero[1][0]==Placa:
                            res+=1
        if res==0: #cuando sabemos que no esta dos veces, procedemos.
            for x in datosUsuarios: #x es cada lista de datos de los vehiculos registrados
                aux1+=1 #aux1 contara todos los vehiculos registrados
                #se compara la placa de cada vahiculo registrado en el sistema con la placa del auto que ingresa.
                if x[3]!=Placa:#si las placas son diferentes
                    aux2+=1#variable que cuenta las placas diferentes
                else:#si las placas son iguales, el vehiculo ya está registrado
                    Tusuario= x[2]#se toma de la lista de datos del vehiculo el tipo de usuario 
                    Ppago=x[5]#se toma de la lista de datos del vehiculo el tipo de pago
                    tv=x[4]
            if aux1==aux2:# si todas las placas de los vehiculos registrados son diferentes a la placa ingresada, haga lo siguiente:
                    Tusuario="Visitante"#el vehiculo es un visitante
                    Ppago="Diario"#su tipo de pago es diario
                    tv=int(input("ingresa el número correspondiente al tipo de vehiculo que va entrar:\n1.Automóvil\n2.Automóvil Eléctrico\n3.Motocicleta\n4.Discapacitado\n"))
            lista.append(Placa)
            lista.append(Tusuario)
            lista.append(Ppago)
            res1=True
        else:
            print("No puedo ingresar la misma placa dos veces, inténtelo de nuevo.")

    #la lista es placa, tipo de usuario y tipo de pago
    return lista, tv #se retorna la lista de los datos del vehiculo que ingresa

def f_Pdisponibles (listadatosvehiculo,OcupacionParqueaderos,tv):
    disponibles=0
    aux1=0
    tvE=0
    if tv==1 or tv=="Automóvil":#se compara de las dos formas para que sea valido para usuarios registrados y usuarios nuevos
        tv="Automóvil"
        tvE=1# va a mantener el tipo de vehiculo del usuario como numero para poderlo comparar con el tipo de vehiculo de cada parqueadero
    elif tv==2 or tv=="Automóvil Eléctrico":#se compara de las dos formas para que sea valido para usuarios registrados y usuarios nuevos
        tv="Automóvil Eléctrico"
        tvE=2# va a mantener el tipo de vehiculo del usuario como numero para poderlo comparar con el tipo de vehiculo de cada parqueadero
    elif tv==3 or tv=="Motocicleta":#se compara de las dos formas para que sea valido para usuarios registrados y usuarios nuevos
        tv="Motocicleta"
        tvE=3# va a mantener el tipo de vehiculo del usuario como numero para poderlo comparar con el tipo de vehiculo de cada parqueadero
    elif tv==4 or tv=="Discapacitado":#se compara de las dos formas para que sea valido para usuarios registrados y usuarios nuevos
        tv="Discapacitado"
        tvE=4# va a mantener el tipo de vehiculo del usuario como numero para poderlo comparar con el tipo de vehiculo de cada parqueadero

    for piso in OcupacionParqueaderos:#se recorre las llaves del parqueadero, que en este caso son los pisos
        x=OcupacionParqueaderos[piso] # X es el contenido de cada piso
        disponiblespiso=0 
        noDisponibles=0
        for parqueaderos in x: #se recorren las lineas de los parqueaderos
            for parqueadero in parqueaderos: #se recorre cada parqueadero de cada linea
                aux1+=1 #aux1 contara todos los parqueaderos del piso
                if tv=="Automóvil":# si el tipo de vehiculo es Automóvil
                    if parqueadero[0]==tvE and parqueadero[1]==0: #si el parqueadero es del tipo de vehiculo y el parqueadero está vacio 
                        disponiblespiso+=1 #se suma uno a los disponibles del piso
                        disponibles+=1 #se suma uno a los disponibles del parqueadero 
                    else:#si no es del tipo de vehiculo o si el parqueadero está ocupado.
                        noDisponibles+=1 #no está disponible
                elif tv=="Automóvil Eléctrico":# si el tipo de vehiculo es Automóvil Eléctrico
                    if (parqueadero[0]==tvE or parqueadero[0]==1) and parqueadero[1]==0:#si el parqueadero es del tipo de vehiculo y el parqueadero está vacio 
                        disponibles+=1  #se suma uno a los disponibles del piso
                        disponiblespiso+=1#se suma uno a los disponibles del parqueadero 
                    else:#si no es del tipo de vehiculo o si el parqueadero está ocupado.
                        noDisponibles+=1#no está disponible
                elif tv=="Motocicleta":# si el tipo de vehiculo es Motocicleta
                        if parqueadero[0]==tvE and parqueadero[1]==0:#si el parqueadero es del tipo de vehiculo y el parqueadero está vacio 
                            disponibles+=1 #se suma uno a los disponibles del piso
                            disponiblespiso+=1 #se suma uno a los disponibles del parqueadero   
                        else:#si no es del tipo de vehiculo o si el parqueadero está ocupado.
                            noDisponibles+=1#no está disponible
                elif tv=="Discapacitado":# si el tipo de vehiculo es Discapacitado
                        if (parqueadero[0]==tvE or parqueadero[0]==1)and parqueadero[1]==0:#si el parqueadero es del tipo de vehiculo y el parqueadero está vacio 
                            disponibles+=1 #se suma uno a los disponibles del piso
                            disponiblespiso+=1 #se suma uno a los disponibles del parqueadero 
                        else:#si no es del tipo de vehiculo o si el parqueadero está ocupado.
                            noDisponibles+=1#no está disponible
        if aux1==noDisponibles:# todos los parqueaderos están ocupados
            print("no hay ningun espacio disponible para este tipo de vehiculo en el "+str(piso))
        else:#si hay aunque sea 1 parquedero disponible en el piso, lo imprime.
            print("el total de parqueaderos disponibles en "+str(piso)+" es de:"+str(disponiblespiso))

    if disponibles==0:#todos los parqueaderos están ocupados
        print("no hay ningun espacio disponible para este tipo de vehiculo en todo el edificio")
    else: #empieza la parte de la gráfica, si hay aunque sea un parqueadero disponible 
        pisoP=eval(input("ingresa el número del piso que deseas ingresar:\n1.Piso 1\n2.Piso 2\n3.Piso 3\n4.Piso 4\n5.Piso 5\n6.Piso 6\n"))
        if pisoP==1:
            pisofinal="Piso1"
            pisoR=OcupacionParqueaderos["Piso1"]#La variable pisoR son los datos de los parqueaderos del piso
        elif pisoP==2:
            pisofinal="Piso2"
            pisoR= OcupacionParqueaderos["Piso2"]#La variable pisoR son los datos de los parqueaderos del piso
        elif pisoP==3:
            pisofinal="Piso3"
            pisoR= OcupacionParqueaderos["Piso3"]#La variable pisoR son los datos de los parqueaderos del piso
        elif pisoP==4:
            pisofinal="Piso4"
            pisoR= OcupacionParqueaderos["Piso4"]#La variable pisoR son los datos de los parqueaderos del piso
        elif pisoP==5:
            pisofinal="Piso5"
            pisoR= OcupacionParqueaderos["Piso5"]#La variable pisoR son los datos de los parqueaderos del piso
        elif pisoP==6:
            pisofinal="Piso6"
            pisoR= OcupacionParqueaderos["Piso6"]#La variable pisoR son los datos de los parqueaderos del piso
        variable= False #variable de control del ciclo
        while not variable:#mientras el usuario no haya ingresado las coordenadas correctamente, se repite
            grafico=""
            for parqueaderos in pisoR:# se recorre las lineas de los parqueaderos del piso que haya escogido(matrices)
                for y in parqueaderos:# se recorren los parqueaderos de cada linea de parqueaderos(listas)
                    if tvE==1:# si el tipo de vehiculo es Automóvil
                        if y[0]==tvE and y[1]==0:# si el parqueadero es del mismo tipo de vehiculo y está desocupado
                            grafico+=" 0 " #vacia
                        else:
                            grafico+=" X "#ocupada
                    elif tvE==2:# si el tipo de vehiculo es Automóvil Eléctrico
                        if (y[0]==tvE or y[0]==1) and y[1]==0:# si el parqueadero es del mismo tipo de vehiculo o es tipo Automóvil, y está desocupado
                            grafico+=" 0 " #vacia
                        else:
                            grafico+=" X "#ocupada
                    elif tvE==3:# si el tipo de vehiculo es Motocicleta
                        if y[0]==tvE and y[1]==0:# si el parqueadero es del mismo tipo de vehiculo y está desocupado
                            grafico+=" 0 " #vacia
                        else:
                            grafico+=" X "#ocupada
                    elif tvE==4:# si el tipo de vehiculo es Discapacitado
                        if (y[0]==tvE or y[0]==1) and y[1]==0:# si el parqueadero es del mismo tipo de vehiculo o es tipo Automóvil, y está desocupado
                            grafico+=" 0 " #vacia
                        else:
                            grafico+=" X "#ocupada
                grafico+= "\n" #se hace un espacio por cada linea de parqueaderos                               
            print("*las X son los parqueaderos no disponibles y los 0 son los parqueaderos disponibles*")
            print(grafico) 
            print("ahora, ingresa los siguientes detalles del parqueadero que escogas: ")
            pY=eval(input("escribe el número de linea en que se encuentra (En este sentido →): "))#esta variable la utilizamos para ubicar la linea  del parqueadero que eligio
            pY-=1#cómo el usuario no sabe que las posiciones de las listas empiezan en 0 en vez de 1, se le resta 1 al valor que indique
            pX=eval(input("escribe el número de columna en que se encuentra(En este sentido ↓) : "))#esta variable la utilizamos para ubicar la columna del parqueadero que eligio
            pX-=1#cómo el usuario no sabe que las posiciones de las listas empiezan en 0 en vez de 1, se le resta 1 al valor que indique


            if  OcupacionParqueaderos[pisofinal][pY][pX][1]==0 and OcupacionParqueaderos[pisofinal][pY][pX][0]==tvE:#se está validando que el parqueadero que escogio esté libre y que sea del mismo tipo de vehiculo
                OcupacionParqueaderos[pisofinal][pY][pX][1]=listadatosvehiculo #se actualiza el archivo agregando al parqueadero que escoga los datos del vehiculo
                with open ("ocupacionParqueaderos.json","w") as file:#se abre el archivo que queremos actualizar
                    json.dump(OcupacionParqueaderos,file)#se actualiza el archivo de la ocupación de los parquederos con con el vehiculo nuevo en el archivo json
                file.close()
                print("su vehiculo ha sido ingresado exitosamente.")
                variable=True #se actualiza la variable a True indicando que el usuario ingreso exitosamente, para que salga del ciclo
            elif OcupacionParqueaderos[pisofinal][pY][pX][1]!=0 or OcupacionParqueaderos[pisofinal][pY][pX][0]!=tvE:#el parqueadero que escogió no está libre o no tiene el mismo tipo de vehiculo
                print("Ingresaste un parqueadero que está ocupado o es para un distinto tipo de vehiculo, intentalo de nuevo.")

def f_cobro (ocupaciónparqueadero):
    placa=input("Ingrese su numero de placa: ")
    Tusuario=0
    t=eval(input("Ingrese el numero de horas que estuvo en el parqueadero: "))
    if t<1:
        t=1
    z=0#variable que cuenta 
    a=0 #variable que cuenta todos los parqueaderos 
    cobrominuto=0 #variable que cuenta cuando la placa no está en el parqueadero
    for piso in ocupaciónparqueadero:#se recorre las llaves del parqueadero, que en este caso son los pisos
        x=ocupaciónparqueadero[piso]# X es el contenido de cada piso
        for parqueaderos in x:#se recorren las lineas de los parqueaderos
                for y in parqueaderos:#se recorre cada parqueadero de cada linea
                    a+=1 # la variable "a" cuenta todos los parqueaderos
                    if y[1]!=0:# se valida que el parqueadero esté ocupado
                        if y[1][0]==placa:#la lista es placa, tipo de usuario y tipo de pago
                            Tusuario=y[1][1]#se saca el tipo de usuario de la lista
                            if(y[1][2]=="Mensualidad"):
                                print("No debe realizar ningun pago debido a que tiene un plan mensual") 
                            elif(y[1][2]=="Diario"):# si el tipo de pago es diario, se hacen los debidos calculos según el tipo de estudiante
                                if(Tusuario=="Estudiante"):
                                    cobrominuto=(t*1000)
                                elif(Tusuario=="Profesor"):
                                    cobrominuto=(t*2000)
                                elif(Tusuario=="Personal Administrativo"):
                                    cobrominuto=(t*1500)
                                elif(Tusuario=="Visitante"):
                                    cobrominuto=(t*3000)
                                print("Tienes que pagar:$"+str(cobrominuto)+" pesos.")
                                print("Vuelva pronto.")
                            y[1]=0#se desocupa el parqueadero en el que estaba el vehiculo
                        else:
                            z+=1 
                    else:
                        z+=1
    if z==a:#validación de que la placa NO está en ningún parqueadero
        print("lo siento, su placa no está almacenada dentro del parqueadero.")                   
    with open("ocupacionParqueaderos.json","w") as file:#se abre el archivo que queremos actualizar
        json.dump(ocupaciónparqueadero,file)#se actualiza el archivo de la ocupación de los parquederos sacando los datos del vehiculo del archivo json
    file.close()

def f_reportes(OcupacionParqueaderos):
    print("\n*Bienvenido a la sección de reportes*")
    print("1.Reporte con la cantidad de vehículos estacionados según el tipo de usuario\n2.Reporte de cantidad de vehículos estacionados según el tipo de vehículo\n3.Reporte que indique el porcentaje de ocupación del parqueadero y sus pisos")    
    pregunta=eval(input("escribe el número de la opción que deseas seleccionar: "))   
    #Como se entra a un ciclo, se deben inicializar las variables
    reporteTotalV1=0#cantidad de automoviles
    reporteTotalV2=0#cantidad de automoviles eléctricos
    reporteTotalV3=0#cantidad de motocicletas
    reporteTotalV4=0#cantidad de vehiculos de discapacitados
    reporteTotalU1=0#cantidad de estudiantes
    reporteTotalU2=0#cantidad de profesores
    reporteTotalU3=0#cantidad de personal administrativo
    reporteTotalU4=0#cantidad de visitantes
    ocupacionglobal=0#porcentaje de ocupación de vehiculos en la totalidad del parqueadero
    ocupaciónP1=0#porcentaje de ocupación del piso 1
    ocupaciónP2=0#porcentaje de ocupación del piso 2
    ocupaciónP3=0#porcentaje de ocupación del piso 3
    ocupaciónP4=0#porcentaje de ocupación del piso 4
    ocupaciónP5=0#porcentaje de ocupación del piso 5
    ocupaciónP6=0#porcentaje de ocupación del piso 6
    for pisos in OcupacionParqueaderos: #se recorre las llaves del parqueadero, que en este caso son los pisos
        x=OcupacionParqueaderos[pisos]# X es el contenido de cada piso
        for parqueaderos in x:#se recorren las lineas de los parqueaderos
            for parqueadero in parqueaderos:#se recorre cada parqueadero de cada linea
                if parqueadero[1]!=0:#si el parqueadero está ocupado, hace lo siguiente.
                    ocupacionglobal+=1#se suma 1 a la ocupación de todo el parqueadero
                    if pisos=="Piso1": 
                        ocupaciónP1+=1
                    elif pisos=="Piso2":
                        ocupaciónP2+=1
                    elif pisos=="Piso3":
                        ocupaciónP3+=1                
                    elif pisos=="Piso4":
                        ocupaciónP4+=1
                    elif pisos=="Piso5":
                        ocupaciónP5+=1
                    elif pisos=="Piso6":
                        ocupaciónP6+=1

                    if parqueadero[0]==1:
                        reporteTotalV1+=1
                    elif parqueadero[0]==2:
                        reporteTotalV2+=1
                    elif parqueadero[0]==3: 
                        reporteTotalV3+=1                   
                    elif parqueadero[0]==4:
                        reporteTotalV4+=1
                    
                    if parqueadero[1][1]=="Estudiante":
                        reporteTotalU1+=1
                    elif parqueadero[1][1]=="Profesor":
                        reporteTotalU2+=1
                    elif parqueadero[1][1]=="Personal Administrativo":
                        reporteTotalU3+=1
                    elif parqueadero[1][1]=="Visitante":
                        reporteTotalU4+=1
        archivOParqueaderos.close()

        PocupacionGlobal=(ocupacionglobal/550)*100#calculo del porcentaje de ocupación global
        PocupacionP1=(ocupaciónP1/100)*100#calculo del porcentaje de ocupación del piso 1
        PocupacionP2=(ocupaciónP2/100)*100#calculo del porcentaje de ocupación del piso 2
        PocupacionP3=(ocupaciónP3/100)*100#calculo del porcentaje de ocupación del piso 3
        PocupacionP4=(ocupaciónP4/100)*100#calculo del porcentaje de ocupación del piso 4
        PocupacionP5=(ocupaciónP5/100)*100#calculo del porcentaje de ocupación del piso 5
        PocupacionP6=(ocupaciónP6/50)*100#calculo del porcentaje de ocupación del piso 6

        if pregunta==1:
            with open ("Reporte1.txt","w") as archivo:#se crea el archivo de texto del reporte 1
                archivo.write("La cantidad de vehiculos de usuarios profesores es: "+str(reporteTotalU2)+"\n")        
                archivo.write("La cantidad de vehiculos de usuarios estudiantes es: "+str(reporteTotalU1)+"\n")
                archivo.write("La cantidad de vehiculos de usuarios personal administrativo es: "+str(reporteTotalU3)+"\n")
                archivo.write("La cantidad de vehiculos de usuarios visitantes es: "+str(reporteTotalU4)+"\n") 
                archivo.close() 
                print("Su reporte se guardó exitosamente.")     

        elif pregunta==2:
            with open ("Reporte2.txt","w") as archivo:#se crea el archivo de texto del reporte 2
                archivo.write("La cantidad de vehiculos del tipo automovil es: "+str(reporteTotalV1)+"\n")
                archivo.write("La cantidad de vehiculos del tipo automovil eléctrico es: "+str(reporteTotalV2)+"\n")        
                archivo.write("La cantidad de vehiculos del tipo motocicleta es: "+str(reporteTotalV3)+"\n")
                archivo.write("La cantidad de vehiculos del tipo discapacitado es: "+str(reporteTotalV4)+"\n")   
                archivo.close() 
                print("Su reporte se guardó exitosamente.")  
        elif pregunta==3:

            with open ("Reporte3.txt","w") as archivo:#se crea el archivo de texto del reporte 3
                archivo.write("El porcentaje de ocupación del parqueadero es del: "+str(PocupacionGlobal)+"%.\n")
                archivo.write("El porcentaje de ocupación del piso 1 es de: "+str(PocupacionP1)+"%.\n")
                archivo.write("El porcentaje de ocupación del piso 2 es de: "+str(PocupacionP2)+"%.\n")
                archivo.write("El porcentaje de ocupación del piso 3 es de: "+str(PocupacionP3)+"%.\n")
                archivo.write("El porcentaje de ocupación del piso 4 es de: "+str(PocupacionP4)+"%.\n")
                archivo.write("El porcentaje de ocupación del piso 5 es de: "+str(PocupacionP5)+"%.\n")
                archivo.write("El porcentaje de ocupación del piso 6 es de: "+str(PocupacionP6)+"%.\n")
                archivo.close()
                print("Su reporte se guardó exitosamente.")  

print("*Bienvenido al sistema de administración de parqueaderos*")
print("*Hecho por Susana Valencia y José Andrade*")
opción=0
w=False#variable de control
while not w: #mientras el usuario no digite un valor númerico
    try:
        while opción!=5:#mientras el usuario no quiera salir, volvera a pedir que escoga una opción
            print("1.Registro de vehiculo\n2.Ingreso de vehiculo a parqueadero\n3.Retiro de vehiculo\n4.Reportes\n5.Salir\n")
            opción=eval(input("por favor escriba el número de la opción que desea utilizar: "))
            if opción==1:
                f_registroPersona(Usuarios)# función de ingresar nuevo usuario
            elif opción==2:
                listaDatosVehiculo, tv=f_ingresoVehiculo(Usuarios,OcupacionParqueaderos)#función de hacer lista de datos de vehiculo que ingresa
                f_Pdisponibles(listaDatosVehiculo,OcupacionParqueaderos,tv)#función que muestra parqueaderos disponibles e ingresa el vehiculo al sistema
            elif opción==3:
                f_cobro(OcupacionParqueaderos)#función de salida de vehiculo, se realiza el cobro
            elif opción==4:
                f_reportes(OcupacionParqueaderos)#funcion de reportes 
        w=True
    except NameError:
        print("El número ingresado no es valido")
archivoUsuarios.close()
archivoParqueaderos.close()

print("Ha finalizado su proceso, muchas gracias.")