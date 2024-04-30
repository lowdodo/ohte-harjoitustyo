from players.player import Player

def test_player_name(session):
    player = Player(name="testname")

    session.add(player)
    session.commit()

    assert player.name is not None