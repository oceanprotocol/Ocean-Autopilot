import pandas as pd

# Define file paths
Aggregated_Data1_path = '/Users/Andrea/Desktop/C2D PoC/Team 1/Aggregated_Data_1.csv'
Aggregated_Data2_path = '/Users/Andrea/Desktop/C2D PoC/Team 2/Aggregated_Data_2.csv'
Aggregated_Data3_path = '/Users/Andrea/Desktop/C2D PoC/Team 3/Aggregated_Data_3.csv'

# Load the three datasets
Aggregated_Data1 = pd.read_csv(Aggregated_Data1_path)
Aggregated_Data2 = pd.read_csv(Aggregated_Data2_path)
Aggregated_Data3 = pd.read_csv(Aggregated_Data3_path)

# Ensure the timestamp columns are of datetime type
Aggregated_Data1['Timestamp'] = pd.to_datetime(Aggregated_Data1['Timestamp'])
Aggregated_Data2['Timestamp'] = pd.to_datetime(Aggregated_Data2['Timestamp'])
Aggregated_Data3['Timestamp'] = pd.to_datetime(Aggregated_Data3['Timestamp'])

def calculate_means(df1, df2, df3):
    # Identify common numeric columns
    common_columns = list(set(df1.columns) & set(df2.columns) & set(df3.columns))
    numeric_common_columns = [col for col in common_columns if col != 'Timestamp' and pd.api.types.is_numeric_dtype(df1[col])]
    
    # Concatenate the dataframes
    concatenated_df = pd.concat([df1[['Timestamp'] + numeric_common_columns],
                                 df2[['Timestamp'] + numeric_common_columns],
                                 df3[['Timestamp'] + numeric_common_columns]])
    
    # Group by 'Timestamp' and calculate the mean
    means = concatenated_df.groupby('Timestamp').mean().reset_index()
    
    # Ensure the column order is maintained based on the first dataset
    ordered_columns = ['Timestamp'] + [col for col in df1.columns if col in numeric_common_columns]
    means = means[ordered_columns]
    
    return means

# Calculate means
means_df = calculate_means(Aggregated_Data1, Aggregated_Data2, Aggregated_Data3)

# Save the means to a CSV file
output_path = '/Users/Andrea/Desktop/C2D PoC/Aggregated_Mean_Values.csv'
means_df.to_csv(output_path, index=False)