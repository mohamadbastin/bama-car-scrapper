import json
import pprint

from search_tool import SearchTool

# number_of_pages = SearchTool.get_number_of_pages()
#
# for i in range(0, number_of_pages + 1):
#     data = SearchTool.get_result_for_page(i)
#     # database.
#


a = SearchTool.get_result_for_page(1)

b = json.loads(a)
ads = b["data"]["ads"]
print(len(ads))


# pprint.pprint(b)

def get_brand_and_model(i):
    aaa = i["breadcrump"]["links"][-3]["url"].split("/")[-1].split('-')
    brand = aaa[0]
    model = aaa[1]

    return brand, model


for i in ads:
    a, b = get_brand_and_model(i)
    detail = i["detail"]
    specs = i["specs"]
    print(a, b, detail["year"], detail["fuel"], detail["body_color"], detail["body_type"], detail["body_status"],
          detail["inside_color"],
          detail["mileage"], specs["acceleration"], specs["engine"], specs["fuel"], specs["volume"],
          i["price"]["price"])
    s = i["metadata"]["canonical"]
