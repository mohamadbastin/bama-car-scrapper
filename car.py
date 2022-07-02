class CarDetail:
    def __init__(self, year, fuel, body_color, body_type, body_status, inside_color, mileage):
        self.year = year
        self.fuel = fuel
        self.body_color = body_color
        self.body_type = body_type
        self.body_status = body_status
        self.inside_color = inside_color
        self.mileage = mileage


class CarSpecs:
    def __init__(self, acceleration, engine, fuel, volume):
        self.volume = volume
        self.fuel = fuel
        self.engine = engine
        self.acceleration = acceleration


class Car:
    def __init__(self, url, brand, model, details: CarDetail, specs: CarSpecs, price):
        self.url = url
        self.brand = brand
        self.model = model
        self.details = details
        self.specs = specs
        self.price = price

    def get_data(self):
        data = {
            "url": str(self.url),
            "brand": str(self.brand),
            "model": str(self.model),
            "price": int(self.price),
            "year": int(self.details.year),
            "fuel_type": str(self.details.fuel),
            "body_color": str(self.details.body_color),
            "body_type": str(self.details.body_type),
            "body_status": str(self.details.body_status),
            "inside_color": str(self.details.inside_color),
            "mileage": int(self.details.mileage),
            "acceleration": float(self.specs.acceleration),
            "engine": float(self.specs.engine),
            "fuel_consumption": float(self.specs.fuel),
            "volume": float(self.specs.volume)
        }
        return data


class CarUtils:
    @staticmethod
    def create_car(data):
        brand, model = CarUtils._get_brand_and_model(data)
        detail = data["detail"]
        year = CarUtils._clean_year(detail["year"])
        fuel_type = detail["fuel"]
        body_color = detail["body_color"],
        body_type = detail["body_type"],
        body_status = detail["body_status"],
        inside_color = detail["inside_color"],
        mileage = CarUtils._clean_mileage(detail["mileage"]),
        specs = data["specs"]
        acceleration = CarUtils._clean_acceleration(specs["acceleration"]),
        engine = specs["engine"],
        fuel_consumption = CarUtils._clean_fuel_consumption(specs["fuel"]),
        volume = CarUtils._clean_volume(specs["volume"]),
        price = CarUtils._clean_price(data["price"]["price"])
        url = data["metadata"]["canonical"]

        car_details = CarDetail(year, fuel_type, body_color, body_type, body_status, inside_color, mileage)
        car_specs = CarSpecs(acceleration, engine, fuel_consumption, volume)

        car = Car(url, brand, model, car_details, car_specs, price)

        return car

    @staticmethod
    def _get_brand_and_model(i):
        aaa = i["breadcrump"]["links"][-3]["url"].split("/")[-1].split('-')
        brand = aaa[0]
        model = aaa[1]

        return brand, model

    @staticmethod
    def _clean_year(year):
        if year is not None:
            if year[0] == "1":
                year2 = int(year) + 621
                return year2
            return int(year)

    @staticmethod
    def _clean_mileage(mileage):
        if mileage:
            if "صفر" in mileage:
                return 0
            else:
                m = mileage.split(" ")[0]
                m2 = m.split(",")
                m3 = ""
                for i in m2:
                    m3 += i
                try:
                    return int(m3)
                except:
                    return None

    @staticmethod
    def _clean_acceleration(acc):
        if acc:
            acc2 = float(acc.split(" ")[0])
            return acc2

    @staticmethod
    def _clean_fuel_consumption(acc):
        if acc:
            acc2 = float(acc.split(" ")[0])
            return acc2

    @staticmethod
    def _clean_volume(acc):
        if acc:
            acc2 = float(acc.split(" ")[0])
            return acc2

    @staticmethod
    def _clean_price(p):
        if p:
            p2 = p.split(",")
            p3 = ""
            for i in p2:
                p3 += i
            try:
                return int(p3)
            except:
                return None
