import hid
from scapy.all import *
import time

contVID = 0x054c
contPID = 0x09cc
ip = "192.168.137.127"
port = 8888
LX = 5
LY = 7
RX = 9
RY = 11
dpad_index = 0

class ControlArray:
	def __init__(self, lx, ly, rx, ry, button) -> None:
		self.array = [lx, ly, rx, ry, button]
	def __repr__(self) -> str:
		s = ""
		for item in self.array:
			s += f"{item:03}" + ","
		return s[:len(s)-1]


"""with hid.Device(contVID, contPID) as h:
	print(f'Device manufacturer: {h.manufacturer}')
	print(f'Product: {h.product}')
	print(f'Serial Number: {h.serial}')"""

#for device in hid.enumerate():
#    print(f"0x{device['vendor_id']:04x}:0x{device['product_id']:04x} {device['product_string']}")

#controller = hid.Device(vid = contVID, pid = contPID)

#Switch Controller:
#array[1,2,3] buttons
#array[5] L X
#array[7] L Y
#array[9] R X
#array[11] R Y

prev = [0] * 6

while True:
	array = []
	#for b in controller.read(16):
	#	array.append(b)
	#print(array)
	#array2 = [...]
	q = ControlArray(1,2,3,4,5)
	"""if array2 != prev:
		print(scapy.IP(dst=ip)/scapy.UDP(dport=port)/array2)
	prev = array2"""
	send(IP(dst=ip)/UDP(dport=port)/str(q))
	time.sleep(0.5)