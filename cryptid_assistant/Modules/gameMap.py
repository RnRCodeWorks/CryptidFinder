from cryptid_assistant.scripts.Config import setup_cards

class GameMap:
    aligned_tiles = []
    standing_stone_key = "standing_stone"
    abandoned_shack_key = "abandoned_shack"

    def __init__(self, key, generated_tiles, player_count):
        setup_params = setup_cards[key]
        self.tile_layout = list(str(key))
        self.generated_tiles = generated_tiles


        self.inverted_tiles = setup_params['inverted']
        self.standing_stones = setup_params['standing_stones']
        self.abandoned_shacks = setup_params['abandoned_shacks']
        self.clues = setup_params['clues'][player_count]

    def combine_tiles(self, first_tile, second_tile):
        for i in range(3):
            self.aligned_tiles.append(first_tile.nodes[i] + second_tile.nodes[i])

    def position_stones(self):
            for color_key, coords in self.standing_stones.items():
                self.aligned_tiles[coords[1]][coords[0]].add_structure(self.standing_stone_key, color_key)

    def position_shacks(self):
            for color_key, coords in self.abandoned_shacks.items():
                self.aligned_tiles[coords[1]][coords[0]].add_structure(self.abandoned_shack_key, color_key)

    def populate_map(self):
        for index in self.inverted_tiles:
            self.generated_tiles[index-1].invert_nodes()
        for i in range(0, 6, 2):
            first_tile = self.generated_tiles[int(self.tile_layout[i])-1]
            second_tile = self.generated_tiles[int(self.tile_layout[i+1])-1]
            for row in range(3):
                self.aligned_tiles.append(first_tile.nodes[row] + second_tile.nodes[row])
        self.position_stones()
        self.position_shacks()






