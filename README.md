# ROS MQTT Client

[![N|Roboteurs](https://cdn.shopify.com/s/files/1/0742/2899/files/logosmall.png?575371702457707276
)](https://www.roboteurs.com)

This is an ROS MQTT client that is used to expose ROS topics over MQTT. Currently the project only supports publishing of ROS topics. The origonal intent of this project was to give students a working datasource from an active robot system. Using MQTT allows the data to be seen by many without needing access to the ROS system itself. 

### Usage
This node uses the config.json file to configure what topics should be published to the MQTT broker. Adding topics will automatically register new callbacks for these topics in the node.

```json
        {       "ros-topic": "chatter",
                "mqtt-topic": "ros/chatter",
                "rate": 10,
                "type" : "String"
        },
```
In this node only topics of type String and Twist are supported. Other topics can easily be added by changing the main python script. The topic type must be added to the topic lookup function and an if statment to define how the processing is being done must be added. 

```python
if dataType == "Twist":
    return Twist
```
```python
if subscriberInfo['type'] == 'Twist':
    mqttc.publish(subscriberInfo['mqtt-topic'], str(data.angular) + str(data.linear))
```

### To Do
* Add security features of MQTT
* Add ROS topic publish (ie, target point)
* Move MQTT client info to .json file
* Implement max rate

 
