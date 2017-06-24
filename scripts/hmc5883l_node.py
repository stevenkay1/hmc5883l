#!/usr/bin/env python

from hmc5883l import hmc5883l
import rospy
import time
from sensor_msgs.msg import MagneticField


def main():
	
	mag_data = MagneticField()
	rospy.init_node('hmc5883l_magnetometer',anonymous=True)
	
	device_address = rospy.get_param('~device_addr')
	sample_rate = rospy.get_param('~sample_rate')
	
	port = rospy.get_param('~i2c_port')
	gauss = rospy.get_param('~gauss')
	declination = (rospy.get_param('~dec1'),rospy.get_param('~dec2'))
	
	pub = rospy.Publisher('magnetometer_data',MagneticField,queue_size = 1)
	rate = rospy.Rate(sample_rate)


	magnetometer = hmc5883l(port,device_address,gauss,declination)
	
	while not rospy.is_shutdown():
		print magnetometer.heading()
		time.sleep(1)

if __name__ == "__main__":
	try:
		main()
	except rospy.ROSInterruptException:
		pass
		
