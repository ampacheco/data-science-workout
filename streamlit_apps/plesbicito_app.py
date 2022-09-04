import streamlit as st
import pandas as pd
import numpy as np
import datetime

#
# convert to function later
#
st.title('Plesbicito de Salida. Santiago de Chile')
data_url='https://raw.githubusercontent.com/ampacheco/data-science-workout/main/data/data_2022.csv'
df = pd.read_csv(data_url)

# df["Date"]=pd.to_datetime(df["Date"])

# to avoid time conversion
df["Date"]=pd.to_datetime(df["Date"]).dt.date

start_date=datetime.date.fromisoformat('2022-01-28')
end_date=datetime.date.fromisoformat('2022-09-02')

s_date=st.date_input('Fecha Inicial', start_date)
e_date=st.date_input('Fecha Final', end_date)

filtered_df=df[(df["Date"]>=s_date) & (df["Date"]<=e_date)]

st.write(filtered_df)
st.line_chart(filtered_df, x="Date", y=["Apruebo", "Rechazo", "NSNR"])

# Insert Columns
data_apruebo_url='https://raw.githubusercontent.com/ampacheco/data-science-workout/main/data/aprueban.csv'
data_rechazo_url='https://raw.githubusercontent.com/ampacheco/data-science-workout/main/data/aprueban.csv'
data_indeciso_url='https://raw.githubusercontent.com/ampacheco/data-science-workout/main/data/aprueban.csv'

data_apruebo_url='https://raw.githubusercontent.com/ampacheco/data-science-workout/main/data/aprueban.csv'
df_apruebo = pd.read_csv(data_apruebo_url)