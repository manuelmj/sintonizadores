import pandas as pd



def leerArchivo(archivo:str)->None:
    df = pd.read_csv(archivo)
    print(df)
    print(df.duplicated(df.columns[df.columns.isin(['temp'])]))
    df = df.drop_duplicates(df.columns[df.columns.isin(['temp'])],keep='first')
    print(df)
    
    nuevoCsv=pd.DataFrame(df)
    nuevoCsv.to_csv("nuevocsv.csv",index=False)
    


def main()->None: 
    archivo=input("ingrese su archivo:")
    leerArchivo(archivo)
    pass

if __name__ =="__main__":  
    main()