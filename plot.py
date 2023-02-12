import streamlit as st
import pandas as pd
import json

def parse_dates(date_string: str):
    parts = date_string.split('-')

    if (len(parts) > 1):
        start_date = int(parts[0].replace("BC", "").strip())
        end_date = int(parts[1].replace("AD", "").strip())
        if "BC" in parts[0]:
            start_date = -start_date
        if "AD" in parts[1]:
            end_date = end_date
    else:
        start_date = end_date = int(date_string.replace("BC", "").strip())
    return start_date, end_date



with open("emperors.json", "r") as file:
    # Load the JSON data from the file
    data = json.load(file)

df = pd.DataFrame(data)

st.title("Stability Ranking Over Time")

# Split the reign column into start and end year
df[["start_date", "end_date"]] = df["reign"].apply(parse_dates).apply(pd.Series)

st.write("Table of Emperors")
st.dataframe(df, width=800, height=500)


# Calculate the mid year
df['mid_year'] = (df['start_date'] + df['end_date']) / 2
df["year_range"] = df["start_date"].astype(str) + " - " + df["end_date"].astype(str)
df["year_range_emp"] = df["start_date"].astype(str).str.zfill(3) + " - " + df["end_date"].astype(str) + " (" + df["emperor"] + ")"


st.line_chart(df, x='year_range_emp', y='stability_ranking')