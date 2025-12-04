import pandas as pd


# Read from JSON
def upload_json_data(file):
    df_read = pd.read_json(file)
    return df_read


def Replacing_unnecessary_values(df: pd.DataFrame):
    df['total_amount'] = df['total_amount'].str.replace('$', '')


def Convert_Value_to_float(df: pd.DataFrame):
    df['total_amount'] = df['total_amount'].astype(float)

def convert_to_datetime(df: pd.DataFrame):
    df['order_date'] = pd.to_datetime(df['order_date'])

def character_cleaner(df: pd.DataFrame):
    df['items_html'] = df['items_html'].str.replace(r'<.*?>', ' ', regex=True)
    df['items_html'] = df['items_html'].str.replace('  ', ' ').str.strip()


def replace_empty_value(df: pd.DataFrame):
    df['coupon_used'] = df['coupon_used'].str.replace('', 'coupon_used')
 



def create_column_of_above_average(df: pd.DataFrame):
    mean_n = df['total_amount'].mean()
    df['high_value_order'] = df['total_amount'] > mean_n
    df.sort_values(by='total_amount', ascending=False)



def create_a_country_rating_average(df: pd.DataFrame):
    df["average rating per country"] = df.groupby('country')['rating'].mean()



# def a(df: pd.DataFrame):
#     for x in df.index:
#         if df.loc[x, "total_amount"] > 1000:
#             df.drop(x, inplace = True)






#save it to csv file
def save_to_csv(df):
    df.to_csv('clean_orders_[ID_NUMBER].csv', index=False)
    