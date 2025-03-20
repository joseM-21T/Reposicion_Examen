def cargar_dataset(archivo):
    import pandas as pd
    import numpy as np
    import os

    extension = os.path.splitext(archivo)[1].lower()
    if extension == '.csv':
        df = pd.read_csv(archivo)
        return (df)
    elif extension == '.html':
        df = pd.read_html(archivo)
        return(df)
    else:
        raise ValueError(f"Hola, acabas de ingresar un documento que desconozco, con extension: {extension}")

#2.Sustituye los valores nulos de las variables de las columnas primas (0,1, 2, 3, 5, 7, 11, 13…etc.) con la 
#constante numérica  “1111111” y de las demás columnas numéricas con la constante “1000001”. Las columnas que 
#no sean de tipo numérico se sustituirán con el string “Valor Nulo”
def reemplazar_nulos(df):
    import pandas as pd
    import numpy as np
    import os

    prim = []
    for num in range(len(df.columns)):
        if num > 1 and all(num % div != 0 for div in range(2, int(num**0.5) + 1)):
            prim.append(num)
    
    colum = df.columns.to_list()
    
    for i in range(len(colum)):
        col = colum[i]
        if df[col].dtype in [np.int64, np.float64]:  
            if i in prim:
                df[col].fillna(1111111, inplace=True)
            else:
                df[col].fillna(1000001, inplace=True)
        else: 
            df[col].fillna("Valor nulo", inplace=True)
    
    return df


#3.Identifica los valores nulos “por columna” y “por dataframe
def cuenta_nulos(df):
    #Valores nulos por columna
    valores_nulos_column = df.isnull().sum()
    #Valores nulos por dataframe
    valores_nulos_df = df.isnull().sum().sum()
    
    return("Valores nulos por Columna", valores_nulos_column,
            "Valores nulos por DataFrame", valores_nulos_df)

#4.Identifica  los valores atípicos de las columnas numéricas con el método de 
#“Rango intercuartílico” y los sustituye con la leyenda “Valor Atípico”
def limpiar_atipicos(df):
    import pandas as pd
    import numpy as np
    import os

    df_n = df.copy()
    columnas_numericas = df.select_dtypes(include=[np.number]).columns

    for col in columnas_numericas:
        Q1, Q3 = df[col].quantile([0.25, 0.75])
        IQR = Q3 - Q1
        limites = (Q1 - 1.5 * IQR, Q3 + 1.5 * IQR)
        df_n.loc[(df[col] < limites[0]) | (df[col] > limites[1]), col] = "Valor Atípico"
    
    return df_n

