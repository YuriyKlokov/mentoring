import pandas as pd

data = [[1, 20, '2019-08-14'], [2, 50, '2019-08-14'], [1, 30, '2019-08-15'], [1, 35, '2019-08-16'], [2, 65, '2019-08-17'], [3, 20, '2019-08-18']]
products = pd.DataFrame(data, columns=['product_id', 'new_price', 'change_date']).astype({'product_id':'Int64', 'new_price':'Int64', 'change_date':'datetime64[ns]'})
products_cut = products[products['change_date'] <= '2019-08-16']
products_grp = products_cut.groupby('product_id')['change_date'].max()
products_final = products.merge(products_grp, on = 'product_id', how = 'left')
products_final = products_final[products_final['change_date_x'] == products_final['change_date_y']]
products_final_cut = products.drop_duplicates(subset=['product_id'])
products_final_cut = products_final_cut.merge(products_final, on = 'product_id', how = 'left')
products_itogo =  products_final_cut[['product_id', 'new_price_y']].fillna(10).rename({'new_price_y':'price'})
print(products_itogo)
