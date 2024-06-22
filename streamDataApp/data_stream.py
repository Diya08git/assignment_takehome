from typing import Dict

class DataStream:
    def __init__(self): 
        self.last_printed: Dict[str, int] = {}
        
    def output_data_str(self, timestamp: int, data_str: str) -> bool:
        if data_str in self.last_printed:
            if timestamp - self.last_printed[data_str] >= 5:
                self.last_printed[data_str] = timestamp
                return True
            else:
                return False
        else:
            self.last_printed[data_str] = timestamp
            return True
