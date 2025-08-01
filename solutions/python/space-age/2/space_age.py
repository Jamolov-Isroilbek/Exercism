class SpaceAge:   
    days = 365.25
    hours = 24
    minutes = 60
    seconds = 60

    orbital_period_in_earth_years = {
        "mercury": 0.2408467,
        "venus": 0.61519726,
        "earth": 1.0,
        "mars": 1.8808158,
        "jupiter": 11.862615,
        "saturn": 29.447498,
        "uranus": 84.016846,
        "neptune": 164.79132
    }
    
    def __init__(self, seconds):
        self.seconds = seconds

    def on_mercury(self):
        return self.planet_year_in_seconds(
            SpaceAge.orbital_period_in_earth_years["mercury"], self.seconds
        )
    
    def on_venus(self):
        return self.planet_year_in_seconds(
            SpaceAge.orbital_period_in_earth_years["venus"], self.seconds
        )
    
    def on_earth(self):
        return self.planet_year_in_seconds(
            SpaceAge.orbital_period_in_earth_years["earth"], self.seconds
        )
    
    def on_mars(self):
        return self.planet_year_in_seconds(
            SpaceAge.orbital_period_in_earth_years["mars"], self.seconds
        )
    
    def on_jupiter(self):
        return self.planet_year_in_seconds(
            SpaceAge.orbital_period_in_earth_years["jupiter"], self.seconds
        )
    
    def on_saturn(self):
        return self.planet_year_in_seconds(
            SpaceAge.orbital_period_in_earth_years["saturn"], self.seconds
        )
    
    def on_uranus(self):
        return self.planet_year_in_seconds(
            SpaceAge.orbital_period_in_earth_years["uranus"], self.seconds
        )

    def on_neptune(self):
        return self.planet_year_in_seconds(
            SpaceAge.orbital_period_in_earth_years["neptune"], self.seconds
        )

    def planet_year_in_seconds(self, year, seconds):
        year_in_seconds = SpaceAge.days * SpaceAge.hours * SpaceAge.minutes * SpaceAge.seconds * year

        return round(seconds / year_in_seconds, 2)

        

        