import requests
import json

orders = requests.get("https://case-study-challenges.s3-eu-west-1.amazonaws.com/BE/orders.json")
deliveries = requests.get("https://case-study-challenges.s3-eu-west-1.amazonaws.com/BE/deliveries.json")

orders = orders.json()['']

print(orders)