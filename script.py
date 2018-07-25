import pandas as pd
datos = pd.read_csv("comida-rapida.tsv", sep='\t')
datos['item_price'] = datos['item_price'].map(lambda x: x.lstrip('$')).astype(float)
datos['quantity'] = datos['quantity'].astype(float)
datos['unit_price'] = datos['item_price']/datos['quantity']
pricewise = datos.groupby(['item_name','choice_description','unit_price'], as_index=False).first().sort_values('unit_price',ascending=False).reset_index().drop(['order_id','quantity','item_price','index'], axis=1)
top = datos.groupby(['item_name','choice_description','unit_price'], as_index=False)['order_id'].count().sort_values('order_id', ascending=False ).rename(columns = {'order_id':'count'}).reset_index().drop(['index'],axis=1).head(10)
print('***********************Resultado por precio***********************')
print(pricewise)
print('***********************Top 10***********************')
print(top)
