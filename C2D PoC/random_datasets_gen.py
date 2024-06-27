import pandas as pd
import numpy as np

# New dummy dataset for Sony IMX728 360°coverage cameras

camera_data_1 = pd.DataFrame({
    'Timestamp': pd.date_range(start='2024-02-01 00:00:00', periods=100, freq='S'),
    'Object_Distance': np.random.uniform(5, 60, 100),
    'Object_Speed': np.random.uniform(10, 220, 100),
    'Object_Type': np.random.choice(['car', 'pedestrian', 'bicycle', 'unknown'], 100)
})
camera_data_1.to_csv('/Users/Andrea/Desktop/C2D PoC/Team 1/Camera_Data_1.csv', index=False)

# New dummy dataset for ZF ProWave Radars
radar_data_1 = pd.DataFrame({
    'Timestamp': pd.date_range(start='2024-02-01 00:00:00', periods=100, freq='S'),
    'Detected_Object_Count': np.random.randint(1, 15, 100),
    'Closest_Object_Distance': np.random.uniform(5, 120, 100),
    'Object_Speed': np.random.uniform(5, 220, 100)
})
radar_data_1.to_csv('/Users/Andrea/Desktop/C2D PoC/Team 1/Radar_Data_1.csv', index=False)

# New dummy dataset for Seyond Falcon Kinetic FK1 Lidars
lidar_data_1 = pd.DataFrame({
    'Timestamp': pd.date_range(start='2024-02-01 00:00:00', periods=100, freq='S'),
    'Point_Cloud_Density': np.random.uniform(0.2, 1.2, 100),
    'Max_Distance': np.random.uniform(10, 250, 100),
    'Object_Count': np.random.randint(1, 25, 100)
})
lidar_data_1.to_csv('/Users/Andrea/Desktop/C2D PoC/Team 1/Lidar_Data_1.csv', index=False)

# New dummy dataset for Neousys RGS-8805GC Computer
computer_data_1 = pd.DataFrame({
    'Timestamp': pd.date_range(start='2024-02-01 00:00:00', periods=100, freq='S'),
    'CPU_Usage': np.random.uniform(5, 100, 100),
    'GPU_Usage': np.random.uniform(5, 100, 100),
    'RAM_Usage': np.random.uniform(1, 32, 100),  # Assuming 32GB RAM
    'Disk_Usage': np.random.uniform(0.1, 1, 100),  # Assuming disk usage is a fraction
    'Temperature': np.random.uniform(25, 110, 100)  # System temperature in Celsius
})
computer_data_1.to_csv('/Users/Andrea/Desktop/C2D PoC/Team 1/Computer_Data_1.csv', index=False)

# New dummy dataset for Engine Sensors
engine_data_1 = pd.DataFrame({
    'Timestamp': pd.date_range(start='2024-02-01 00:00:00', periods=100, freq='S'),
    'Engine_Temperature': np.random.uniform(80, 130, 100),  # Engine temperature in Celsius
    'Engine_RPM': np.random.uniform(2000, 16000, 100),  # Engine RPM
    'Oil_Pressure': np.random.uniform(30, 110, 100)  # Oil pressure in PSI
})
engine_data_1.to_csv('/Users/Andrea/Desktop/C2D PoC/Team 1/Engine_Data_1.csv', index=False)

# New dummy dataset for Brake Sensors
brake_data_1 = pd.DataFrame({
    'Timestamp': pd.date_range(start='2024-02-01 00:00:00', periods=100, freq='S'),
    'Brake_Pressure_Front_Left': np.random.uniform(10, 110, 100),
    'Brake_Pressure_Front_Right': np.random.uniform(10, 110, 100),
    'Brake_Pressure_Rear_Left': np.random.uniform(10, 110, 100),
    'Brake_Pressure_Rear_Right': np.random.uniform(10, 110, 100),
    'Brake_Temperature_Front_Left': np.random.uniform(50, 1050, 100),  # in Celsius
    'Brake_Temperature_Front_Right': np.random.uniform(50, 1050, 100),  # in Celsius
    'Brake_Temperature_Rear_Left': np.random.uniform(50, 1050, 100),  # in Celsius
    'Brake_Temperature_Rear_Right': np.random.uniform(50, 1050, 100)  # in Celsius
})
brake_data_1.to_csv('/Users/Andrea/Desktop/C2D PoC/Team 1/Brake_Data_1.csv', index=False)

# New dummy dataset for Tire Sensors
tire_data_1 = pd.DataFrame({
    'Timestamp': pd.date_range(start='2024-02-01 00:00:00', periods=100, freq='S'),
    'Tire_Pressure_Front_Left': np.random.uniform(25, 40, 100),  # in PSI
    'Tire_Pressure_Front_Right': np.random.uniform(25, 40, 100),  # in PSI
    'Tire_Pressure_Rear_Left': np.random.uniform(25, 40, 100),  # in PSI
    'Tire_Pressure_Rear_Right': np.random.uniform(25, 40, 100),  # in PSI
    'Tire_Temperature_Front_Left': np.random.uniform(70, 130, 100),  # in Celsius
    'Tire_Temperature_Front_Right': np.random.uniform(70, 130, 100),  # in Celsius
    'Tire_Temperature_Rear_Left': np.random.uniform(70, 130, 100),  # in Celsius
    'Tire_Temperature_Rear_Right': np.random.uniform(70, 130, 100)  # in Celsius
})
tire_data_1.to_csv('/Users/Andrea/Desktop/C2D PoC/Team 1/Tire_Data_1.csv', index=False)

# New dummy dataset for Telemetry Sensors
telemetry_data_1 = pd.DataFrame({
    'Timestamp': pd.date_range(start='2024-02-01 00:00:00', periods=100, freq='S'),
    'Speed': np.random.uniform(10, 220, 100),  # in km/h
    'Throttle_Position': np.random.uniform(5, 100, 100),  # in percentage
    'Steering_Angle': np.random.uniform(-90, 90, 100),  # in degrees
    'G-Force_Lateral': np.random.uniform(-6, 6, 100),  # in g
    'G-Force_Longitudinal': np.random.uniform(-6, 6, 100)  # in g
})
telemetry_data_1.to_csv('/Users/Andrea/Desktop/C2D PoC/Team 1/Telemetry_Data_1.csv', index=False)
