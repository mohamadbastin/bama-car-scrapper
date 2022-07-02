import json
import os
import time

from car import CarUtils
from database import DatabaseManager
from search_tool import SearchTool

db = DatabaseManager.init()
cars_collection = db["cars"]
print("connected to database")

# number_of_pages = SearchTool.get_number_of_pages()
number_of_pages = 0

starting_point = 0

for i in range(starting_point, number_of_pages + 1):
    list_of_cars = []

    print(f"getting data for page {i} / {number_of_pages}")
    data = SearchTool.get_result_for_page(i)
    b = json.loads(data)
    ads = b["data"]["ads"]

    for ad in ads:
        car = CarUtils.create_car(ad)
        list_of_cars.append(car)

    DatabaseManager.insert_many_if_duplicate_pass(cars_collection, list_of_cars)
    print(f"wrote page {i} result to database.")

    os.system(f"echo {i} -> lastIndex.txt")

    # time.sleep(3)

print("finished all pages.")
