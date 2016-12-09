#!/usr/bin/python

import serial, threading


class ButtonBox(threading.Thread):

	def __init__(self, device='/dev/ttyUSB0', rate=9600, name='ButtonBox'):
		super(ButtonBox, self).__init__(name=name)
		self.name = name
		self.device = device
		self.rate = rate

		self.data = -1

		self.serial_device = serial.Serial(self.device, self.rate)

		self.daemon = True
		self.data_event = threading.Event()

	def run(self):
		while True:
			self.data = self.serial_device.read()
			self.data_event.set()
			self.data_event.clear()


if __name__ == '__main__':
	button_box = ButtonBox()
	button_box.start()
	while True:
		button_box.data_event.wait()
		print(button_box.data)
