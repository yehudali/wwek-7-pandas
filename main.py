from utils import *
def main():
    df_read=upload_json_data("orders_simple.json")

    Replacing_unnecessary_values(df_read)

    Convert_Value_to_float(df_read)

    convert_to_datetime(df_read)

    character_cleaner(df_read)

    replace_empty_value(df_read)
    
    save_to_csv(df_read)

    create_column_of_above_average(df_read)

    create_a_country_rating_average(df_read)


    # #testim:
    # print(df_read.head(10))
    # print(df_read.describe())
    # print(df_read.value_counts())
    # print(df_read.dtypes)



    



if __name__ == "__main__":
    main()
    