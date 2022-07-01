import requests
import pprint

headers = {
    'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
    'Accept': 'application/json, text/plain, */*',
    'Referer': 'https://bama.ir/car?priced=1',
    'traceparent': '00-0e6f3ef7a30f648bb21266d7929a03f5-0702c6922ce666ac-01',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'priced': '1',
    'pageIndex': '1',
}

response = requests.get('https://bama.ir/cad/api/search', params=params, headers=headers)

pprint.pprint(response.text)
