from game.game import Game

def main():
    game = Game()
    while True:
        game.handle_events()
        game.update()
        game.draw()
        game.clock.tick(60)

if __name__ == '__main__':
    main()
