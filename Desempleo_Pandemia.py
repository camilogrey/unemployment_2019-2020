#VARIATON WITIN & BETWEEN GROUS
import pandas as pd
pd.set_option('display.max_columns', None)
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from seaborn import axes_style
import re
from seaborn import load_dataset
from scipy.stats import t
from scipy.stats import zscore
desp = pd.read_excel("Route") #,sheet_name=None)
desp['Año Prepandemia'] = desp['Año Prepandemia'].str.replace('%', '')
desp['Año Pandemia'] = desp['Año Pandemia'].str.replace('%', '')

desp['Año Prepandemia'] = pd.to_numeric(desp['Año Prepandemia'])
desp['Año Pandemia'] = pd.to_numeric(desp['Año Pandemia'])

print(desp.info())
print(desp.columns)

print(desp.head(10))
#Boxplot de la distribucion de tasas de desempleo de los paises en el 2019 y 2020
plt.figure(figsize=(10, 6))
# Create the boxplot
plt.boxplot([desp['Año Prepandemia'], desp['Año Pandemia']], labels=['2019', '2020'])

# Set the title and labels
plt.title('Tasas de desempleo(%) años 2019 (prepandemia) y 2020 (pandemia) paises')
plt.xlabel('Año')
plt.ylabel('Tasa de desempleo')
plt.text(1.1, 1, ' COL, ESP, POR, CAN, AUS, UK y USA', fontsize=12, bbox=dict(facecolor='white', edgecolor="none", boxstyle='round,pad=0.5'))
# Show the plot
plt.show()


df = pd.read_excel("C:/Users/camil/Documents/COURSES/Diplomado Data Sience/Data Sciences/Kaggle/Desempleo_Pre_pandemia/Desempleo_Pandemia.xlsx", sheet_name='Desempleo 2019')
df1 = pd.read_excel("C:/Users/camil/Documents/COURSES/Diplomado Data Sience/Data Sciences/Kaggle/Desempleo_Pre_pandemia/Desempleo_Pandemia.xlsx", sheet_name='Desempleo 2020')
print(df.columns)
print(df1.columns)


plt.figure(figsize=(10, 6))
# Create the boxplot
plt.boxplot([df['Colombia'], df['España'], df['Portugal'], df['Canada'], df['Australia'], df['Reino Unido'], df['Estados Unidos']], 
            labels=['Colombia', 'España', 'Portugal', 'Canada', 'Australia','Reino Unido', 'Estados Unidos'])

# Set the title and labels
plt.title('Tasas mensuales de desempleo año 2019 (prepandemia)')
plt.xlabel('País')
plt.ylabel('Tasa de desempleo')

# Show the plot
plt.show()


plt.figure(figsize=(10, 6))
# Create the boxplot
plt.boxplot([df1['Colombia'], df1['España'], df1['Portugal'], df1['Canada'], df1['Australia'], df1['Reino Unido'], df1['Estados Unidos']], 
            labels=['Colombia', 'España', 'Portugal', 'Canada', 'Australia','Reino Unido', 'Estados Unidos'])

# Set the title and labels
plt.title('Tasas mensuales de desempleo año 2020 (pandemia)')
plt.xlabel('País')
plt.ylabel('Tasa de desempleo')

# Show the plot
plt.show()

infor = pd.read_excel("C:/Users/camil/Documents/COURSES/Diplomado Data Sience/Data Sciences/Kaggle/Desempleo_Pre_pandemia/Desempleo_Pandemia.xlsx",sheet_name="Informalidad")
print(infor.head())
print(infor.columns)


plt.figure(figsize=(10, 6))
# Create the boxplot
plt.boxplot([infor['Tasa de Empleo Informal en Colombia'], 
             infor['Tasa de Empleo Informal en España']], labels=['Colombia', 'España'])

# Set the title and labels
plt.title('Tasas de desempleo informal años 2010 a 2019')
plt.xlabel('Paises')
plt.ylabel('Tasa de desempleo informal')
