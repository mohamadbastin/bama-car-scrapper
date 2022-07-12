import json
import os
import time
from car import CarUtils
from database import DatabaseManager
from search_tool import SearchTool

db = DatabaseManager.init()
cars_collection = db["cars-test3"]
print("connected to database")

# number_of_pages = SearchTool.get_number_of_pages()
number_of_pages = 1

starting_point = 0

for i in range(starting_point, number_of_pages + 1):
    list_of_cars = []

    print(f"getting data for page {i} / {number_of_pages}")
    data = SearchTool.get_result_for_page(i)
    b = json.loads(data)
    ads = b["data"]["ads"]
    print(f"page {i} has {len(ads)} cars")

    for ad in ads:
        car = CarUtils.create_car(ad)
        list_of_cars.append(car.get_data())

    DatabaseManager.insert_many_if_duplicate_pass(cars_collection, list_of_cars)
    # print(list_of_cars)
    print(f"wrote page {i} result ({len(list_of_cars)} cars) to database.")

    os.system(f"echo {i} > lastIndex.txt")

print("finished all pages.")
