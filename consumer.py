import paho.mqtt.subscribe as subscribe
import json
from main import Product, db

def print_msg(client, userdata, message):
    print("%s : %s" % (message.topic, message.payload))
    data = json.loads(message.payload)
    print(data)
    
    if message.topic == '/main/product_created':
        product = Product(id=data['id'], title=data['title'], image = ['image'])
        db.session.add(product)
        db.session.commit()
        print('Product Created')
        
    elif message.topic == '/main/product_updated':
        product = Product.query.get(data['id'])
        product.title = data['title']
        product.image = data['image']
        db.session.commit()
        print('Product Updated')
        
    elif message.topic == '/main/product_deleted':
        product = Product.query.get(data)
        db.session.delete(product)
        db.session.commit()
        print('Product Deleted')
        
print('Started Consuming')
subscribe.callback(print_msg, "/main/#", hostname="192.168.0.29",port=1882,auth = {'username':"henda", 'password':"henda"})