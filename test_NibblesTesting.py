import time

def test_intro_time():
    timeLimit = time.time() + 5 * 1
    assert time.time() < timeLimit

def test_snake_speed():
    snake_speed = 15
    timePass = time.time() + 5 * 1
    while time.time() < timePass:
        new_snake_speed = snake_speed + snake_speed
    assert new_snake_speed > snake_speed


def test_gameloop_start():
    game_over, game_close = False, False
    assert game_over == True
    assert game_close == True

def test_snake():
    snake_block = 10
    assert snake_block == 0