from typing import Dict

class FuelStation:
    def __init__(self, diesel: int, petrol: int, electric: int):
        self.slots: Dict[str, int] = {
            "diesel" : diesel,
            "petrol" : petrol,
            "electric": electric
        }
        
        self.occupied: Dict[str, int] = {
            "diesel": 0,
            "petrol": 0,
            "electric": 0
        }
    
    def fuel_vehicle(self, fuel_type: str) -> bool:
        if self.occupied[fuel_type] < self.slots[fuel_type]:
            self.occupied[fuel_type] += 1
            return True
        return False
    
    def open_fuel_slot(self, fuel_type: str) -> bool:
        if self.occupied[fuel_type] > 0:
            self.occupied[fuel_type] -= 1
            return True
        return False
