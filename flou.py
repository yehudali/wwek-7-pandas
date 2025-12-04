# import pandas as pd

# df_read = pd.read_json('orders_simple.json')
# df_read['total_amount'] = df_read['total_amount'].str.replace('$', '')
# df_read['total_amount'] = df_read['total_amount'].astype(float)
# df_read['order_date'] = pd.to_datetime(df_read['order_date'])
# df_read['items_html'] = df_read['items_html'].str.replace(r'<.*?>', ' ', regex=True)
# df_read['items_html'] = df_read['items_html'].str.replace('  ', ' ').str.strip()
# df_read['coupon_used'] = df_read['coupon_used'].str.replace('', 'coupon_used')

# # df_read['coupon_used']=df_read['order_date'].


# mean = df_read['total_amount'].mean()
# def check_if_is_higher_than_average(df):
#      df_read['total_amount'] < mean:
        

# df_read['high_value_order']=df_read.apply(df_read['total_amount'], )


# print(df_read['items_html'])

