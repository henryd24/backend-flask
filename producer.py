# import paho.mqtt.subscribe as subscribe
import paho.mqtt.publish as publish

def publishmqtt(method,body):
    topic = "/main/{}".format(method)
    publish.single(topic, body, hostname="192.168.0.29",port=1882, auth = {'username':"henda", 'password':"henda"})

# def print_msg(client, userdata, message):
#     print("%s : %s" % (message.topic, message.payload))

# subscribe.callback(print_msg, "#", hostname="192.168.0.29",port=1882,auth = {'username':"henda", 'password':"henda"})
