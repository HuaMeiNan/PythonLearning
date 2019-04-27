import pygame
from python_exercise.PlaneGame.GameSprite import *



class PlaneGame(object):
    # 游戏初始化
    def __init__(self):
        # 创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 创建游戏时钟
        self.clock = pygame.time.Clock()
        # 调用精灵组
        self.__create_sprite()
        # 创建定时器
        pygame.time.set_timer(ENEMY_TIME, 1000)
        pygame.time.set_timer(BULLET_TIME, 400)

    # 游戏开始
    def start_game(self):
        print("游戏开始")
        while True:
            # 设置刷新频率
            self.clock.tick(SHUXINZHENLV)

            # 调用事件监听
            self.__event_handler()
            # 碰撞检测
            self.__check_collide()
            # 更新精灵位置
            self.__upadte_sprite()
            # 更新屏幕显示
            pygame.display.update()

    #创建精灵组
    def __create_sprite(self):
        bg = BackGround()
        bg2 = BackGround(True)
        self.back_ground = pygame.sprite.Group(bg, bg2)

        self.enemy_group = pygame.sprite.Group()

        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    # 事件监听
    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == ENEMY_TIME:
                print('敌机出场')
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif event.type == BULLET_TIME:
                self.hero.fire_bullet()

        keys_pressd = pygame.key.get_pressed()
        if keys_pressd[pygame.K_LEFT]:
            self.hero.speed = -2
        elif keys_pressd[pygame.K_RIGHT]:
            self.hero.speed = 2
        else:
            self.hero.speed = 0

    # 碰撞检测
    def __check_collide(self):
        pygame.sprite.groupcollide(self.hero.bullet_group, self.enemy_group, True, True)
        enemies = pygame.sprite.groupcollide(self.hero_group, self.enemy_group ,True, True)
        if len(enemies) >0:
            PlaneGame.__game_over()

    # 更新精灵位置
    def __upadte_sprite(self):
        self.back_ground.update()
        self.back_ground.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.screen)

    # 游戏结束
    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()

if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()