





def play(round):


    transform_dict = {
        "A":"rock",
        "B":"paper",
        "C":"scissors",
        "X":"rock",
        "Y":"paper",
        "Z":"scissors",
    }

    win_dict = {
        "rock":"paper",
        "paper":"scissors",
        "scissors":"rock"
    }

    points_dict = {
        "rock": 1,
        "paper": 2,
        "scissors": 3,
    }

    try:
        player_a, player_b = round.split()
    except:
        print("invalid round")
        return 0

    player_a = transform_dict[player_a]
    player_b = transform_dict[player_b]


    result = 0
    if player_a == player_b:
        result = 3
    elif player_b == win_dict[player_a]:
        result = 6
    else:
        result = 0

    return result + points_dict[player_b]

    
with open("advent_of_code\day_2\data.txt", mode="r") as data_file:
    data = data_file.read().split("\n")

round_scores = [play(round) for round in data]

print(f"Total Score: {sum(round_scores)}")


def decide_strategy(player_a, expected_result):

    expected_result_dict = {
        "X":"lose",
        "Y":"draw",
        "Z":"win",
    }
    win_dict = {
        "rock":"paper",
        "paper":"scissors",
        "scissors":"rock"
    }
    lose_dict = {
        "rock":"scissors",
        "paper":"rock",
        "scissors":"paper"
    }


    expected_result = expected_result_dict[expected_result]
    if expected_result == "draw":
        return player_a
    if expected_result == "win":
        return win_dict[player_a]
    else:
        return lose_dict[player_a]


def play_s2(round):


    transform_dict = {
        "A":"rock",
        "B":"paper",
        "C":"scissors",
    }

    win_dict = {
        "rock":"paper",
        "paper":"scissors",
        "scissors":"rock"
    }

    points_dict = {
        "rock": 1,
        "paper": 2,
        "scissors": 3,
    }


    try:
        player_a, expected_result = round.split()
    except:
        print("invalid round")
        return 0

    player_a = transform_dict[player_a]


    player_b = decide_strategy(player_a, expected_result)


    result = 0
    if player_a == player_b:
        result = 3
    elif player_b == win_dict[player_a]:
        result = 6
    else:
        result = 0

    return result + points_dict[player_b]


round_scores = [play_s2(round) for round in data]

print(f"Total Score with strategy 2: {sum(round_scores)}")