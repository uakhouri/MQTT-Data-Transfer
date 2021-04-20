# Copyright (c) 2010,2011 Roger Light <roger@atchoo.org>
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# 1. Redistributions of source code must retain the above copyright notice,
#   this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
# 3. Neither the name of mosquitto nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import paho.mqtt.client as mqtt
import os
import serial

#usbport = 'COM8' #usb from arduino


arduino = serial.Serial('COM12', 250000, timeout=0)

# Define event callbacks
def on_connect(client, userdata, flags, rc):
    print("rc: " + str(rc))

def on_message(client, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

def on_publish(client, obj, mid):
    print("mid: " + str(mid))

def on_subscribe(client, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(client, obj, level, string):
    print(string)






mqttc = mqtt.Client()
# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe

# Uncomment to enable debug messages
#mqttc.on_log = on_log

# Parse CLOUDMQTT_URL (or fallback to localhost)
#url_str = os.environ.get('CLOUDMQTT_URL', 'mqtt://localhost:1883')
#url = urllib.parse(url_str)
#topic = url.path[1:] or 'test'
topic="utkarsh"
# Connect
mqttc.username_pw_set("sxxcujld", "hyFl3hNA8O8t")# url.username, url.password
mqttc.connect("m16.cloudmqtt.com", 10985)#url.server name, url.port

# Start subscribe, with QoS level 0
mqttc.subscribe(topic, 0)





#distances = []
while (True):
    if (arduino.inWaiting()>0):
        myData = arduino.readline()
        #distances.append(myData)
        myData=myData.decode()
        print(myData)
        mqttc.publish(topic, myData)
        #print(distances)
# Publish a message
#for i in range(0,10):
#    mqttc.publish(topic,i)
#    if i==6:
#        i=0
    
    

# Continue the network loop, exit when an error occurs
#rc = 0
#while rc == 0:
#	    rc = mqttc.loop()
#print("rc: " + str(rc))
#
#bytes.decode(rc)






