import pandas as pd


def get_top_300_enterprises(df):
    values = []
    for (i, row) in df.iterrows():
        val = 0
        if row['Ind_EntrprnrGender'] == 'Female':
            val = val + 2
        elif row['Ind_EntrprnrGender'] == 'Male':
            val = val + 0
        if row['TakenFormalLoan'] == 'Yes':
            val = val + 2
        elif row['TakenFormalLoan'] == 'No':
            val = val + 0
        if row['ShopType'] == 'Rented Premises':
            val = val + 1.5
        else:
            val = val + 0
        if row['Hiredworkers'] >= 1:
            val = val + 1.5
        else:
            val = val + 0
        if row['EnterprsLocation'] == 'Highway' or row['EnterprsLocation'] == 'Main Road':
            val = val + 1.5
        else:
            val = val + 0
        if row['EnterprsStartDate'] <=2018:
            val = val + 0.5
        else:
            val = val+ 0
        if row['BusinessType'] == '141 Tailoring' or row['BusinessType']=='471 Kirana':
            val = val + 0
        else:
            val = val + 0.5
        values.append(val)
    df['scores'] = values
    data = df.sort_values(by=['scores'], ascending=False)
    top_300 = data.head(300)
    return top_300

