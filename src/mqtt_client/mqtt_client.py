import json
import time
import random
import paho.mqtt.client as mqtt
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist


# build the json datastore set
jsonFile = open("config.json")
jsonStr = jsonFile.read()
jsonData = json.loads(jsonStr)

# mqtt client connection and setup
mqttc = mqtt.Client()
mqttc.connect("locahost", 8883)

# ros setup
rospy.init_node('mqtt_listener', anonymous=True)

# returns the message type
def data_type(dataType):
	if dataType == "String":
		return String
	if dataType == "Twist":
		return Twist

# callback template builder
def create_callback(subscriberInfo):

	def function_template(data):
		#print dir(data)
		if subscriberInfo['type'] == 'String':
			mqttc.publish(subscriberInfo['mqtt-topic'], data.data)
		if subscriberInfo['type'] == 'Twist':
			mqttc.publish(subscriberInfo['mqtt-topic'], str(data.angular) + str(data.linear))

	return function_template

callbacks = []


# generates callback for all defined subscribers in the json
for idx, subscribers in enumerate(jsonData['subscribers']):
	callbacks.append(create_callback(subscribers))
	rospy.Subscriber(subscribers['ros-topic'], data_type(subscribers['type']), callbacks[idx])

rospy.spin()

# test run of all functions
#for function in callbacks:
#	function(random.randrange(0, 10000))
