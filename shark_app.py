import pandas as pd
import streamlit as st
import datetime
from shark_functions import(connect_to_db,add_attack,dist_attack_year,attack_history)
st.title("shark data")
db=connect_to_db()
connection =db.connect()
selected_Task=st.selectbox("Choose a Task",['Add shark attack details','check history'])
# ---------------------------------- Add shark attack details ------------------------------
if selected_Task == 'Add shark attack details':
    st.header("Add shark attack details")

    with st.form("Add shark attack form"):

        attack_date = st.date_input("Date")
        attack_type = st.text_input("Type")
        attack_country = st.text_input("Country")
        attack_area = st.text_input("Area")
        attack_location = st.text_input("Location")
        attack_activity = st.text_input("Activity")
        victim_name = st.text_input("Name")
        victim_sex = st.selectbox("Sex", ["M", "F", "Unknown"])
        victim_age = st.number_input("Age", min_value=0.0, step=1.0)
        injury = st.text_input("Injury")
        fatal = st.selectbox("Fatal (Y/N)", ["Y", "N"])
        attack_time = st.text_input("Time")
        species = st.text_input("Species")

        submitted = st.form_submit_button("Submit")

        if submitted:
            try:
                add_attack(
                    connection,
                    attack_date,
                    attack_type,
                    attack_country,
                    attack_area,
                    attack_location,
                    attack_activity,
                    victim_name,
                    victim_sex,
                    victim_age,
                    injury,
                    fatal,
                    attack_time,
                    species
                )
                st.success("Shark attack data inserted successfully ✅")

            except Exception as e:
                st.error("Error while inserting shark attack data")
                st.write(e)

# -------------------------- Shark attack history --------------------------
if selected_Task == 'check history':
    st.header("Shark Attack History")

    years = dist_attack_year(connection)
    year_list = [y[0] for y in years]

    selected_year = st.selectbox("Select Year", year_list)

    if st.button("Show History"):
        data = attack_history(connection, selected_year)

        if data:
            st.dataframe(data)
        else:
            st.warning("No data found for this year")


