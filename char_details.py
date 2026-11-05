class Uma:
    def __init__(self, png, name, title, stats, track_aptitude, distance_aptitude, style_aptitude):
        self.png = png
        self.name = name
        self.title = title
        self.stats = stats
        self.track_aptitude = track_aptitude
        self.distance_aptitude = distance_aptitude
        self.style_aptitude = style_aptitude

    def to_rows(self):
        row1 = [
            # Character details
            self.png, 
            self.name, 
            # Stat values
            self.stats.speed,
            self.stats.stamina,
            self.stats.power,
            self.stats.guts,
            self.stats.wit,
           # Track aptitude
            self.track_aptitude.turf,
            self.track_aptitude.dirt,
            # Distance aptitude
            self.distance_aptitude.sprint,
            self.distance_aptitude.mile,
            self.distance_aptitude.medium,
            self.distance_aptitude.long,
            # Style aptitude
            self.style_aptitude.front,
            self.style_aptitude.pace,
            self.style_aptitude.late,
            self.style_aptitude.end,
        ]

        row2 = [
            # title
            "",
            self.title,
            # Stat growths
            self.stats.speed_growth,
            self.stats.stamina_growth,
            self.stats.power_growth,
            self.stats.guts_growth,
            self.stats.wit_growth,
            "", "", "", "", "", "", "", "", "", "",
        ]

        return [row1, row2]

    @staticmethod
    def get_headers(stat_headers):
        header_row = [
            "Image",
            "Name",
            stat_headers[0], stat_headers[1], stat_headers[2], stat_headers[3], stat_headers[4],
            "Turf",
            "Dirt",
            "Sprint", "Mile", "Medium", "Long",
            "Front", "Pace", "Late", "End",
        ]

        return header_row

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