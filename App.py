
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load and process your dataset
df = pd.read_csv('hotel_bookings.csv') 

    
df['arrival_date'] = pd.to_datetime(df['arrival_date_year'].astype(str) + '-' +
                                    df['arrival_date_month'] + '-' +
                                    df['arrival_date_day_of_month'].astype(str))

df['Month'] = df['arrival_date'].dt.month_name()
df['Week'] = df['arrival_date'].dt.isocalendar().week
df['Weekday'] = df['arrival_date'].dt.weekday
df['Week_Name'] = df['arrival_date'].dt.day_name()

# Custom Mapping for Region
country_to_region = {
    'USA': 'North America', 'CAN': 'North America', 'MEX': 'North America',
    'GBR': 'Europe', 'FRA': 'Europe', 'DEU': 'Europe', 'ESP': 'Europe', 'IRL': 'Europe', 'PRT': 'Europe',
    'ROU': 'Europe', 'NOR': 'Europe', 'POL': 'Europe', 'CHE': 'Europe', 'GRC': 'Europe', 'ITA': 'Europe',
    'NLD': 'Europe', 'DNK': 'Europe', 'RUS': 'Europe', 'SWE': 'Europe', 'AUT': 'Europe', 'BLR': 'Europe',
    'LUX': 'Europe', 'SVN': 'Europe', 'ALB': 'Europe', 'SMR': 'Europe', 'MNE': 'Europe', 'KOS': 'Europe',
    'CZE': 'Europe', 'SVK': 'Europe', 'HRV': 'Europe', 'HUN': 'Europe', 'EST': 'Europe', 'LVA': 'Europe',
    'LTU': 'Europe', 'BGR': 'Europe', 'GIB': 'Europe', 'AND': 'Europe', 'MLT': 'Europe', 'ISL': 'Europe',
    'MAC': 'Asia', 'KOR': 'Asia', 'CRI': 'North America', 'JPN': 'Asia', 'KAZ': 'Asia', 'PAK': 'Asia',
    'IDN': 'Asia', 'LBN': 'Asia', 'PHL': 'Asia', 'SGP': 'Asia', 'THA': 'Asia', 'VNM': 'Asia', 'HKG': 'Asia',
    'TWN': 'Asia', 'CHN': 'Asia', 'IRN': 'Asia', 'OMN': 'Asia', 'ARE': 'Asia', 'IRQ': 'Asia', 'JOR': 'Asia',
    'SYR': 'Asia', 'ARM': 'Asia', 'GEO': 'Asia', 'AZE': 'Asia', 'ARM': 'Asia',
    'AUS': 'Oceania', 'NZL': 'Oceania', 'PNG': 'Oceania', 'FJI': 'Oceania', 'SLB': 'Oceania', 'VUT': 'Oceania',
    'WLF': 'Oceania', 'PYF': 'Oceania', 'KIR': 'Oceania', 'SAM': 'Oceania', 'TON': 'Oceania', 'NCL': 'Oceania',
    'ZAF': 'Africa', 'NGA': 'Africa', 'EGY': 'Africa', 'KEN': 'Africa', 'ETH': 'Africa', 'DZA': 'Africa',
    'UGA': 'Africa', 'Tanzania': 'Africa', 'GHA': 'Africa', 'CMR': 'Africa', 'CIV': 'Africa', 'MUS': 'Africa',
    'ZMB': 'Africa', 'MWI': 'Africa', 'NAM': 'Africa', 'MLI': 'Africa', 'BFA': 'Africa', 'TGO': 'Africa',
    'GNB': 'Africa', 'SLE': 'Africa', 'STP': 'Africa', 'AGO': 'Africa', 'BEN': 'Africa', 'BWA': 'Africa',
    'LSO': 'Africa', 'SWZ': 'Africa', 'SDN': 'Africa', 'SOM': 'Africa', 'MDG': 'Africa', 'REU': 'Africa',
    'DJI': 'Africa', 'ERI': 'Africa', 'GAB': 'Africa', 'COM': 'Africa', 'MRT': 'Africa', 'BWA': 'Africa',
    'SYR': 'Asia', 'HUN': 'Europe', 'AIA': 'Caribbean', 'ABW': 'Caribbean', 'BRB': 'Caribbean', 'GUY': 'South America',
    'PYF': 'Oceania', 'ATA': 'Antarctica', 'GLP': 'Caribbean', 'DMA': 'Caribbean', 'LCA': 'Caribbean',
    'SUR': 'South America', 'BRB': 'Caribbean', 'BOL': 'South America', 'PRY': 'South America', 'GUY': 'South America',
    'VGB': 'Caribbean', 'TCA': 'Caribbean', 'JAM': 'Caribbean', 'ATF': 'Antarctica', 'FRO': 'Europe',
    'UMI': 'Oceania', 'MTQ': 'Caribbean', 'BES': 'Caribbean', 'SXM': 'Caribbean', 'GUF': 'South America',
    'SPM': 'Caribbean', 'MNP': 'Oceania', 'RMI': 'Oceania', 'FSM': 'Oceania'
    }

df['Region'] = df['country'].map(country_to_region).fillna('Unknown')



# --- Streamlit App ---
st.title('Hotel Booking Analysis')

# --- Bookings by Month ---
st.header('Bookings by Month')
num_of_booking_in_month = df.groupby('Month')['lead_time'].count()
num_of_booking_in_month = num_of_booking_in_month.reindex([
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
])

fig_month = px.bar(x = num_of_booking_in_month.index, y = num_of_booking_in_month.values,
                    labels = {'x': 'Month', 'y': 'Number of Bookings'},
                    title = 'Number of Bookings per Month',
                    color_discrete_sequence = ['skyblue'])
st.plotly_chart(fig_month)



# --- Bookings by Week ---
st.header('Bookings by Week')
num_of_booking_in_week = df.groupby('Week')['lead_time'].count()
fig_week = px.bar(x = num_of_booking_in_week.index, y = num_of_booking_in_week.values,
                    labels = {'x': 'Week', 'y': 'Number of Bookings'},
                    title = 'Number of Bookings per Week',
                    color_discrete_sequence = ['skyblue'])
st.plotly_chart(fig_week)

# --- Bookings by Weekday (Name and Number) ---
st.header('Bookings by Weekday')
col1, col2 = st.columns(2)
with col1:
    st.subheader("Bookings by Weekday Name")
    num_of_booking_in_weekname = df.groupby('Week_Name')['lead_time'].count()
    fig_weekname = px.bar(x = num_of_booking_in_weekname.index, y = num_of_booking_in_weekname.values,
                    labels = {'x': 'Week Name', 'y': 'Number of Bookings'},
                    title = 'Number of Bookings Per Week Name',
                    color_discrete_sequence = ['skyblue'])
    st.plotly_chart(fig_weekname)
with col2:
    st.subheader('Bookings by Weekday Number')
    num_of_booking_in_weekday = df.groupby('Weekday')['lead_time'].count()
    fig_weekday = px.bar(x = num_of_booking_in_weekday.index, y = num_of_booking_in_weekday.values,
                        labels = {'x': 'Weekday Number', 'y': 'Number of Bookings'},
                        title = 'Number of Bookings Per Weekday Number',
                        color_discrete_sequence = ['skyblue'])
    st.plotly_chart(fig_weekday)
    
# --- Bookings per Region by Month ---
st.header('Bookings per Region by Month')
num_of_bookings_per_region = df.groupby(['Region', 'Month'])['lead_time'].count().reset_index()
fig_region = px.bar(num_of_bookings_per_region, x = "Month", y = "lead_time", color = "Region",
                    title = "Number of Bookings per Month by Region",
                    labels = {'lead_time': 'Number of Bookings'},
                    log_y = True)
st.plotly_chart(fig_region)



# --- Display Raw Data ---
if st.checkbox("Show Raw Data"):
    st.subheader("Raw Data")
    st.write(df)