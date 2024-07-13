import wmi
import json

def get_gpu_temperatures():
    # Connect to the WMI interface
    w = wmi.WMI(namespace="root\\OpenHardwareMonitor")

    # Query the sensors
    sensors = w.Sensor()

    # Variables to hold the temperatures
    gpu_hotspot_temp = None
    gpu_memory_junction_temp = None

    # Iterate through the sensors to find GPU hotspot and memory junction temperatures
    # Replace with whatever the sensors' names are in Open Hardware Monitor
    for sensor in sensors:
        if sensor.SensorType == "Temperature":
            if "hot spot" in sensor.Name.lower():
                gpu_hotspot_temp = sensor.Value
            elif "gpu memory" in sensor.Name.lower():
                gpu_memory_junction_temp = sensor.Value

    return gpu_hotspot_temp, gpu_memory_junction_temp

def main():
    hotspot_temp, memory_junction_temp = get_gpu_temperatures()
    hotspot_temp = int(hotspot_temp*1000)
    memory_junction_temp = int(memory_junction_temp*1000) # formatted to millidegrees for CoolerControl, modify according to your needs
    result = {
        "GPU Hotspot Temperature": hotspot_temp if hotspot_temp is not None else "Not found",
        "GPU Memory Junction Temperature": memory_junction_temp if memory_junction_temp is not None else "Not found"
    }
    print(json.dumps(result, indent=4))

if __name__ == "__main__":
    main()
