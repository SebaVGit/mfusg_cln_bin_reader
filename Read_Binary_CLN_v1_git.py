# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 12:22:05 2020

@author: Sebastián Vázquez Gasty
"""
"""
----------------Comments-------------
This version use "WELLS" flags for the cell by cell file
in order to get the pumping rate directly from the
node with the well condition. The rest of the nodes will
have 0 instead.
---------------------------------------------------
"""

#------------------Imports----------------------------
import os
import sys
import numpy as np
import pandas as pd
import flopy.utils.binaryfile as bf
#-------------------Tiempo-----------------------------
import time
t = time.time()
#--------------Presentación-------------------------------
presentacion='CLN binary reader v1 GITHUB\nby Sebastián Vázquez Gasty\n'
print(presentacion)
#-----------------Read Binary File------------------
Ruta = os.getcwd() + '\\'

#--------------While Cycle------------------------
while True:
    try:
        archivo=input('Binary file name?: ')
        if not os.path.exists(Ruta+'\\'+archivo):
            raise ValueError
        break
    except ValueError:
        while True:
            try:
                err=int(input('This file does not exists, try it again [1] or exit [2]: '))
                break
            except ValueError:
                print('Oops! Must be a number between 1 or 2. Try it again...')                                
        if err==2:
            sys.exit('Good Bye')
while True:
    try:
        tipo=int(input('Concentration [1], head [2], Cell by Cell [3] or exit [4]: '))
        break
    except ValueError:
        print('Oops! Must be a number between 1 to 4. Try it again...')
#----------------Condición del tipo de archivo----------------------------
if tipo==1:
    conobj = bf.HeadFile(Ruta+'\\'+archivo, text='CONC')
    con=conobj.get_alldata()
    nodos=con.shape[3]
    con=con.reshape((con.shape[0],nodos))
    tiempo=np.asarray(conobj.get_times())
    tiempo=tiempo.reshape((tiempo.shape[0],1))
    kstpkper=np.asarray(conobj.get_kstpkper())+1 #(time step, stress period)
    matrix=np.concatenate((kstpkper,tiempo,con),axis=1)
    df = pd.DataFrame(matrix)
    columna=['Time Step','Stress Period','Time']
    for i in range(nodos):
        columna.append('CLN Node '+str(i+1))
    df.columns=columna 
    df.to_csv(Ruta+'\\Concentrationes_CLN.csv',index=False)
    print('\nConcentrationes_CLN.csv file has been created correctly')
elif tipo==2:
    hdobj = bf.HeadFile(Ruta+'\\'+archivo)
    hds=hdobj.get_alldata()
    nodos=hds.shape[3]
    hds=hds.reshape((hds.shape[0],nodos))
    tiempo=np.asarray(hdobj.get_times())
    tiempo=tiempo.reshape((tiempo.shape[0],1))
    kstpkper=np.asarray(hdobj.get_kstpkper())+1
    matrix=np.concatenate((kstpkper,tiempo,hds),axis=1)
    df = pd.DataFrame(matrix)
    columna=['Time Step','Stress Period','Time']
    for i in range(nodos):
        columna.append('CLN Node '+str(i+1))
    df.columns=columna 
    df.to_csv(Ruta+'\\Heads_CLN.csv',index=False)
    print('\nHeads_CLN.csv file has been created correctly')
elif tipo==3:
    cbb = bf.CellBudgetFile(Ruta+'\\'+archivo)
    kstpkper=cbb.get_kstpkper()
    largo=len(kstpkper)
    kstpkper=np.asarray(cbb.get_kstpkper())
    gwf=cbb.get_data(kstpkper=(0,0), text='WELLS')
    gwf=np.asarray(gwf)
    #If there is only one CLN node
    if gwf.size==1:
        dim=1
    else:
        dim=3
    nodos=gwf.shape[dim]
    gwf=gwf.reshape((1, nodos))
    for i in range(1,largo):
        aux=cbb.get_data(kstpkper=(kstpkper[i][0],kstpkper[i][1]), text='WELLS')
        aux=np.asarray(aux)
        aux=aux.reshape((1, aux.shape[dim]))
        gwf=np.vstack((gwf,aux))
    kstpkper=kstpkper+1
    matrix=np.concatenate((kstpkper,gwf),axis=1)
    df = pd.DataFrame(matrix)
    columna=['Time Step','Stress Period']
    for i in range(nodos):
        columna.append('CLN Node '+str(i+1))
    df.columns=columna 
    df.to_csv(Ruta+'\\Flux_CLN.csv',index=False)
    print('\nFlux_CLN.csv file has been created correctly')
else:
    sys.exit('Good Bye')

print('\nRun Time: '+str((time.time()-t)//60)+' minuts and '+('%.1f' %((time.time()-t)-60*((time.time()-t)//60)))+' seconds.')