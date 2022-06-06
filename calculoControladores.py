from calculosPrevios import variableProceso,spamTransmisor,variableControl
from calculosPrevios import constanteProporcionalidadPK,zonaveintiocho,zonaseseintaytres 
from calculosPrevios import calculoTao,calculoTiempoCero,leer_archivo,interpolacionLineal

from sintonizadores import lambdaTunning



def main() -> None:
    print("*************************************************************")
    print("-------------------------------------------------------------")
    print("|    BIENVENIDO AL CALCULO DE VALORES PARA SU CONTROLADOR   |")
    print("-------------------------------------------------------------")
    print("*************************************************************")
    print("\r\n\r\n")
    print(">>>>>DEBERÁ INGRESAR LOS SIGUIENTES DATOS<<<<<<<")

#-------------------------------------------------------------------------------------#
    listaDatos=[]
    listaTiempo=[]
    print("-------------------------------------------------------------------------------")
    nombreArchivo = str(
        input("\r\n ingrese el nombre del archivo que desea leer ->>>"))
    print("--------------------------------------------------------------------------------")
    listaTiempo,listaDatos = leer_archivo(nombreArchivo)
    primerValor = listaDatos[0]
    ultimoValor = listaDatos.pop()
    listaDatos.append(ultimoValor)

    VariableProceso = variableProceso(primerValor, ultimoValor)
#----------------------------------------------------------------------------------#

    print("--------------------------------------------------------------------------------")
    numerosSpam = str(
        input("ingrese el rango minimo y maximo del sensor (ejemplo: 1:10) ->>>"))
    print("--------------------------------------------------------------------------------")
    numerosSpam = numerosSpam.split(":")
    numerosSpam = [float(numeros) for numeros in numerosSpam]
    Spam = spamTransmisor(numerosSpam[0], numerosSpam[1])
#-------------------------------------------------------------------------------------------#
    VariableC = variableControl(VariableProceso, Spam)
    VariableC *= 100
#-------------------------------------------------------------------------------------------#

    print("--------------------------------------------------------------------------------")
    variablemanipulada = float(input("ingrese el porcentaje de la variable manipulada  ->>>"))
    print("--------------------------------------------------------------------------------")

    constanteProporcionalidad = constanteProporcionalidadPK(VariableC, variablemanipulada)
    
#--------------------------------------------------------------------------------------------#

    primeraZona = zonaveintiocho(VariableProceso, primerValor)
    segundaZona = zonaseseintaytres(VariableProceso, primerValor)
    print("el porcentaje al 28.3 es >>{zona1}<< y al 63.2 es >>{zona2}<<".format(zona1=primeraZona, zona2=segundaZona))
#----------------------------------------------------------------------------------------------#
    t1=interpolacionLineal(listaTiempo,listaDatos,primeraZona)
    t2=interpolacionLineal(listaTiempo,listaDatos,segundaZona)
    tao=calculoTao(t1,t2)
    t0=calculoTiempoCero(tao,t2) 
    sintionia=1

    while(sintionia):
        print("#############################################################")
        print("|                    SINTONIZACIONES:                       |")
        print("#############################################################")

        sintionia = int(input("""
        (1) para lambda Tunning 
        (0) Para salir
        -> """))
        print("--------------------------------------------------------------------------------")
        listaConstante=["constante Kc    ","tiempo integral(s)","tiempo integral(m)","tiempo derival (s)","tiempo derival(m)"]
        
    #-----------------------LAMBDA  TUNNING ---------------------------------------------------------------------------------------    
    
        if (sintionia==1):
          
            print("""
            Variable de proceso :  {varProceso}
            Variable manipulada :  {varManipulada}%
            Variable controlada :  {varControlada}
            spam                :  {varspam}
            constante de proporcionalidad: {varPropor}
            """.format(varProceso=VariableProceso,varManipulada=variablemanipulada,
                        varspam=Spam, varControlada=VariableC/100,varPropor=constanteProporcionalidad))

            print("TAO={Tao}\n T0={T0}\n Kp={Kp}".format(Tao=tao,T0=t0,Kp=constanteProporcionalidad))

            tunning=lambdaTunning(constanteProporcionalidad,tao,abs(t0))
            print("\r\n-----------------------------------------------------------------------------")
            i=0

            print("**************************************************************************")
            for valores in tunning:
                print("\t",valores)

                for dato in tunning[valores]:
                    print("{indice}\t-> \t{dato}".format(indice=listaConstante[i],dato=dato))
                    i+=1
                i=0
                print("\r\n\r\n")
            print("**************************************************************************")

   #-----------------------------FIN LAMBDA TUNNING -----------------------------------------------------------         
    



if __name__ == "__main__":
    main()
