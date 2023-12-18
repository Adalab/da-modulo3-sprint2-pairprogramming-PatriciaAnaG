#%%
import pandas as pd
import numpy as np
from scr import soporte_pair as sp

# %%
df_clientes = pd.read_csv('clientes.csv')
df_clientes
# %%
df_productos = pd.read_csv('productos.csv')
df_productos.reset_index(inplace=True)
df_productos

# %%
df_ventas = pd.read_csv('ventas.csv')
df_ventas
# %%
minusculas_df_clientes = sp.minusculas_columnas(df_clientes)
minusculas_df_clientes
# %%
minusculas_df_productos = sp.minusculas_columnas(df_productos)
minusculas_df_productos
# %%
minusculas_df_ventas = sp.minusculas_columnas(df_ventas)
minusculas_df_ventas
# %%
diccionario_nombres = {
        'index': 'id',
        'id': 'nombre_producto',
        'nombre_producto': 'categoria',
        'categoría': 'precio',
        'precio': 'origen',
        'origen': 'descripcion1',
        'descripcion_total': 'descripción'
    }
trannsformar_productos = sp.transformar_productos(df_productos, diccionario_nombres)
trannsformar_productos
# %%
remplazar_nulos_productos = sp.reemplazar_nulos_desconocido(df_productos)
remplazar_nulos_productos
# %%
reemplazar_nulos_ventas = sp.reemplazar_nulos_desconocido(df_ventas)
reemplazar_nulos_ventas
# %%
df_juntos = sp.juntar_df(df_ventas, df_clientes, df_productos)
df_juntos

# %%

