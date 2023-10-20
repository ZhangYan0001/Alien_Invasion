import sys
import pygame
from setting import Settings
from ship import Ship


# pygame.init() 初始化背景设置
# pygame.display.set_mode() 来创建一个名为screen的显示窗口，这个游戏的所有图形元素都在其中绘制
# 实参(1200,800) 是一个元组 指定了游戏的窗口大小

def run_game():
  pygame.init()
  ai_setting = Settings()
  screen = pygame.display.set_mode(
      (ai_setting.screen_width, ai_setting.screen_height))
  pygame.display.set_caption("Alien Invasion")

# 创建一首飞船
  ship = Ship(screen)
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()

# 每次循环都重绘屏幕
    screen.fill(ai_setting.bg_color)
    ship.blitme()
# 让最近绘制的屏幕可见
    pygame.display.flip()
