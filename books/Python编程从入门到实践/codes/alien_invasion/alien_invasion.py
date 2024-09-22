import sys
import pygame

from settings import Settings


def run_game():
    # 初始化
    pygame.init()

    # 初始化设置
    ai_settings = Settings()
    # 创建一个 Screen
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    # 标题栏文字
    pygame.display.set_caption("Alien Invasion")

    # 主循环
    while True:
        # 监听键鼠事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 填充背景色
        screen.fill(ai_settings.bg_color)
        # 将内容刷新到屏幕
        pygame.display.flip()


run_game()
