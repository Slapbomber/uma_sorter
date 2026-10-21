class Uma:
    def __init__(self, png, name, title, stats, track_aptitude, distance_aptitude, style_aptitude):
        self.png = png
        self.name = name
        self.title = title
        self.stats = stats
        self.track_aptitude = track_aptitude
        self.distance_aptitude = distance_aptitude
        self.style_aptitude = style_aptitude

    def to_list(self):
        return [
            #Character details
            self.png, 
            self.name, 
            self.title,
            #Stats & growths
            self.stats.speed,
            self.stats.stamina,
            self.stats.power,
            self.stats.guts,
            self.stats.wit,
            self.stats.speed_growth,
            self.stats.stamina_growth,
            self.stats.power_growth,
            self.stats.guts_growth,
            self.stats.wit_growth,
            # Aptitudes
            self.track_aptitude.turf,
            self.track_aptitude.dirt,
            self.distance_aptitude.sprint,
            self.distance_aptitude.mile,
            self.distance_aptitude.medium,
            self.distance_aptitude.long,
            self.style_aptitude.front,
            self.style_aptitude.pace,
            self.style_aptitude.late,
            self.style_aptitude.end,
            ]

class Stats:
    def __init__(self, speed, stamina, power, guts, wit, speed_growth, stamina_growth, power_growth, guts_growth, wit_growth):
        self.speed = speed
        self.stamina = stamina
        self.power = power
        self.guts = guts
        self.wit = wit
        self.speed_growth = speed_growth
        self.stamina_growth = stamina_growth
        self.power_growth = power_growth
        self.guts_growth = guts_growth
        self.wit_growth = wit_growth

class TrackAptitude:
    def __init__(self, turf, dirt):
        self.turf = turf
        self.dirt = dirt

class DistanceAptitude:
    def __init__(self, sprint, mile, medium, long):
        self.sprint = sprint
        self.mile = mile
        self.medium = medium
        self.long = long

class StyleAptitude:
    def __init__(self, front, pace, late, end):
        self.front = front
        self.pace = pace
        self.late = late
        self.end = end