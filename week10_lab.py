'''
class Movie:
    def __init__(self):
        self.title = ""
        self.genres = []
        self.scariness = 0
        self.duration = 0

    def get_title(self):
        return self.title
    def set_title(self, value):
        self.title = value

    def get_genre(self):
        output = ""
        for genre in self.genres:
            output += f" {genre}"
        return output
    def set_genre(self, value):
        self.genres.append(value)
    
    def get_duration(self):
        return self.duration
    def set_duration(self, value):
        if 0 < value <= 10:
            self.duration = value
    
    def get_scariness(self):
        return self.scariness
    def set_scariness(self, value):
        if 0 < value <= 10:
            self.scariness = value
    

    def get_description(self):
        description = "This movie is a "
        if 0 < self.duration <= 3:
            description += "short, "
        else:
            description += "long, "

        if 0 < self.scariness <= 5:
            description += "not scary, "
        else:
            description += "scary, "
        description += "movie titled {self.title}."
        return description

    def __str__(self):
        return f"{self.title} of genre {self.get_genre()} duration is {self.duration} and scariness is {self.scariness}."
    

movie1 = Movie()
movie1.set_title("The Lord of the Rings: Fellowship of the Ring")
movie1.set_genre(["Fantasy", "Fiction"])
'''


class Color_Wheel:
    def __init__(self, _magenta, _yellow, _cyan):
        self.magenta = _magenta
        self.yellow = _yellow
        self.cyan = _cyan
    def get_color(self):
        if 0 <= (self.magenta and self.yellow and self.cyan):
            if self.magenta == self.cyan != self.yellow:
                color = "Blue"
            elif self.magenta == self.yellow != self.cyan:
                color = "Red"
            elif self.yellow > (self.magenta and self.cyan):
                color = "Yellow"
            elif self.yellow == self.cyan != self.magenta:
                color = "Green"
            elif self.cyan > (self.yellow and self.magenta):
                color = "Cyan"
            elif self.magenta > (self.yellow and self.cyan):
                color = "Magenta"
            elif (self.magenta and self.yellow and self.cyan) == 0:
                color = "White"
            elif self.magenta == self.yellow == self.cyan:
                color = "Black"
            elif (self.magenta + self.yellow) == self.cyan:
                color = "Purple"
            elif self.magenta == self.yellow/2:
                color = "Orange"
            return color
    def adjust_color(self,color,value):
        if color == "magenta": self.magenta += value
        if color == "yellow": self.yellow += value
        if color == "cyan": self.cyan += value

color = Color_Wheel(1,1,2)
print(color.get_color())
