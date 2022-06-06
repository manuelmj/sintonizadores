def lambdaTunning(kp:float,tao:float,t0:float)->dict:
   
    valoresLambda=(0.2*t0,t0,0)
    controladorTunning={}
    listaKc=[]

    for landa in valoresLambda:
        kc=tao/(kp*(landa+t0))
        listaKc.append(kc)
       

    #VALORES DEL CONTROLADOR P
    controladorTunning["P"]=[listaKc[2],"X","X"]
    #VALORES DEL CONTROLADOR PI
    controladorTunning["PI"]=[listaKc[1],tao,tao/60,"X"]
    #VALORES DEL CONTROLADOR PID
    controladorTunning["PID"]=[listaKc[0],tao,tao/60,t0/2,(t0/2)/60]

    return(controladorTunning)    

