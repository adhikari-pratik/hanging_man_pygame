import random
import string
import words
import pygame
import hanging_man

pygame.init()
# Name and icon and background
pygame.display.set_caption("Hangman")
rope = pygame.image.load("rope.png")
pygame.display.set_icon(rope)
background = pygame.image.load("images.jfif")
background = pygame.transform.scale(background, (1000, 700))

# colours
white = (255, 255, 255)
light_yellow = (255, 255, 191)
yellow = (255, 255, 0)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# alphabets
alphabets = string.ascii_uppercase
print(alphabets)
word = ""
list_word = []
list_box_pos_x = []
list_box_pos_y = []
box_pos_value_x = []
box_pos_value_y = []
record = 0
answer_list = []
hint_x = 0
hint_y = 0
# change = 0
hint_index = 0
chances = 6
index = []

window = pygame.display.set_mode((1000, 700), pygame.RESIZABLE)

# checks
run_game = True
is_display = True
is_selected = False
is_position = False
in_list = False
is_guessed = False
is_pressed = False
is_first = True
show_hint = False
given = False
is_win = False
is_hanged = False
is_gameover = False
is_restart = False
is_restart_pressed = False


def word_selection():
    global word, is_selected
    all_words = words.word.split(",")
    # print(all_words)
    if not is_selected:
        word_selected = random.choice(all_words)
        for letters in word_selected:
            if letters != " ":
                word += letters
        print(word)
        for letters in word:
            list_word.append(letters)
        print(list_word)
        is_selected = True
    else:
        pass


def letter_box():
    circles = []
    box_pos_x = 58
    box_pos_y = 59
    global is_position
    if not is_position:
        for each in range(len(alphabets)):

            if box_pos_x >= 958:
                box_pos_x = 58
                box_pos_y += 40
            list_box_pos_x.append(box_pos_x)
            list_box_pos_y.append(box_pos_y)
            box_pos_x += 100

        for position in list_box_pos_x:
            values_x = range(position - 17, position + 17)
            box_pos_value_x.append(values_x)
        for position in list_box_pos_y:
            values_y = range(position-17, position+17)
            box_pos_value_y.append(values_y)

        is_position = True
    # print(list_box_pos_y)
    # print(list_box_pos_x)
    j = 0
    for i in range(len(alphabets)):
        circles.append(pygame.draw.circle(window, yellow, (list_box_pos_x[i], list_box_pos_y[j]), 17))
        j += 1
    # print(len(box_pos_value_x), len(box_pos_value_y))


def display_letters():
    letter_pos_x = 50
    letter_pos_y = 50

    for letters in alphabets:
        letter_text = pygame.font.Font("freesansbold.ttf", 24)
        letter = letter_text.render(letters, True, black)
        if letter_pos_x >= 950:
            letter_pos_x = 50
            letter_pos_y += 40

        window.blit(letter, (letter_pos_x, letter_pos_y))
        letter_pos_x += 100


def answer_dash():
    # dash = []
    # global is_display
    # global is_selected
    word_selection()
    dash_x = 50
    dash_y = 550
    dash_len = 24
    # answer_x = 50
    # answer_y = 530
    for i in range(len(word)):
        pygame.draw.line(window, white, (dash_x, dash_y), (dash_x + dash_len, dash_y), width=3)
        dash_x += dash_len + 10
    # is_selected = True
    # answer_text = pygame.font.Font("freesansbold.ttf", 24)
    # for i in range(len(list_word)):
    #     if is_display:
    #         answer_list.append(answer_text.render(alphabets[record], True, black))
    #         # window.blit(answer_list[i], (answer_x, answer_y))
    #         # answer_x += 35
    #         is_display = False
    #     else:
    #         pass


def user_guess():
    # user = ""
    global is_guessed, is_display, is_pressed, is_first
    global record, in_list, index, chances
    letter_guessed = ""
    get_pos = (0, 0)
    get_pos_x, get_pos_y = get_pos
    if not is_pressed:
        if event.type == pygame.MOUSEBUTTONDOWN:
            get_pos = pygame.mouse.get_pos()
            get_pos_x, get_pos_y = get_pos
            # is_display = True
            is_pressed = True
        # in_list = False
    if event.type == pygame.MOUSEBUTTONUP:
        # is_display = False
        is_pressed = False
    for i in range(len(box_pos_value_x)):
        if (get_pos_x in box_pos_value_x[i]) and (get_pos_y in box_pos_value_y[i]):
            record = i
            print(i)
            letter_guessed = alphabets[i]
            print(letter_guessed)
            # in_list = True
            is_guessed = True
            # is_display = True
            print(get_pos)
            # print("pos found")
            # print(type(letter_guessed))
    # if is_first:
    #     index.append(random.randint(0, len(word)))
    #     is_first = False
    if is_guessed:
        if letter_guessed in list_word:
            print("word is in the list")
            # in_list = True
            is_guessed = False
            num = 0
            for letter in list_word:
                if letter_guessed == letter:
                    if num not in index:
                        index.append(num)
                num += 1
            print(index)
            # index.append(list_word.index(letter_guessed))
            # is_display = True
        else:
            print("word not in list")
            # chances = (len(word) + 1)
            chances -= 1
            print(chances)
            is_guessed = False

    answer_text = pygame.font.Font("freesansbold.ttf", 24)
    for i in range(len(word)):
        # if is_display:
        answer_list.append(answer_text.render(list_word[i], True, green))
        # window.blit(answer_list[i], (answer_x, answer_y))
        # answer_x += 35
        # is_display = False
        # else:
        #     pass

    if letter_guessed != "":
        print(letter_guessed)


def print_answer():
    global is_first, is_win
    # is_first = True
    answer_x_initial = 50
    answer_x = []
    answer_y = 525
    # j = 0
    # global in_list
    for i in range(len(word)):
        answer_x.append(answer_x_initial)
        answer_x_initial += 35
    for i in range(len(index)):
        window.blit(answer_list[index[i]], (answer_x[index[i]], answer_y))
        if len(index) == len(list_word):
            is_win = True
        # j += 1
    if is_first:
        rand = random.randint(0, len(list_word)-1)
        window.blit(answer_list[rand], (answer_x[rand], answer_y))
        index.append(rand)
        is_first = False
    #     # index.append(i)
    #     # j += 1

    if is_gameover:
        for i in range(len(list_word)):
            window.blit(answer_list[i], (answer_x[i], answer_y))
        # answer_x += 35
        # in_list = False
#     answer_text = pygame.font.Font("freesansbold.ttf", 24)
#     if is_display:
#         answer = answer_text.render(alphabets[record], True, black)
#         window.blit(answer, (50, 550))
#     else:
#         pass


def hint():
    global hint_x, hint_y, hint_index
    global show_hint, given
    # i = 0
    text_hint = pygame.font.Font("freesansbold.ttf", 24)
    text = text_hint.render("HINT: ", True, white)
    window.blit(text, (800, 550))
    if not show_hint:
        if event.type == pygame.MOUSEBUTTONDOWN:
            hint_pos = pygame.mouse.get_pos()
            hint_x, hint_y = hint_pos
            # print(hint_pos)

        if (hint_x in range(800, 980)) and (hint_y in range(530, 580)):
            hint_index = random.randint(0, len(list_word)-1)
            if hint_index not in index:
                print("i:" + str(hint_index))
                pass
            else:
                for li in range(len(word)):
                    if li not in index:
                        hint_index = li
            show_hint = True
            given = True

    if event.type == pygame.MOUSEBUTTONUP:
        pass

    # if (hint_x in range(800, 980)) and (hint_y in range(530, 580)):
    #     i = random.randint(0, len(list_word))
    #     if i not in index:
    #         j = i
    #     else:
    #         for li in range(len(word)):
    #             if li not in index:
    #                 j = li
    hint_letter_text = pygame.font.Font("freesansbold.ttf", 24)
    if given:
        hint_letter = hint_letter_text.render(list_word[hint_index], True, white)
        window.blit(hint_letter, (890, 550))


def game_over():
    global is_hanged, is_gameover
    if chances <= 0:
        text_gameover = pygame.font.Font("freesansbold.ttf", 50)
        gameover = text_gameover.render("HANGED!", True, red)
        window.blit(gameover, (620, 285))

        reload = pygame.image.load("reload.png")
        reload = pygame.transform.scale(reload, (30, 30))
        window.blit(reload, (670, 405))

        exit_game = pygame.image.load("sign-out.png")
        exit_game = pygame.transform.scale(exit_game, (30, 30))
        window.blit(exit_game, (800, 405))

        is_hanged = True
        is_gameover = True
    if is_win:
        text_win = pygame.font.Font("freesansbold.ttf", 50)
        winner = text_win.render("SAVED!", True, white)
        window.blit(winner, (620, 285))
        is_gameover = True

        reload = pygame.image.load("reload.png")
        reload = pygame.transform.scale(reload, (30, 30))
        window.blit(reload, (670, 405))

        exit_game = pygame.image.load("sign-out.png")
        exit_game = pygame.transform.scale(exit_game, (30, 30))
        window.blit(exit_game, (800, 405))


# def reveal():


def restart():
    # reload = pygame.image.load("reload.png")
    # reload = pygame.transform.scale(reload, (30, 30))
    # window.blit(reload, (620, 300))
    global is_restart, is_gameover, is_restart_pressed

    reload = (0, 0)
    reload_x, reload_y = reload
    if is_gameover:
        if not is_restart_pressed:
            if event.type == pygame.MOUSEBUTTONDOWN:
                reload = pygame.mouse.get_pos()
                reload_x, reload_y = reload

            if (reload_x in range(660, 710)) and (reload_y in range(395, 455)):
                # is_restart = True
                is_restart_pressed = True
            if (reload_x in range(790, 840)) and (reload_y in range(400, 450)):
                exit()

        if event.type == pygame.MOUSEBUTTONUP:
            # is_restart_pressed = True
            pass

        # if (reload_x in range(660, 710)) and (reload_y in range(395, 455)):
        #     is_restart = True
        #
        # if (reload_x in range(790, 840)) and (reload_y in range(400, 450)):
        #     exit()


while run_game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False

    # window.fill(green)
    window.blit(background, (0, 0))
    letter_box()
    display_letters()
    # drawing the hanging man
    hanging_man.draw_man(chances, is_win)
    hanging_man.support()
    hanging_man.winning(is_win)
    hanging_man.hanged(is_hanged)

    answer_dash()
    user_guess()
    print_answer()
    hint()
    game_over()
    restart()

    if is_restart_pressed:
        list_word.clear()
        answer_list.clear()
        index.clear()
        box_pos_value_x.clear()
        box_pos_value_y.clear()
        list_box_pos_x.clear()
        list_box_pos_y.clear()
        word = ""
        chances = 6
        # change = 0
        is_display = True
        is_selected = False
        is_position = False
        in_list = False
        is_guessed = False
        is_pressed = False
        is_first = True
        show_hint = False
        given = False
        is_win = False
        is_hanged = False
        is_gameover = False
        is_restart = False
        is_restart_pressed = False

    pygame.display.update()
