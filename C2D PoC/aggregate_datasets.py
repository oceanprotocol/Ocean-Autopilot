import pandas as pd

# Define file paths [UPDATE FILE PATH]
computer_data_path = '/Users/Andrea/Desktop/C2D PoC/Team 3/Computer_Data_3.csv'
engine_data_path = '/Users/Andrea/Desktop/C2D PoC/Team 3/Engine_Data_3.csv'
brake_data_path = '/Users/Andrea/Desktop/C2D PoC/Team 3/Brake_Data_3.csv'
tire_data_path = '/Users/Andrea/Desktop/C2D PoC/Team 3/Tire_Data_3.csv'
telemetry_data_path = '/Users/Andrea/Desktop/C2D PoC/Team 3/Telemetry_Data_3.csv'

# Load the new datasets 
computer_data = pd.read_csv(computer_data_path)
engine_data = pd.read_csv(engine_data_path)
brake_data = pd.read_csv(brake_data_path)
tire_data = pd.read_csv(tire_data_path)
telemetry_data = pd.read_csv(telemetry_data_path)

# Merge datasets on the Timestamp column
combined_data_new = pd.merge(computer_data, engine_data, on='Timestamp', suffixes=('_computer', 'engine'))
combined_data_new = pd.merge(combined_data_new, brake_data, on='Timestamp', suffixes=('', '_brake'))
combined_data_new = pd.merge(combined_data_new, tire_data, on='Timestamp', suffixes=('', '_tire'))
combined_data_new = pd.merge(combined_data_new, telemetry_data, on='Timestamp', suffixes=('', '_telemetry'))

# Save the combined dataset to a CSV file [UPDATE FILE PATH AND FILE NAME]
combined_csv_new_path = '/Users/Andrea/Desktop/C2D PoC/Team 3/Aggregated_Data_3.csv'
combined_data_new.to_csv(combined_csv_new_path, index=False)

print(f"Aggregated dataset saved to {combined_csv_new_path}")
