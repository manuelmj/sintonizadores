import math
import csv


def variableProceso(PVinicial: float = 0, PVfinal: float = 0) -> float:
    """" calcula el delta de la variable de proceso 

        devuelve el resultado de la diferencia entre 
        el valor inicial y el final de la variable de proceso

        parametros: 
        PVinicial: valor inicial de la variable de proceso
        PVfinal: valor  final de la variable de proceso
    """
    return(PVfinal-PVinicial)


def spamTransmisor(valorTransmisorMinimo: float, valorTransmisorMaximo: float) -> float:
    """calcula el spam del transmisor usado en el proceso de control 

        devuelve la diferencia entre el rango minimo y maximo que soporta el transmisor

        parametros: 
        valorTransmisorMinimo: valor minimo de la configuracion del transmisor
        valorTransmisorMaximo: valor maximo de la configuracion del transmisor
    """
    return(valorTransmisorMaximo-valorTransmisorMinimo)


def variableControl(deltaVariableProceso: float, spam: float) -> float:
    """calcula el valor de la variable de proceso 

        devulve el valor de la variable de proceso, el cual es el cociente
        entre el delta de la variable de proceso y  el espam del transmisor

        parametros: 
        deltaVariableProceso: el delta de la variable del proceso de control 
        spam: el spam del transmisor, es decir la diferencia entre el valor minimo y maximo 
              soportado por el transmisor 
    """

    return (deltaVariableProceso/spam)


def constanteProporcionalidadPK(variableControl: float, variableManipulada: float) -> float:
    """ calcula la constante de proporcionalidad 

        devuelve el valor absoludo de la constante de proporcionalidad 

        parametros: 
        variableControl: variable de control del proceso(deltaC)
        variableManipulada: variable manipulada del proceso (deltaM)
    """
    return abs(variableControl/variableManipulada)


def zonaseseintaytres(variableProceso: float, valorInicial: float) -> float:
    """ calcula la zona de crecimiento en el 63.2% 

        devuelve el el valor de la variable de controlada en el 63.2% del tiempo
        antes de la estabilidad 

        parametros: 
        variableProceso: variable del proceso de control (puede ser humedad,
                        temperatura o cualquier otra) 
        valorInicial: valor inicial de la variable de control antes de empezar
                     algun cambio en el proceso
    """
    return (variableProceso*(0.632) + valorInicial)


def zonaveintiocho(variableProceso: float, valorInicial: float) -> float:
    """ calcula la zona de crecimiento en el 28.3% 

        devuelve el el valor de la variable de controlada en el 28.3% del tiempo
        antes de la estabilidad 

        parametros: 
        variableProceso: variable del proceso de control (puede ser humedad,
                        temperatura o cualquier otra) 
        valorInicial: valor inicial de la variable de control antes de empezar
                     algun cambio en el proceso
    """

    return (variableProceso*(0.283) + valorInicial)


def calculoTao(tiempoZonaUno: float, tiempoZonaDos: float) -> float:
    """calcula la constante de Tao 

        devuelve la cosntante Tao, la cual se calcula con 
        el tiempo1(tiempo en el que la variable alcanzó el 28.3%)
        y  tiempo2(tiempo en el que la variable alcanzó el 63.2%)

        parametros: 
        tiempoZonaUno: tiempo en el que la variable alcanzó el 28.3% 
        tiempoZonaDos: tiempo en el que la variable alcanzó el 63.2%
    """
    return (3.0/2.0)*(tiempoZonaDos-tiempoZonaUno)


def calculoTiempoCero(tao: float, tiempoZonaDos: float) -> float:
    """ calcula el tiempo t0, o tiempo de retrazo o tiempo muerto 

    devuelve el valor de t0 

    parametros: 
    tao: constante Tao 
    tiempoZonaDos:  tiempo en el que la variable alcanzó el 63.2%
    """
    return (tao-tiempoZonaDos)


def leer_archivo(nombreArchivo: str) -> list:
    """ devuelve una lista con los valor numericos leidos desde unarchivo en formato csv 
        el cual contiene los valor del cambio en una tabla

        parametros: 
        nombreArchivo: nombre del archivo en formato csv del que se van a leer los datos      
    """
    
    listaDatosTiempo=[]
    listaDatosValores=[]
    
    with open(nombreArchivo, newline='') as File:
        archivo = csv.reader(File)
        for filas in archivo:

            listaDatosTiempo.append(float(filas[0]))
            listaDatosValores.append(float(filas[1]))


    return [listaDatosTiempo,listaDatosValores]

def interpolacionLineal(listaTiempo:list,listaValores:list,valorConocido)->float:
    """
    calcual la interpolacion lineal de un valor que se encuentra dentro de la tabla 

    devuelve el el valor correspondiente al tiempo del valor de la lectura que se interpoló

    parametros: 
    listaTiempo: lista con los valores del tiempo en el que se hicieron las mediciones 
    listaValores: lista con los valores del la variable examinada 
    valorConocido: valor conocido del cual se quiere interpolar el tiempo 
    """
    resultado=[]
    indice=0
    resultado=[valor for valor in listaValores if (valor==valorConocido)]
    if resultado:
        indice = resultado.index(resultado[0])
        return listaTiempo[indice]

    ultimo=listaValores.pop() 
    listaValores.append(ultimo)
    primero=listaValores[0]

    if (ultimo>primero):

        for valor in listaValores:
            if(valorConocido<valor):
                indice=listaValores.index(valor)
                valor1=listaValores[indice-1]
                resultado.append(valor1)   #y1    
                resultado.append(valor)     #y2
                break
    else : 

        for valor in listaValores:
            if(valorConocido>valor):
                indice=listaValores.index(valor)
                valor1=listaValores[indice-1]
                resultado.append(valor1)   #y1    
                resultado.append(valor)     #y2
                break
    
    if not(resultado):
        return(0)

    indice2=indice-1   
    y1=listaTiempo[indice2]
    y2=listaTiempo[indice]
    x1=resultado[0]
    x2=resultado[1]
    resultadoInterpolacion=y1+((y2-y1)/(x2-x1))*(valorConocido-x1)
 
    return(resultadoInterpolacion)
