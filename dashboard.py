import streamlit as st
from data_collection import fetch_price_data
from calculations import calculate_crack_spread, calculate_moving_average, calculate_volatility

# Streamlit webpage layout
st.title('Crude 3-2-1 Crackspread Dashboard')

# Fetching data
start_date = '2019-01-01'
end_date = '2024-01-01'  # Adjust as needed
crude_oil_data = fetch_price_data('CL=F', start_date, end_date)
gasoline_data = fetch_price_data('RB=F', start_date, end_date)
distillates_data = fetch_price_data('HO=F', start_date, end_date)
crak_etf_data = fetch_price_data('CRAK', start_date, end_date)

# Calculations
crack_spread = calculate_crack_spread(crude_oil_data, gasoline_data, distillates_data)
moving_average_200d = calculate_moving_average(crack_spread)
volatility = calculate_volatility(crack_spread)
crak_etf_daily_changes = crak_etf_data.pct_change()

# Displaying data on the dashboard
st.write("### Crack Spread")
st.line_chart(crack_spread)

st.write("### 200-Day Moving Average of Crack Spread")
st.line_chart(moving_average_200d)

st.write("### Volatility (200-day Rolling Std Dev)")
st.line_chart(volatility)

st.write("### CRAK ETF Daily Price Changes")
st.line_chart(crak_etf_daily_changes)
