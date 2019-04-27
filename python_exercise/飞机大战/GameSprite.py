import pygame
from plane_sprite import *


class PlaneGame(object):
        # 飞机大战主方法

        def __init__(self):
                print('游戏初始化')

                # 创建游戏窗口
                self.screen = pygame.display.set_mode(SCREEN_RECT.size)
                # 创建游戏时钟
                self.clock = pygame.time.Clock()
                # 调用私有方法，精灵和精灵族的创建
                self.__create_sprites()
                # 设置定时器时间 -创建敌机
                pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)

                pygame.time.set_timer(HERO_FIRE, 400)

        def __create_sprites(self):
                # 创建背景精灵组
                bg1 = BackGround()
                bg2 =BackGround(True)
                self.black_group = pygame.sprite.Group(bg1, bg2)

                #创建敌机精灵组
                self.enemy_group = pygame.sprite.Group()

                self.hero = Hero()
                self.hero_group = pygame.sprite.Group(self.hero)

        def __event_handler(self):
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                PlaneGame.__game_over()
                        elif event.type == CREATE_ENEMY_EVENT:
                                print('敌机出场')
                                #创建敌机精灵，将敌机创建到敌机精灵组
                                enemy = Enemy()
                                self.enemy_group.add(enemy)
                        #elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:     只嗯一下有用
                         #       print("向右移动")

                        elif event.type == HERO_FIRE:
                                self.hero.fire()


                # 使用键盘提供的方法获取键盘按键 -按键元组
                keys_pressd = pygame.key.get_pressed()
                #判断元组中对应的按键索引值 1
                if keys_pressd[pygame.K_RIGHT]:
                        self.hero.speed = 2
                elif keys_pressd[pygame.K_LEFT]:
                        self.hero.speed = -2
                else:
                        self.hero.speed = 0


        def __check_collide(self):
                pygame.sprite.groupcollide(self.hero.bullets_group, self.enemy_group, True, True)
                #pygame.sprite.spritecollide(self.hero, self.enemy_group,  True)
                enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group , True)
                if len(enemies) >0:
                        self.hero.kill()
                        PlaneGame.__game_over()

        def __update_sprites(self):

                self.black_group.update()
                self.black_group.draw(self.screen)

                self.enemy_group.update()
                self.enemy_group.draw(self.screen)

                self.hero_group.update()
                self.hero_group.draw(self.screen)

                self.hero.bullets_group.update()
                self.hero.bullets_group.draw(self.screen)




        @staticmethod
        def __game_over():
                print('游戏结束')

                pygame.quit()
                exit()

        def start_game(self):
                print('游戏开始')
                while True:
                        # 设置刷新帧率
                        self.clock.tick(SHUA_XIN_ZHEN_LV)
                        # 事件监听
                        self.__event_handler()
                        # 碰撞检测
                        self.__check_collide()
                        # 更新/绘制精灵
                        self.__update_sprites()
                        # 更新显示

                        pygame.display.update()
                        pass


if __name__ == '__main__':

        # 创建游戏对象
        game = PlaneGame()

        # 启动游戏
        game.start_game()
