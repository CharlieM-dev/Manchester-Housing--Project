import pandas as pd

df = pd.read_csv('house-prices-messy.csv')

# now we will try to show 10 first columns
# to see what is going on
print(df.columns[:10])

df = df.rename(columns={
    'V4_1': 'value',
    'calendar-years': 'year',          # fixed
    'mmm': 'month_short',
    'Month': 'month',
    'Data Marking': 'data_marking',
    'Time': 'time',
    'administrative-geography': 'administrative_geography',
    'Geography': 'geography',
    'property-type': 'property_type',
    'PropertyType': 'property_type'
})


# We'll need to only keep the key columns
df = df[['year', 'month_short', 'administrative_geography',
         'geography', 'value', 'property_type']]

# Now we drop rows with missing values
df = df.dropna(subset=['value'])

# We need to make price column numeric
df['value'] = pd.to_numeric(df['value'], errors='coerce')

# We'll need to combine year and month
df['Date'] = pd.to_datetime(df['year'].astype(
    str) + "-" + df['month_short'], format='%Y-%b', errors='coerce')

df = df[df['administrative_geography'].str.contains('Manchester', case=False)]

print(df.head())
