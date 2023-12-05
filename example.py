# This is a sample Python script to Request API from SSDaily API

# Importing the SS Daily API Client
from lib.SSDailyAPIClient import SSDailyAPIClient

# Importing the json library
import json

# Creating a new instance of SSDailyAPIClient
# You can get your API key from https://ssdaily.shop/home/profile

apiConnector = SSDailyAPIClient(
    api_key="YOUR_API_KEY_HERE",
    logger=True  # Set this to False if you don't want to log the API requests
)

# Getting the balance
balance = apiConnector.get_balance()

# Printing the balance
print(
    json.dumps(
        balance,
        indent=4,
        sort_keys=True
    )
)

# Getting the order status
order_status = apiConnector.get_order_status(order_id="YOUR_ORDER_ID_HERE")

# Printing the order status
print(
    json.dumps(
        order_status,
        indent=4,
        sort_keys=True
    )
)

# Getting the service list
service_list = apiConnector.get_service_list()

# Printing the service list
print(
    json.dumps(
        service_list,
        indent=4,
        sort_keys=True
    )
)

# Creating a new order
new_order = apiConnector.create_order(
    service_id="1",
    quantity="100000",
    target="https://www.instagram.com/sandroputraa/",
)

# Printing the new order
print(
    json.dumps(
        new_order,
        indent=4,
        sort_keys=True
    )
)
