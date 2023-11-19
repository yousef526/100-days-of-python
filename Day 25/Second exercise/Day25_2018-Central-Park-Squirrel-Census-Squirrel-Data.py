import pandas as pd 

df = pd.read_csv('229 - 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv')

df_red = len(df[df['Primary Fur Color'] == 'Cinnamon'])
df_gray = len(df[df['Primary Fur Color'] == 'Gray'])
df_black = len(df[df['Primary Fur Color'] == 'Black'])



dict_Fur = {
    "Fur Color":['red','gray','black'],
    "Count":[df_red,df_gray,df_black]
}

new_csv = pd.DataFrame(dict_Fur)
new_csv.to_csv("Color data.csv")