import requests
import json

product = input("Product name: ")
# lipstick, eyeliner,eyeshadow, blush, bronzer, etc.
brand = input("Brand name: ")
# maybelline, nyx, covegirl

response = requests.get(
    f'http://makeup-api.herokuapp.com/api/v1/products.json?product_type={product}&brand={brand}')


if response.status_code != requests.codes.ok:
    print("Something wrong. Status code:", response.status_code)


else:

    print(json.dumps(response.json(), indent=4))
