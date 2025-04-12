from cryptid_assistant.Modules import tile, tileNode, gameMap, solutionFinder
from cryptid_assistant.scripts.Config import tile_layouts


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



game_key = 341256
player_count = 4
game_map = generate_game(game_key, player_count)
game_map.populate_map()
solution = solutionFinder.SolutionFinder(game_map)

valid_answers = solution.solve()
game_key = list(str(game_key))

print(f"""
Based on the tile configuration:
{game_key[0]}       {game_key[1]}
{game_key[2]}       {game_key[3]}
{game_key[4]}       {game_key[5]}
With {player_count} players, the solution{ 's are' if len(valid_answers) > 1 else ' is'}:
{valid_answers}
""")
