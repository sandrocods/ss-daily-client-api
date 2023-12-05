# SS Daily API Client

![SS Daily API Client](https://ssdaily.shop/static/logo.png "SS Daily API Client")

#### Simple API client for [SS Daily Social Media Marketing](https://ssdaily.shop) Requests API,

### - Get your API key from [Profile Page](https://ssdaily.shop/home/profile)

## Python Version

#### Install Requirements

```bash
pip install -r requirements.txt
```

### Usage

```python
# Import SSDailyAPIClient
from lib.SSDailyAPIClient import SSDailyAPIClient

# Create SSDailyAPIClient instance
ssdaily = SSDailyAPIClient(
    api_key="YOUR_API_KEY"
)

# Example: Get all SS Daily services
services = ssdaily.get_service_list()
print(services)

```

### Expected Result

```json
{
  "data": [
    {
      "category": "Shopee",
      "description": "👥 User 99% Indonesia [ GOOD QUALITY OF ACCOUNTS HAS PROFILE PICTURE  GOOD USERNAME ]\r\n⌚ Start Time : Instant - 8 Hours, Max 1 Day [ Natural Increase ]\r\n🎯 Target : Link Toko [ ex : https://shopee.co.id/sandroputraa ]\r\n✔ Start Count : Active\r\n📷 Sample : https://prnt.sc/dIVvNpZLR2wX",
      "id": 1,
      "max_order": 1000,
      "min_order": 100,
      "name": "Shopee Followers Indonesia [Max 1K] 🔥🔥",
      "price_api": 64000,
      "slug": "shopee_followers_indonesia_max_1k_"
    },
    .... more services
  ],
  "message": "Success get services",
  "status": "success"
}
```

#### For more examples, check out the [example.py](example.py) file.


