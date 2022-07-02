class SearchParser:

    @staticmethod
    def get_list_of_data(data):
        pass

    @staticmethod
    def _get_car_data(data):
        pass

    @staticmethod
    def parse_number_of_pages(data: str):
        seed = '"total_pages":'
        idx = data.index(seed)
        d = len(seed)

        return int(data[idx + d: idx + d + 3])
