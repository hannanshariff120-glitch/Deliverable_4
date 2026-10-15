def clean_sensor_readings (sensor_readings: list[float], sensor_threshold: float) -> list:
    """
    Cleans the sensor readings by removing None values and readings below the threshold.
    
    Parameters:
    readings (list): A list of sensor readings which may include None values.
    threshold (float): The minimum valid reading value. Readings below this value will be removed.
    threshold (float): The minimum valid reading value. Readings below this value will be removed.
    
    Returns:
    list: A list of cleaned sensor readings.
    """
    cleaned_readings = [reading for reading in sensor_readings if reading is not None and reading >= sensor_threshold]
    return cleaned_readings

def generate_sensor_report(sensor_name: str, sensor_readings: list[float], sensor_threshold: float) -> str:
    """
    Generates a report for the sensor readings.
    
    Parameters:
    sensor_name (str): The name of the sensor.
    sensor_readings (list): A list of sensor readings which may include None values.
    sensor_threshold (float): The minimum valid reading value. Readings below this value will be removed.
    
    Returns:
    str: A formatted report string for the sensor readings.
    """
    cleaned_readings = clean_sensor_readings(sensor_readings, sensor_threshold)
    total_readings = len(sensor_readings)
    valid_readings_count = len(cleaned_readings)
    removed_readings_count = total_readings - valid_readings_count
    average_reading = sum(cleaned_readings) / valid_readings_count if valid_readings_count > 0 else 0.0
    valid_percentage = (valid_readings_count / total_readings) * 100 if total_readings > 0 else 0.0

    report = f"--- SENSOR REPORT: {sensor_name} ---\n"
    report += f"{'Valid readings':<20}: {valid_percentage:>8.1f}%\n"
    report += f"{'Average reading':<20}:{average_reading:>8.2f}\n"
    report += f"{'Removed readings':<20}: {removed_readings_count:>8}\n"
    return report

sensor_name = "sensor a"
sensor_readings = [2.673, -3.876, 4.589, None, None, None, -6.111, 0.435, None, 0.005,
                   2.444, 10.897, 0.019, 10.222, -0.543, None, 8.097, 0.962, None, 1.005,
                   None, 0.765, 0.765, 0.765, 0.765, 7.937, -1.007, 4.405, None, None]
sensor_threshold = 0.010
print(generate_sensor_report(sensor_name, sensor_readings, sensor_threshold))
