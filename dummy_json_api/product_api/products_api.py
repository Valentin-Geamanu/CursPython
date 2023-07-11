import requests


class ProductsApi:
    __BASE_URL = "https://dummyjson.com/products"

    def get_products(self):
        response = requests.get(self.__BASE_URL)
        return response


    def get_product_by_id(self, product_id):
        url = f"{self.__BASE_URL}/{product_id}"
        response = requests.get(url)
        return response

    def search_products(self, search_criteria):
        url = f"{self.__BASE_URL}/shearch"
        response = requests.get(url, params={"q":search_criteria})
        return response
