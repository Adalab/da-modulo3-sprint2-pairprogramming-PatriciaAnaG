#%% 
import pandas as pd
import numpy as np
import os
import sys

#%%
def minusculas_columnas (dataframe):
    nuevas_columnas = {columna: columna.lower() for columna in dataframe.columns}
    dataframe.rename(columns=nuevas_columnas, inplace=True)
    return dataframe


# %%
def transformar_productos(df, diccionario_nombres):
    # Renombrar columnas
    df.rename(columns= diccionario_nombres, inplace=True)

    # Concatenar las columnas 'descripcion1' y 'descripcion2' en una nueva columna 'descripcion'
    df['descripcion_total'] = df['descripcion1'].astype(str) + df['descripción']

    # Eliminar columnas 'descripcion1' y 'descripcion2'
    df.drop(['descripcion1', 'descripción'], axis=1, inplace=True)

    return df
# %%
def reemplazar_nulos_desconocido(dataframe):
    for columna in dataframe.columns:
        dataframe[columna].replace(np.nan, 'Desconocido', inplace=True)
    return dataframe
# %%
def juntar_df(df1, df2, df3):
    df_juntos1 = df1.merge(df2, left_on = 'id_cliente', right_on = 'id' )
    df_juntos2 = df_juntos1.merge(df3, left_on = 'id_producto', right_on = 'id')
    df_juntos2.drop(['id_x', 'id_y'], axis=1, inplace=True)
    df_juntos2.to_csv('etl1.csv', index=False)
    return df_juntos2
# %%
