# coding=utf-8

import pygame
from sys import exit

# local package
from chess.chess_game import ChessGame, ChessView

if __name__ == "__main__":
    # 显示文字
    # font = pygame.font.Font(pygame.font.get_default_font(), 16)
    # text = font.render("chess - yi", True,(0, 0, 0))
    # screen.blit(text, (0, 0))
    pygame.init()

    game = ChessGame()

    # game loop
    while True:
        game.update()
        # get event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 获取鼠标位置
                pixel_x, pixel_y = pygame.mouse.get_pos()
                x, y = ChessView.Pixel2XY(pixel_x, pixel_y)

                game.select(x, y)