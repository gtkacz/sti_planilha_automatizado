import pandas as pd
from time import time
 
df=pd.read_excel('tabela_produtos_meuintimo_brucolino.xlsx', skiprows=[1])

urls={}

start_time = time()

for index, row in df.iterrows():
    x=row['Image Src'].split(",")
    for i in (x):
        if row['Handle'] not in urls:
            urls[row['Handle']]=[i]
        else:
            urls[row['Handle']].append(i)
            
    df.at[index, 'Image Src'] = x[0]
    df.at[index, 'Image Position'] = 1
    
for i in urls.keys():
    values = urls.get(i)
    values = values[1:]
    p = 2
    for j in values:
        row = {'Handle':i, 'Title':'', 'Body (HTML)':'', 'Vendor':'', 'Type':'', 'Tags':'', 'Published':'', 'Option1 Name':'', 'Option1 Value':'', 'Option2 Name':'', 'Option2 Value':'', 'Variant SKU':'', 'Variant Grams':'', 'Variant Inventory Tracker':'', 'Variant Inventory Qty':'', 'Variant Inventory Policy':'', 'Variant Fulfillment Service':'', 'Variant Price':'', 'Variant Compare At Price':'', 'Variant Requires Shipping':'', 'Variant Taxable':'', 'Variant Barcode':'', 'Image Src':j, 'Image Position':p, 'Image Alt Text':'', 'Gift Card':'', 'SEO Title':'', 'SEO Description':'', 'Variant Weight Unit':'', 'Cost per item':''}
        df = df.append(row, ignore_index=True)
        p += 1
        
print("Programa levou", time() - start_time, "segundos para rodar")

df.to_excel("tabela_produtos_meuintimo_brucolino_editado.xlsx")