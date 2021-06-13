#!/usr/bin/env python
# coding: utf-8

# In[56]:


# Used to clean and analyse the data-set
import pandas as pd
# To open an excel file
df = pd.read_csv('Formulario_Tabela.csv', index_col=False)

import xlwt 
from xlwt import Workbook 
n_intervalos=df.shape[0]

wb = Workbook() 

sheet1 = wb.add_sheet('Resultados')
style = xlwt.easyxf('font: bold 1') 
  

sheet1.write(0,0,'Tipo de Estabelecimento')
sheet1.write(0,1,'Norte')
sheet1.write(0,2,'Sul')
sheet1.write(0,3, 'Leste')
sheet1.write(0,4,'Oeste')
sheet1.write(0,5, 'Centro')


for i in range (n_intervalos):
    sheet1.write(i+1,0, str(df.iloc[i][0]))
    sheet1.write(i+1,1, int(df.iloc[i][1]))
    sheet1.write(i+1,2, int(df.iloc[i][2]))
    sheet1.write(i+1,3, int(df.iloc[i][3]))
    sheet1.write(i+1,4, int(df.iloc[i][4]))
    sheet1.write(i+1,5, int(df.iloc[i][5]))

    
wb.save("Resultados1.xls")





