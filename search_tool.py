import requests

from search_parser import SearchParser


class SearchTool:
    _headers = {
        'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
        'Accept': 'application/json, text/plain, */*',
        'Referer': 'https://bama.ir/car?priced=1',
        'traceparent': '00-0e6f3ef7a30f648bb21266d7929a03f5-0702c6922ce666ac-01',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37',
        'sec-ch-ua-platform': '"Windows"',
    }

    @staticmethod
    def get_result_for_page(index):
        params = {
            'priced': '1',
            'pageIndex': str(index),
        }
        response = requests.get('https://bama.ir/cad/api/search', params=params, headers=SearchTool._headers)

        return response.text

    @staticmethod
    def get_number_of_pages():
        params = {
            'priced': '1',
            'pageIndex': 1,
        }
        response = requests.get('https://bama.ir/cad/api/search', params=params, headers=SearchTool._headers)

        return SearchParser.parse_number_of_pages(response.text[:100])
