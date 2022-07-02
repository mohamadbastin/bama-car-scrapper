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
