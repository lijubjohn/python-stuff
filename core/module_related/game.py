# game.py
# import the draw module
import core.module_related.draw as draw


def play_game():
    print("play game")

def driver():
    play_game()
    draw.draw_game()

# this means that if this script is executed, then
# main() will be executed
if __name__ == '__main__':
    driver()