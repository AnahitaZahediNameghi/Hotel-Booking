
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load and process your dataset
df = pd.read_csv('hotel_bookings.csv')  # Replace with your actual dataset
df['arrival_date'] = pd.to_datetime(df['arrival_date_year'].astype(str) + '-' +
                                    df['arrival_date_month'] + '-' +
                                    df['arrival_date_day_of_month'].astype(str))
df['Month'] = df['arrival_date'].dt.month_name()
df['Week'] = df['arrival_date'].dt.isocalendar().week
df['Weekday'] = df['arrival_date'].dt.weekday
df['Week_Name'] = df['arrival_date'].dt.day_name()

# Replace with your mapping dictionary
country_to_region = {
    'USA': 'North America', 'CAN': 'North America', 'MEX': 'North America',
    # Add other mappings here...
}
df['Region'] = df['country'].map(country_to_region).fillna('Unknown')

# Streamlit App Layout
st.title("Booking Data Dashboard")

# Sidebar Filters
st.sidebar.header("Filters")
selected_region = st.sidebar.selectbox("Select a Region", ["All"] + df['Region'].unique().tolist())
selected_month = st.sidebar.selectbox("Select a Month", ["All"] + df['Month'].unique().tolist())

# Apply filters
filtered_df = df
if selected_region != "All":
    filtered_df = filtered_df[filtered_df['Region'] == selected_region]
if selected_month != "All":
    filtered_df = filtered_df[filtered_df['Month'] == selected_month]

# Number of Bookings per Month
st.header("Number of Bookings per Month")
num_of_booking_in_month = filtered_df.groupby('Month')['lead_time'].count().reindex([
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
])

fig, ax = plt.subplots(figsize = (10, 6))
num_of_booking_in_month.plot(kind = 'bar', color = 'skyblue', ax = ax)
ax.set_title("Number of Bookings per Month")
ax.set_xlabel("Month")
ax.set_ylabel("Number of Bookings")
st.pyplot(fig)

# Number of Bookings per Week
st.header("Number of Bookings per Week")
num_of_booking_in_week = filtered_df.groupby('Week')['lead_time'].count()

fig, ax = plt.subplots(figsize = (10, 6))
num_of_booking_in_week.plot(kind = 'bar', color = 'skyblue', ax = ax)
ax.set_title("Number of Bookings per Week")
ax.set_xlabel("Week")
ax.set_ylabel("Number of Bookings")
st.pyplot(fig)

# Number of Bookings by Region
st.header("Number of Bookings per Month by Region")
num_of_bookings_per_region = filtered_df.groupby(['Region', 'Month'])['lead_time'].count().reset_index()

fig, ax = plt.subplots(figsize = (14, 8))
sns.barplot(x = 'Month', y = 'lead_time', hue = 'Region', data = num_of_bookings_per_region, palette = 'tab10', ax = ax)
ax.set_title("Number of Bookings per Month by Region")
ax.set_xlabel("Month")
ax.set_ylabel("Number of Bookings")
plt.xticks(rotation = 45)
st.pyplot(fig)