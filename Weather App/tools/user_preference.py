class UserPreference:
    def __init__(self, units="metric") -> None:
        self.units = units
        self.saved_locations = []
    
    def save_location(self,location) -> None:
        self.saved_locations.append(location)
    
    def remove_location(self,location) -> None:
        self.saved_locations.remove(location)

    def get_saved_location(self) -> list:
        return self.saved_locations