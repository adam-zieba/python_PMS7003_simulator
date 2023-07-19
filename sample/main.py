import generateMeasurements
import time

while True:
  time.sleep(1)
  json_readings= generateMeasurements.generate_json_measurements()
  print(json_readings)