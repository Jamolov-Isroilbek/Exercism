class SpaceAge:   
    days = 365.25
    hours = 24
    minutes = 60
    seconds = 60
    
    def __init__(self, seconds):
        self.seconds = seconds

    def on_mercury(self):
        return round(self.seconds / self.total_seconds(0.2408467), 2)
    
    def on_venus(self):
        return round(self.seconds / self.total_seconds(0.61519726), 2)
    
    def on_earth(self):
        return round(self.seconds / self.total_seconds(1.0), 2)
    
    def on_mars(self):
        return round(self.seconds / self.total_seconds(1.8808158), 2)
    
    def on_jupiter(self):
        return round(self.seconds / self.total_seconds(11.862615), 2)
    
    def on_saturn(self):
        return round(self.seconds / self.total_seconds(29.447498), 2)
    
    def on_uranus(self):
        return round(self.seconds / self.total_seconds(84.016846), 2)

    def on_neptune(self):
        return round(self.seconds / self.total_seconds(164.79132), 2)

    def total_seconds(self, year):
        return SpaceAge.days * SpaceAge.hours * SpaceAge.minutes * SpaceAge.seconds * year
        

        