# DCS comp.
import pygame

# Инициализация Pygame
pygame.init()

# Инициализация фреймов
frame_time = pygame.time.Clock()

# Установка экрана с возможностью изменения размера
screen = pygame.display.set_mode((1400, 900))

# Название игры и иконка
pygame.display.set_caption("Robot Fights")
pygame.display.set_icon(pygame.image.load("image/icon2.png"))

# Фон
back_1 = pygame.image.load("image/fon.png")

# Игрок для одиночки
player_1 = [
    pygame.image.load("image/walk1.png"),
    pygame.image.load("image/walk2.png"),
    pygame.image.load("image/walk3.png"),
    pygame.image.load("image/walk4.png"),
    pygame.image.load("image/walk5.png"),
    pygame.image.load("image/walk6.png"),
    pygame.image.load("image/walk7.png"),
    pygame.image.load("image/walk8.png"),
    pygame.image.load("image/walk9.png"),
    pygame.image.load("image/walk10.png"),
    pygame.image.load("image/walk11.png"),
    pygame.image.load("image/walk12.png"),
    pygame.image.load("image/walk13.png"),
    pygame.image.load("image/walk14.png"),
    pygame.image.load("image/walk15.png"),
    pygame.image.load("image/walk16.png"),
    pygame.image.load("image/walk17.png"),
    pygame.image.load("image/walk18.png"),
    pygame.image.load("image/walk19.png"),
    pygame.image.load("image/walk20.png")
]

# Надпись рестарта
restart = pygame.image.load("image/rest_image.png")

# Для фикса бага с пулей
play_shot = True

# Время последнего выстрела
last_shot_time = 0
# Задержка выстрела
shot_delay = 600


# Функция возврата
def reset_game():
    global anim_count, anim_back, shot_count_1, bullets, player_speed, player_x1, player_y1, boss_x, boss_health
    global jump_start, jump_count, enemy_speed, score, run_game, background_stopped, speed_boss
    global play_shot, cup_speed, cup_x, boss_y, em_pos_1, em_pos_2, em_pos_3, em_pos_4, en_1_y, en_2_y, en_3_y, en_4_y
    anim_count = 0
    anim_back = 0
    shot_count_1 = 1000
    bullets = []
    player_speed = 14
    player_x1 = 80
    player_y1 = 435
    jump_start = False
    jump_count = 15
    enemy_speed = 14
    score = 0
    run_game = True
    background_stopped = False
    boss_x = 3500
    speed_boss = 4
    boss_health = 16
    play_shot = True
    cup_speed = 3
    cup_x = 3900
    boss_y = 150
    em_pos_1 = 1500
    em_pos_2 = 3200
    em_pos_3 = 4900
    em_pos_4 = 6600

    en_1_y = 540
    en_2_y = 540
    en_3_y = 540
    en_4_y = 540


# Переменные анимаций
anim_count = 0
anim_back = 0

# Заряды
shot_count_1 = 10000
bullet = pygame.image.load('image/shot_bull.png')
bullets = []

# Скорость и координаты
player_speed = 14
player_x1 = 80
player_y1 = 435

# Прыжок
jump_start = False
jump_count = 15
jump_height = 3

# Противники
em_1_t = pygame.image.load('image/em1.png')
em_2_t = pygame.image.load('image/em2.png')
em_3_t = pygame.image.load('image/em3.png')
em_4_t = pygame.image.load('image/em4.png')

em_pos_1 = 1500
em_pos_2 = 3200
em_pos_3 = 4900
em_pos_4 = 6600

en_1_y = 540
en_2_y = 540
en_3_y = 540
en_4_y = 540

# Скорость врагов
enemy_speed = 14

# Босс игры
boss = pygame.image.load("image/boss.png")
boss_x = 3500
boss_y = 150
speed_boss = 4
boss_health = 16
speed_boss_y = 200

# Счёт
score = 0

# Кубок
cup = pygame.image.load('image/cup.png')
cup_speed = 3
cup_x = 3900
won_fon = pygame.image.load('image/won_tab.png')

# Переменная для остановки фона
background_stopped = False

# Переменные фона и персонажей
back = pygame.image.load("image/fon_2.png")

player_shot_1_two = True
player_shot_2_two = True

# Левый персонаж
player_game_1_two = [
    pygame.image.load('image/left1.png'),
    pygame.image.load('image/left2.png'),
    pygame.image.load('image/left3.png'),
    pygame.image.load('image/left4.png'),
    pygame.image.load('image/left5.png'),
    pygame.image.load('image/left6.png'),
    pygame.image.load('image/left7.png'),
    pygame.image.load('image/left8.png'),
    pygame.image.load('image/left9.png'),
    pygame.image.load('image/left10.png'),
    pygame.image.load('image/left11.png'),
    pygame.image.load('image/left12.png'),
    pygame.image.load('image/left13.png'),
    pygame.image.load('image/left14.png'),
    pygame.image.load('image/left15.png'),
    pygame.image.load('image/left16.png'),
    pygame.image.load('image/left17.png'),
    pygame.image.load('image/left18.png'),
    pygame.image.load('image/left19.png'),
    pygame.image.load('image/left20.png')
]
# Правый персонаж
player_game_2_two = [
    pygame.image.load('image/right1.png'),
    pygame.image.load('image/right2.png'),
    pygame.image.load('image/right3.png'),
    pygame.image.load('image/right4.png'),
    pygame.image.load('image/right5.png'),
    pygame.image.load('image/right6.png'),
    pygame.image.load('image/right7.png'),
    pygame.image.load('image/right8.png'),
    pygame.image.load('image/right9.png'),
    pygame.image.load('image/right10.png'),
    pygame.image.load('image/right11.png'),
    pygame.image.load('image/right12.png'),
    pygame.image.load('image/right13.png'),
    pygame.image.load('image/right14.png'),
    pygame.image.load('image/right15.png'),
    pygame.image.load('image/right16.png'),
    pygame.image.load('image/right17.png'),
    pygame.image.load('image/right18.png'),
    pygame.image.load('image/right19.png'),
    pygame.image.load('image/right20.png')
]

anim_1_two = 0
anim_2_two = 0


# Функция возврата для 2 игры
def reset_game_two():
    global shot_count_1_two, shot_count_2_two, anim_2_two, anim_1_two, player_shot_1_two, player_shot_2_two, bullets_1_two
    global player_y2_two, bullets_2_two, player_speed_two, player_x1_two, player_x2_two, player_y1_two, jump_start_1_two
    global jump_count_1_two, jump_start_2_two, score_1_two, score_2_two, jump_count_2_two, shot_delay_two, last_shot_time_1_two, last_shot_time_2_two
    anim_1_two = 0
    anim_2_two = 0
    shot_count_1_two = 1000
    shot_count_2_two = 1000
    player_shot_1_two = True
    player_shot_2_two = True
    bullets_1_two = []
    bullets_2_two = []
    player_speed_two = 20
    player_x1_two = 100
    player_x2_two = 1050
    player_y1_two = 450
    player_y2_two = 450
    jump_start_1_two = False
    jump_count_1_two = 13
    jump_start_2_two = False
    jump_count_2_two = 13
    score_1_two = 0
    score_2_two = 0
    shot_delay_two = 800
    last_shot_time_1_two = 0
    last_shot_time_2_two = 0


# Пули
shot_count_1_two = 1000
shot_count_2_two = 1000
bullet_1_two = pygame.image.load('image/bullet_shot_1.png')
bullet_2_two = pygame.image.load('image/bullet_shot_2.png')
bullets_1_two = []
bullets_2_two = []

# Скорость, координаты и прыжок
player_speed_two = 20
player_x1_two = 100
player_x2_two = 1050
player_y1_two = 450
player_y2_two = 450

jump_start_1_two = False
jump_count_1_two = 13

jump_start_2_two = False
jump_count_2_two = 13

# Счет
score_1_two = 0
score_2_two = 0
score_font_two = pygame.font.Font(None, 100)

# Время последнего выстрела для обоих игроков
last_shot_time_1_two = 0
last_shot_time_2_two = 0
shot_delay_two = 800  # Задержка между выстрелами

# Надписи победы
win_tab_left = pygame.image.load("image/win_left.png")
win_tab_right = pygame.image.load("image/win_right.png")

# Изображения меню и инструкции
menu_fon = pygame.image.load('image/fon_menu.png')
manual_game = pygame.image.load("image/manual_fon.png")
game_1 = False
game_2 = False
game_menu = True
manual_fon = False

# Бесконечный цикл игры
run_game = True
while run_game:
    # Нажатие на кнопку чтобы, перейти куда нужно
    menu_keys = pygame.key.get_pressed()
    if game_menu:
        screen.blit(menu_fon, (0, 0))
        pygame.display.update()

        if menu_keys[pygame.K_m]:
            game_menu = False
            game_2 = False
            game_1 = True
            reset_game()
        if menu_keys[pygame.K_n]:
            game_menu = False
            game_2 = True
            game_1 = False
            reset_game()
        if menu_keys[pygame.K_b]:
            game_menu = False
            game_2 = False
            game_1 = False
            manual_fon = True

    if manual_fon:
        game_menu = False
        game_2 = False
        game_1 = False
        screen.blit(manual_game, (0, 0))

    if game_1:

        # Отрисовка фона и игроков
        screen.blit(back_1, (anim_back, 0))
        screen.blit(back_1, (anim_back + 2800, 0))
        screen.blit(player_1[anim_count], (player_x1, player_y1))

        # Отрисовка счета
        score_font = pygame.font.Font(None, 50)  # выбираем шрифт и размер для счета
        score_text = score_font.render("Score: " + str(score), True, (255, 255, 255))  # создаем текст с текущим счетом
        screen.blit(score_text, (10, 10))  # выводим текст счета на экран

        # Отрисовка босса
        screen.blit(boss, (boss_x, boss_y))
        boss_rect = boss.get_rect(topleft=(boss_x, boss_y))
        boss_x -= speed_boss

        # Отрисовка кубка
        screen.blit(cup, (cup_x, 450))
        cup_x -= cup_speed
        cup_rect = cup.get_rect(topleft=(cup_x, 450))

        # Призраки
        screen.blit(em_1_t, (em_pos_1, en_1_y))
        screen.blit(em_2_t, (em_pos_2, en_2_y))
        screen.blit(em_3_t, (em_pos_3, en_3_y))
        screen.blit(em_4_t, (em_pos_4, en_4_y))
        em_pos_1 -= enemy_speed
        em_pos_2 -= enemy_speed
        em_pos_3 -= enemy_speed
        em_pos_4 -= enemy_speed

        # Отрисовка невидимых квадратов
        player_rect = player_1[0].get_rect(topleft=(player_x1, player_y1))
        enemy_rect_1 = em_1_t.get_rect(topleft=(em_pos_1, en_1_y))
        enemy_rect_2 = em_2_t.get_rect(topleft=(em_pos_2, en_2_y))
        enemy_rect_3 = em_3_t.get_rect(topleft=(em_pos_3, en_3_y))
        enemy_rect_4 = em_4_t.get_rect(topleft=(em_pos_4, en_4_y))

        # Нажатие клавиш влево и вправо
        press_key = pygame.key.get_pressed()
        if press_key[pygame.K_LEFT] and player_x1 > 70:
            player_x1 -= player_speed
        elif press_key[pygame.K_RIGHT] and player_x1 < 550:
            player_x1 += player_speed

        # Прыжок
        if not jump_start:
            if press_key[pygame.K_SPACE]:
                jump_start = True
        else:
            anim_count = 0
            if jump_count >= -15:
                if jump_count > 0:
                    player_y1 -= (jump_count ** 2) / jump_height
                else:
                    player_y1 += (jump_count ** 2) / jump_height
                jump_count -= 1

            else:
                jump_start = False
                jump_count = 15

        # Пули и счет в игре
        if play_shot:
            if bullets:
                for (q, el) in enumerate(bullets):
                    screen.blit(bullet, (el.x, el.y))
                    el.x += 17

                    if el.x > 1450:
                        bullets.pop(q)

                    if el.colliderect(enemy_rect_1):
                        score += 1000
                        en_1_y += 400
                        bullets.pop(q)
                    elif el.colliderect(enemy_rect_2):
                        score += 1000
                        en_2_y += 400
                        bullets.pop(q)
                    elif el.colliderect(enemy_rect_3):
                        score += 1000
                        en_3_y += 400
                        bullets.pop(q)
                    elif el.colliderect(enemy_rect_4):
                        score += 1000
                        en_4_y += 400
                        bullets.pop(q)
                    elif el.colliderect(boss_rect):
                        score += 1000
                        boss_health -= 1
                        bullets.pop(q)
                        if boss_health == 0:
                            boss_y += 1400

        # Обнуление анимации персонажа и запуск ее заново
        if anim_count == 19:
            anim_count = 0
        else:
            anim_count += 1

        # Проверка столкновения и остановка игры
        if (player_rect.colliderect(enemy_rect_1) or player_rect.colliderect(enemy_rect_2) or player_rect.colliderect(enemy_rect_3) or player_rect.colliderect(enemy_rect_4) or player_rect.colliderect(boss_rect)
                or player_rect.colliderect(cup_rect)):
            anim_count = 0
            enemy_speed = 0
            player_speed = 0
            jump_count = 0
            speed_boss = 0
            bullets.clear()
            shot_count_1 = 0
            cup_speed = 0
            play_shot = False
            if player_rect.colliderect(cup_rect):
                screen.blit(won_fon, (380, 200))
            else:
                screen.blit(restart, (200, 100))
            background_stopped = True
        else:
            background_stopped = False

        # Движение фона
        if not background_stopped:
            anim_back -= 3
        if anim_back <= -2800:
            anim_back = 0

        # Корректный выход
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    reset_game()
            # Обработка клавиши F
            if event.type == pygame.KEYUP and event.key == pygame.K_f and shot_count_1 != 0:
                current_time = pygame.time.get_ticks()
                if current_time - last_shot_time >= shot_delay:
                    bullet_rect = pygame.Rect(player_x1 + 220, player_y1 + 116, bullet.get_width(), bullet.get_height())
                    bullets.append(bullet_rect)
                    last_shot_time = current_time

        # Количество фреймов
        frame_time.tick(30)

    if game_2:
        screen.blit(back, (0, 0))
        screen.blit(player_game_1_two[anim_1_two], (player_x1_two, player_y1_two))
        screen.blit(player_game_2_two[anim_2_two], (player_x2_two, player_y2_two))

        # Отображение счёта игроков
        score_text_1 = score_font_two.render(str(score_1_two), True, (255, 255, 255))
        score_text_2 = score_font_two.render(str(score_2_two), True, (255, 255, 255))

        # Отображение счёта игрока 1 в верхней части экрана
        text_rect_1 = score_text_1.get_rect(center=(650, 125))
        screen.blit(score_text_1, text_rect_1)

        # Отображение счёта игрока 2 в верхней части экрана
        text_rect_2 = score_text_2.get_rect(center=(750, 125))
        screen.blit(score_text_2, text_rect_2)

        # Квадраты для персонажей
        player_1_rect_two = player_game_1_two[0].get_rect(topleft=(player_x1_two, player_y1_two))
        player_2_rect_two = player_game_2_two[0].get_rect(topleft=(player_x2_two, player_y2_two))

        # Нажатие клавиш
        press_1 = pygame.key.get_pressed()
        if press_1[pygame.K_a] and player_x1_two > 100:
            player_x1_two -= player_speed_two
        if press_1[pygame.K_LEFT] and player_x2_two > 750:
            player_x2_two -= player_speed_two

        if press_1[pygame.K_d] and player_x1_two < 400:
            player_x1_two += player_speed_two
        if press_1[pygame.K_RIGHT] and player_x2_two < 1050:
            player_x2_two += player_speed_two

        # Анимация для первого
        if anim_1_two == 19:
            anim_1_two = 0
        else:
            anim_1_two += 1

        # Анимация для второго
        if anim_2_two == 19:
            anim_2_two = 0
        else:
            anim_2_two += 1

        # Прыжок для первого
        if not jump_start_1_two:
            if press_1[pygame.K_w]:
                jump_start_1_two = True
        else:
            anim_1_two = 0
            if jump_count_1_two >= -13:
                if jump_count_1_two > 0:
                    player_y1_two -= (jump_count_1_two ** 2) / 2.2
                else:
                    player_y1_two += (jump_count_1_two ** 2) / 2.2
                jump_count_1_two -= 1
            else:
                jump_start_1_two = False
                jump_count_1_two = 13

        # Прыжок для второго
        if not jump_start_2_two:
            if press_1[pygame.K_UP]:
                jump_start_2_two = True
        else:
            anim_2_two = 0
            if jump_count_2_two >= -13:
                if jump_count_2_two > 0:
                    player_y2_two -= (jump_count_2_two ** 2) / 2.2
                else:
                    player_y2_two += (jump_count_2_two ** 2) / 2.2

                jump_count_2_two -= 1
            else:
                jump_start_2_two = False
                jump_count_2_two = 13

        if player_shot_1_two:
            # Пульки для первого игрока
            for bullet_66 in bullets_1_two:
                screen.blit(bullet_1_two, (bullet_66.x, bullet_66.y))
                bullet_66.x += 16
                if bullet_66.colliderect(player_2_rect_two):
                    score_1_two += 1
                    bullets_1_two.remove(bullet_66)
                elif bullet_66.x > 1400:
                    bullets_1_two.remove(bullet_66)

        if player_shot_2_two:
            # Пульки для второго игрока
            for bullet_66 in bullets_2_two:
                screen.blit(bullet_2_two, (bullet_66.x, bullet_66.y))
                bullet_66.x -= 16
                if bullet_66.colliderect(player_1_rect_two):
                    score_2_two += 1
                    bullets_2_two.remove(bullet_66)
                elif bullet_66.x < 0:
                    bullets_2_two.remove(bullet_66)

        if score_1_two == 10:
            screen.blit(win_tab_left, (400, 200))
            anim_1_two = 0
            anim_2_two = 0
            jump_count_1_two = 0
            jump_count_2_two = 0
            bullets_1_two.clear()
            bullets_2_two.clear()
            player_shot_2_two = False
            player_shot_1_two = False
            shot_count_1_two = 0
            shot_count_2_two = 0
            player_speed_two = 0
        if score_2_two == 10:
            screen.blit(win_tab_right, (400, 200))
            anim_1_two = 0
            anim_2_two = 0
            jump_count_1_two = 0
            jump_count_2_two = 0
            bullets_1_two.clear()
            bullets_2_two.clear()
            player_shot_2_two = False
            player_shot_1_two = False
            shot_count_1_two = 0
            shot_count_2_two = 0
            player_speed_two = 0

        # Корректный выход
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    reset_game_two()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_g and shot_count_1_two != 0:
                    current_time = pygame.time.get_ticks()
                    if current_time - last_shot_time_1_two >= shot_delay_two:
                        bullet_rect_two_1 = bullet_1_two.get_rect(topleft=(player_x1_two + 250, player_y1_two + 163))
                        bullets_1_two.append(bullet_rect_two_1)
                        last_shot_time_1_two = current_time
                if event.key == pygame.K_p and shot_count_2_two != 0:
                    current_time = pygame.time.get_ticks()
                    if current_time - last_shot_time_2_two >= shot_delay_two:
                        bullet_rect_two_2 = bullet_2_two.get_rect(topleft=(player_x2_two - 40, player_y2_two + 163))
                        bullets_2_two.append(bullet_rect_two_2)
                        last_shot_time_2_two = current_time

        # Количество фреймов
        frame_time.tick(30)

    if menu_keys[pygame.K_ESCAPE]:
        game_menu = True
        game_1 = False
        game_2 = False
        manual_fon = False

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or menu_keys[pygame.K_BACKSPACE]:
            run_game = False
            pygame.quit()
