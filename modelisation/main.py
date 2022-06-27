from PileSand import PileSand
from ChipFiringGame import ChipFiringGame


def main_pile_sand():
    game = PileSand(5,5, 1, 1)     #(Nb_ligne,Nb_colonne,H,h)
    game.game_representation(2)


def main_cfg():
    game = ChipFiringGame(5,5,1,1)
    game.game_representation(2)


if __name__ == '__main__':
    main_pile_sand()
    main_cfg()
