import time
import json
import requests


class market(object):

    def __init__(self):
        self.market_api_url = "https://market-api.radiocaca.com/nft-sales/"
        self.market_url = "https://market.radiocaca.com/#/market-place/"
        self.nft_category = {"MSL": "7", "MPB": "10", "Potion": "15", "Diamond": "16", "Egg": "17", "Kiss": "20"}
        self.payload = {"pageNo": "1", "pageSize": 10, "sortBy": "single_price", "order": "asc", "name": "",
                        "saleType": "", "category": "", "tokenType": ""}

    def get_1155_nft(self, name, number=20):
        self.payload["category"] = self.nft_category[name]
        self.payload["pageSize"] = number
        self.r = json.loads(requests.get(self.market_api_url, params=self.payload).text)
        self.nft_list = self.r["list"]
        for nft in self.nft_list:
            s = name + ": x" + str(nft["count"]).ljust(4) + "  unit price: " + str(
                int(nft["fixed_price"]) // nft["count"]) + "  total price: " + str(nft["fixed_price"]).ljust(
                9) + "  url: " + self.market_url + str(nft["id"])
            print(s)

if __name__ == "__main__":
    my_market = market()
    my_market.get_1155_nft("Egg", 100)  # name = ["Potion", "Diamond", "Egg"]
    #my_market.get_721_nft("Kiss", 5)  # name = ["MPB", "MSL", "Kiss"]
    #my_market.get_metamon(20)