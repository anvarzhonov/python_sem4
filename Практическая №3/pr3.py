class C32:
    def __init__(self):
        self.state = "A"

    def roam(self):
        if self.state == "A":
            self.state = "B"
            return 0
        elif self.state == "E":
            self.state = "F"
            return 5
        elif self.state == "F":
            self.state = "G"
            return 6
        else:
            raise RuntimeError

    def hike(self):
        if self.state == "B":
            return 2
        elif self.state == "F":
            self.state= "B"
            return 7
        elif self.state == "G":
            return 9
        else:
            raise RuntimeError

    def slur(self):
        if self.state == "B":
            self.state = "C"
            return 1
        if self.state == "C":
            self.state = "D"
            return 3
        if self.state == "D":
            self.state = "E"
            return 4
        if self.state == "F":
            self.state = "C"
            return 8
        else:
            raise RuntimeError
