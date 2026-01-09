from game import Player   # assuming your main code is saved as leaderboard.py
def test_player_rank():
    # Test case: Player with high scores should be "Legend"
    username = "GamerX"
    game_title = "BattleZone"
    level = "Elite"
    scores = [950, 980, 970]  # average = 966.67

    expected_output = {
        "Username": username,
        "Game Title": game_title,
        "Level": level,
        "Scores": scores,
        "Average": sum(scores) / len(scores),
        "Rank Badge": "Legend"
    }

    # Create player object
    player = Player(username, game_title, level, scores)

    # Compare expected vs actual
    assert player.username == expected_output["Username"]
    assert player.game_title == expected_output["Game Title"]
    assert player.level == expected_output["Level"]
    assert player.scores == expected_output["Scores"]
    assert abs(player.average - expected_output["Average"]) < 0.01  # float comparison
    assert player.rank == expected_output["Rank Badge"]
