# Base class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def device_info(self):
        return f"{self.brand} {self.model}"

# Derived class (inherits from Device)
class Smartphone(Device):
    def __init__(self, brand, model, os, storage):
        super().__init__(brand, model)  # inherit brand & model from Device
        self.os = os
        self.storage = storage
    
    # Method
    def call(self, contact):
        print(f"Calling {contact} from {self.device_info()}...")
    
    def install_app(self, app_name):
        print(f"Installing {app_name} on {self.device_info()} ({self.os})")

# Creating objects
phone1 = Smartphone("Apple", "iPhone 15 Pro", "iOS", "256GB")
phone2 = Smartphone("Samsung", "Galaxy S24", "Android", "512GB")

# Using methods
phone1.call("Alice")
phone2.install_app("WhatsApp")
