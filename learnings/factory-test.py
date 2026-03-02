class VehicleFactory:
    def create_vehicle(self):
        raise NotImplementedError("This method should be implemented by subclasses")

class IndiaFactory(VehicleFactory):
    def create_vehicl(self, vehicle_type, fuel_type):
        return CarFactory().create_car(fuel_type)
    
class USFactory(VehicleFactory):
    def create_vehicle(self, vehicle_type, fuel_type):
        return CarFactory().create_car(fuel_type)



class CarFactory:
    def create_car(self, type):
        if type == "petrol":
            return self.create_petrol_car()
        elif type == "electric":
            return self.create_electric_car()

    def create_petrol_car(self):
        return "Creating a petrol car"

    def create_electric_car(self):
        return "Creating an electric car"


country = input("Enter the country (India/US): ")
fuel_type = input("Enter the fuel type (petrol/electric): ")
get_factory = IndiaFactory() if country == "India" else USFactory()
print(get_factory.create_vehicle("car", fuel_type))