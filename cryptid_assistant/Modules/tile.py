class Tile:

    nodes = [] # list of TileNodes in 6 cols x 3 rows
    def __init__(self, id, nodes):
        self.id = id
        self.nodes = nodes

    def __repr__(self):
        output = f"Tile {self.id} contains the following nodes:\n"
        for row in self.nodes:
            output += "row: \n"
            for node in row:
                output += str(node) + "\n"
        return output

    def invert_nodes(self):
        self.nodes.reverse()
        for node_list in self.nodes:
            node_list.reverse()