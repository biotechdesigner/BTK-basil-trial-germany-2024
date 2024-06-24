import pandas as pd
from datetime import datetime, timedelta

# Load the CSV file
file_path = '/Users/vrivero/Downloads/BTK DE 001 BASIL 2024 (3).csv'
data = pd.read_csv(file_path)

# Convert TimeStamp column to datetime
data['TimeStamp'] = pd.to_datetime(data['TimeStamp'])

# Define the date range
start_date = datetime(2024, 5, 5)
end_date = datetime(2024, 5, 25)
date_range = pd.date_range(start_date, end_date)

# Get unique values for Treatment, Block, and Observer(s)
treatments = data['Treatment'].unique()
blocks = data['Block'].unique()
observers = data['Observer(s)'].unique()

# Create a list to hold the new rows
new_rows = []

# Generate rows for each date in the date range
for single_date in date_range:
    if not data['TimeStamp'].isin([single_date]).any():
        for treatment in treatments:
            for block in blocks:
                for observer in observers:
                    new_row = {
                        'TimeStamp': single_date,
                        'Treatment': treatment,
                        'Block': block,
                        'Observer(s)': observer,
                        'Plant Height (cm)': None,
                        'Stem Diameter (mm)': None,
                        'Leaf Area (cm²)': None,
                        'Leaf Number': None,
                        'Leaf Colour (HEX)': None,
                        'Water Stress incident': None,
                        'Health Status': None,
                        'Leaf Blistering': None,
                        'Notes': None
                    }
                    new_rows.append(new_row)

# Create a DataFrame from the new rows
new_data = pd.DataFrame(new_rows)

# Append the new rows to the original data
combined_data = pd.concat([data, new_data], ignore_index=True)

# Sort the combined data by TimeStamp, Treatment, Block, and Observer(s)
combined_data.sort_values(by=['TimeStamp', 'Treatment', 'Block', 'Observer(s)'], inplace=True)

# Save the modified dataset to a new CSV file
output_file_path = '/Users/vrivero/Downloads/BTK DE 001 BASIL 2024 (3-transformed).csv'
combined_data.to_csv(output_file_path, index=False)

print(f"Modified dataset saved to {output_file_path}")
