class Structure:
    def __init__(self, structure_type, color):
        self.structure_type = structure_type
        self.color = color
    def __repr__(self):
        return f"{self.color} {self.structure_type}"
    def __eq__(self, other):
        if isinstance(other, Structure):
            return (self.structure_type, self.color) == (other.structure_type, other.color)
        return False

class TileNode:
    # terrain_type = (w)ater, (m)ountain, (s)wamp, (f)orest, (d)esert
    territory = "none" # none, bear, cougar
    structure_type = "none" # none, standing_stone, abandoned_shack

    def __init__(self, terrain_type, territory):
        self.terrain_type = terrain_type
        self.territory = territory

    def add_structure(self, structure, color):
        if structure != "" and color != "":
            self.structure_type = Structure(structure, color)

    def has_cougar(self):
        return self.territory == "cougar"

    def has_bear(self):
        return self.territory == "bear"

    def __repr__(self):
        return f"Node is {self.terrain_type} is the territory of {self.territory} and contains a {self.structure_type}\n"