
import numpy as np

class Submission:
    def __init__(self, board_size, win_size):
        self.board_size = board_size
        self.win_size = win_size

    def evaluate_potential(self, state, player):
        """
        Evaluate the potential of each action for the given player.
        """
        potentials = np.zeros((self.board_size, self.board_size))

        for r in range(self.board_size):
            for c in range(self.board_size):
                if state.board[0, r, c] == 1:  # Check if the position is empty
                    for dr in [-1, 0, 1]:
                        for dc in [-1, 0, 1]:
                            if dr == 0 and dc == 0:
                                continue
                            potentials[r, c] += self.count_consecutive(state, player, r, c, dr, dc)

        return potentials

    def count_consecutive(self, state, player, r, c, dr, dc):
        """
        Count the number of consecutive marks for the given player in a certain direction.
        """
        consecutive = 0
        open_ends = 0
        for i in range(self.win_size):
            nr, nc = r + i * dr, c + i * dc
            if 0 <= nr < self.board_size and 0 <= nc < self.board_size:
                if state.board[player, nr, nc] == 1:
                    consecutive += 1
                elif state.board[0, nr, nc] == 1:
                    open_ends += 1
                else:
                    break
            else:
                break

        for i in range(1, self.win_size):
            nr, nc = r - i * dr, c - i * dc
            if 0 <= nr < self.board_size and 0 <= nc < self.board_size:
                if state.board[player, nr, nc] == 1:
                    consecutive += 1
                elif state.board[0, nr, nc] == 1:
                    open_ends += 1
                else:
                    break
            else:
                break

        return self.calculate_potential(consecutive, open_ends)

    def calculate_potential(self, consecutive, open_ends):
        """
        Calculate the potential based on the number of consecutive marks and open ends.
        """
        if consecutive == self.win_size - 1:
            return 100000
        elif consecutive == self.win_size - 2 and open_ends == 2:
            return 5000
        elif consecutive == self.win_size - 2 and open_ends == 1:
            return 1000
        elif consecutive == self.win_size - 1 and open_ends == 1:
            return 1000
        elif consecutive == self.win_size - 2:
            return 500
        elif consecutive == self.win_size - 1:
            return 100
        elif consecutive == self.win_size - 3 and open_ends == 2:
            return 100
        elif consecutive == self.win_size - 3 and open_ends == 1:
            return 50
        elif consecutive == self.win_size - 2 and open_ends == 0:
            return 50
        elif consecutive == self.win_size - 3:
            return 30
        elif consecutive == self.win_size - 4:
            return 20
        elif consecutive == self.win_size - 5:
            return 10
        else:
            return 1

    def __call__(self, state):
        """
        Select the action with the highest potential based on the heuristic.
        """
        player = state.current_player()
        opponent = 3 - player  # Switch player (1 to 2, 2 to 1)

        player_potentials = self.evaluate_potential(state, player)
        opponent_potentials = self.evaluate_potential(state, opponent)

        total_potentials = player_potentials + opponent_potentials

        # Find the action with the highest total potential
        max_indices = np.argwhere(total_potentials == np.max(total_potentials))
        selected_action = tuple(max_indices[0])

        return selected_action

