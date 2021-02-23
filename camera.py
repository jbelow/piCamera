from picamera import PiCamera
from time import Button
from datetime import datetime

button = Button(6)
camera = Picamera()

camera.start_preview()
while True:
	try:
		button.wait_for_press()
		now = datetime.now()
		dt_string = now.strftime("%d-%m-%Y_%H:%M:%S")
		camera.annotate_test = dt_string
		camera.capture('//home/pi/adv-web-services/photos/photo%s.jpg' % dt_string)
	except KeyboardInterrupt:
	camera.stop_preview()
	break
