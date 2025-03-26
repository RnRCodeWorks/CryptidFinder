from cryptid_assistant.Modules import tile, tileNode, gameMap
from Config import tile_layouts, setup_cards

def generate_tiles():
    generated_tiles = []
    for key, value in tile_layouts.items():
        tile_nodes = []
        for row in value:
            row_nodes = []
            for node in row:
                node_params = node.split("|")
                tile_node = tileNode.TileNode(node_params[0], node_params[1] if len(node_params)>1 else "none")
                row_nodes.append(tile_node)
            tile_nodes.append(row_nodes)
        generated_tile = tile.Tile(key, tile_nodes)
        generated_tiles.append(generated_tile)
    return generated_tiles

def generate_game(key, player_count):
    if player_count < 3 or player_count > 5:
        return "Invalid player count"
    return gameMap.GameMap(key, generate_tiles(), player_count)

game_map = generate_game(615432, 3)
game_map.populate_map()