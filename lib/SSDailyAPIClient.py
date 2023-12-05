import requests
import logging


class SSDailyAPIClient:
    BASE_API_URL = "https://ssdaily.shop/api/v1/"

    def __init__(self, api_key, logger=False):
        self.logger = logger
        self.api_key = api_key
        if self.api_key is None or self.api_key == "YOUR_API_KEY_HERE":
            raise ValueError("API key must be set")

        if self.logger:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
            self.logger = logging.getLogger(__name__)
            self.logger.info("API key: " + self.api_key)

        self.headers = {
            "User-Agent": "SSDaily Python API Client",
            "Content-Type": "application/json"
        }

    def get_balance(self):
        if self.logger:
            self.logger.info("Getting balance from API")
        _request = None
        try:
            _request = requests.post(
                url=self.BASE_API_URL + "subscriptions",
                headers=self.headers,
                json={
                    "api_key": self.api_key
                },
            )

            if _request.status_code == 200 and _request.json()["status"] == "success":
                if self.logger:
                    self.logger.info("Balance retrieved successfully")
                return {
                    "status": True,
                    "current_balance": _request.json()["data"]["current_balance"],
                    "total_usage": _request.json()["data"]["total_usage"],
                }
            else:
                if self.logger:
                    self.logger.error("Failed to retrieve balance")
                return {
                    "status": False,
                    "message": _request.json()["message"]
                }

        except KeyError:
            if self.logger:
                self.logger.error("Something went wrong while parsing the response from the API")
            return {
                "status": False,
                "message": "Something went wrong while parsing the response from the API",
                "response": _request.json()
            }

        except Exception as e:
            if self.logger:
                self.logger.error("Something went wrong while requesting the API")
            return {
                "status": False,
                "message": "Something went wrong while requesting the API",
                "error": str(e)
            }

    def get_order_status(self, order_id):
        if self.logger:
            self.logger.info("Getting order status from API")
        if order_id is None or order_id == "YOUR_ORDER_ID_HERE":
            raise ValueError("Order ID must be set")

        _request = None
        try:
            _request = requests.post(
                url=self.BASE_API_URL + "status/orders/{order_id}".format(order_id=order_id),
                headers=self.headers,
                json={
                    "api_key": self.api_key,
                },
            )
            if _request.status_code == 200 and _request.json()["status"] == "success":
                if self.logger:
                    self.logger.info("Order status retrieved successfully")
                return {
                    "status": True,
                    "id_order": _request.json()["data"]["id_order"],
                    "status_order": _request.json()["data"]["status"],
                    "quantity": _request.json()["data"]["quantity"],
                    "target": _request.json()["data"]["target"],
                    "total_price": _request.json()["data"]["total_price"],
                    "progress": _request.json()["data"]["progress"],
                    "created_at": _request.json()["data"]["created_at"],
                }
            else:
                if self.logger:
                    self.logger.error("Failed to retrieve order status")
                return {
                    "status": False,
                    "message": _request.json()["message"]
                }

        except KeyError:
            if self.logger:
                self.logger.error("Something went wrong while parsing the response from the API")
            return {
                "status": False,
                "message": "Something went wrong while parsing the response from the API",
                "response": _request.json()
            }

        except Exception as e:
            if self.logger:
                self.logger.error("Something went wrong while requesting the API")
            return {
                "status": False,
                "message": "Something went wrong while requesting the API",
                "error": str(e)
            }

    def get_service_list(self):
        if self.logger:
            self.logger.info("Getting service list from API")
        _request = None
        try:
            _request = requests.post(
                url=self.BASE_API_URL + "services",
                headers=self.headers,
                json={
                    "api_key": self.api_key,
                },
            )
            if _request.status_code == 200 and _request.json()["status"] == "success":
                if self.logger:
                    self.logger.info("Service list retrieved successfully")
                return {
                    "status": True,
                    "services": _request.json()["data"]
                }
            else:
                return {
                    "status": False,
                    "message": _request.json()["message"]
                }

        except KeyError:
            if self.logger:
                self.logger.error("Something went wrong while parsing the response from the API")
            return {
                "status": False,
                "message": "Something went wrong while parsing the response from the API",
                "response": _request.json()
            }

        except Exception as e:
            if self.logger:
                self.logger.error("Something went wrong while requesting the API")
            return {
                "status": False,
                "message": "Something went wrong while requesting the API",
                "error": str(e)
            }

    def create_order(self, service_id, quantity, target):
        if self.logger:
            self.logger.info("Creating order from API")

        if service_id is None:
            raise ValueError("Service ID must be set")
        if quantity is None:
            raise ValueError("Quantity must be set")
        if target is None:
            raise ValueError("Target must be set")

        _request = None
        try:
            _request = requests.post(
                url=self.BASE_API_URL + "order",
                headers=self.headers,
                json={
                    "api_key": self.api_key,
                    "service_id": service_id,
                    "quantity": quantity,
                    "target": target,
                },
            )
            if _request.status_code == 200 and _request.json()["status"] == "success":
                if self.logger:
                    self.logger.info("Order created successfully")
                return {
                    "status": True,
                    "id_order": _request.json()["data"]["id_order"],
                    "service_id": _request.json()["data"]["service_id"],
                    "status_order": _request.json()["data"]["status"],
                    "quantity": _request.json()["data"]["quantity"],
                    "target": _request.json()["data"]["target"],
                    "total_price": _request.json()["data"]["total_price"],
                    "created_at": _request.json()["data"]["created_at"],
                }
            else:
                if self.logger:
                    self.logger.error("Failed to create order")
                return {
                    "status": False,
                    "message": _request.json()["message"]
                }

        except KeyError:
            if self.logger:
                self.logger.error("Something went wrong while parsing the response from the API")
            return {
                "status": False,
                "message": "Something went wrong while parsing the response from the API",
                "response": _request.json()
            }

        except Exception as e:
            if self.logger:
                self.logger.error("Something went wrong while requesting the API")
            return {
                "status": False,
                "message": "Something went wrong while requesting the API",
                "error": str(e)
            }
