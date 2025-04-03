
from cryptid_assistant.scripts.clues import alpha, beta, epsilon

class SolutionFinder:

    def __init__(self, game_map):
        self.game_map = game_map

    def check_structure_range(self, structure, max_range, x_coord, y_coord):
        #structure_coords are added by row index then col index ie [y, x]
        structure_coords = []
        if structure.structure_type == self.game_map.standing_stone_key:
            structure_coords = self.game_map.standing_stones[structure.color]
        elif structure.structure_type == self.game_map.abandoned_shack_key:
            structure_coords = self.game_map.abandoned_shacks[structure.color]

        if x_coord == structure_coords[0]:
            hex_distance = abs(y_coord - structure_coords[1])
        elif y_coord == structure_coords[1]:
            hex_distance = abs(x_coord - structure_coords[0])
        else:
            hex_distance = abs((x_coord-y_coord) * -1 - (structure_coords[0] - structure_coords[1] * -1))

        if 0 < hex_distance <= max_range:
                return True
        return False

    def solve(self):
        active_clues = []
        alpha_index = self.game_map.clues[0]
        beta_index = self.game_map.clues[1]
        charlie_index = self.game_map.clues[2]
        delta_index = self.game_map.clues[3]
        epsilon_index = self.game_map.clues[4]

        if alpha_index != -1:
            active_clues.append(alpha[alpha_index])
        if beta_index != -1:
            active_clues.append(beta[beta_index])
        if epsilon_index != -1:
            active_clues.append(epsilon[epsilon_index])

        possible_nodes = []

        for y_coord in range(len(self.game_map.aligned_tiles)):
            node_line = self.game_map.aligned_tiles[y_coord]
            for x_coord in range(len(node_line)):
                node = node_line[x_coord]
                matched_clues = len(active_clues)
                for clue in active_clues:
                    if matched_clues < len(active_clues):
                        break
                    if len(clue['range']) == 1 and clue['range'][0] == 0:
                        # Assumes absolute clues will only be of one type ie territory, terrain, or structure
                        if len(clue['terrain']) > 0:
                            if node.terrain_type in clue['terrain']:
                                continue
                        if len(clue['structure']) > 0:
                            if node.structure_type in clue['structure']:
                                continue
                        if len(clue['territory']) > 0:
                            if clue['territory'] in node.structure_type:  # Clues may have multiple territories, but nodes will only ever be one
                                continue
                        matched_clues -= 1
                    elif clue['range'][0] == 0 and clue['range'][1] > 0:
                        if len(clue['structure']) > 0:
                            valid_structure_found = False
                            for structure in clue['structure']:
                                if self.check_structure_range(structure, clue['range'][1], x_coord, y_coord):
                                    valid_structure_found = True
                                    break
                            if not valid_structure_found:
                                matched_clues -= 1
                                break
                if matched_clues == len(active_clues):
                    possible_nodes.append('Row '+str(y_coord+1) + ' and column '+str(x_coord+1))

        return possible_nodes

                        