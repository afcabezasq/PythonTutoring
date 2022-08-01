class Room:
    def __init__(self, person, width, length):
        self.person = person
        self.width = width
        self.length = length

    def __repr__(self):
        repr = f"""Owner: {self.person}
Measurements: {self.width}x{self.length}\n"""
        return repr
