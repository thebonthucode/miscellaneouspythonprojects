import random

opponent_moves = []
beats = {"r": "p", "p": "s", "s": "r"}
probabilities = {"r": 0.33, "p": 0.33, "s": 0.33}


def move(my_history, their_history):
    if len(their_history) < 2:
        return "r"
    if their_history[-1] == their_history[-2]:
        return beat_move(their_history[-1])
    return random.choice(["r", "p", "s"])


def beat_move(move):
    opponent_moves.append(move)
    update_probabilities()
    return choose_move()


def update_probabilities():
    move_counts = {"r": 0, "p": 0, "s": 0}
    for move in opponent_moves:
        move_counts[move] += 1

    total_moves = len(opponent_moves)
    for move in move_counts:
        probabilities[move] = move_counts[move] / total_moves

    total_probability = sum(probabilities.values())
    if total_probability != 1:
        scaling_factor = 1 / total_probability
        for move in probabilities:
            probabilities[move] *= scaling_factor


def choose_move():
    random_num = random.random()

    cumulative_prob = 0
    for move in probabilities:
        cumulative_prob += probabilities[move]
        if random_num <= cumulative_prob:
            return move

    return random.choice(["r", "p", "s"])
