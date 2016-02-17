'''
Temperature monitoring module

Grabs data which OpenHardwareMonitor (http://openhardwaremonitor.org/) makes available via WMI.
If OHWM isn't running this will fail.
So the methods exposed here will (optionally) attempt to open OHWM if it doesn't seem to be running.
'''

from wmi import WMI

w = WMI(namespace="root\OpenHardwareMonitor")

def get_CPU_Core():
	for sensor in w.Sensor(Name = u"CPU Core"):
		return sensor.Value
		
def get_GPU_Core():
	for sensor in w.Sensor(Name = u"GPU Core"):
		return sensor.Value

# print(get_GPU_Core())
# print(get_CPU_Core())