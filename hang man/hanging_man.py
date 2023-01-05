import pygame

pygame.init()

# color
black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)
skin = (141, 85, 36)
steel = (202, 204, 206)

# positions
face_center_x, face_center_y = (500, 300)
# body
body_x, body_y = (500, 328)
end_x, end_y = (500, 390)
# legs
leg_x, leg_y = (500, 390)
end_rx, end_ry = (525, 460)
end_lx, end_ly = (475, 460)
# hands
hand_x, hand_y = (500, 340)
end_leftx, end_lefty = (470, 410)
end_rightx, end_righty = (530, 410)

screen = pygame.display.set_mode((1000, 700))
# chances = 6
change = 0

run_time = True


def draw_man(chances, is_win):
    # head
    if not is_win:
        if chances < 6:
            pygame.draw.circle(screen, white, (face_center_x, face_center_y), 28, width=2)
        # body
        if chances < 5:
            pygame.draw.line(screen, white, (500, 328), (500, 390), width=2)
        # legs
        if chances < 4:
            pygame.draw.line(screen, white, (500, 390), (475, 460), width=2)
        if chances < 3:
            pygame.draw.line(screen, white, (500, 390), (525, 460), width=2)
            # eyes
            pygame.draw.line(screen, white, (483, 290), (493, 290), width=2)
            pygame.draw.line(screen, white, (507, 290), (517, 290), width=2)
        # hands
        if chances < 2:
            pygame.draw.line(screen, white, (500, 340), (470, 410), width=2)
        if chances < 1:
            pygame.draw.line(screen, white, (500, 340), (530, 410), width=2)
            # eyes
            # pygame.draw.line(screen, black, (483, 290), (493, 290), width=2)
            # pygame.draw.line(screen, black, (507, 290), (517, 290), width=2)
            # mouth
            pygame.draw.line(screen, white, (488, 312), (512, 312), width=2)


def hanged(is_hanged):
    # global face_center_x, face_center_y, body_x, body_y, end_x, end_y, leg_x, leg_y, end_rx, end_ry
    # global end_lx, end_ly, hand_x, hand_y, end_leftx, end_lefty, end_rightx, end_righty
    global change
    if is_hanged:
        if change > -700:
            change -= 5
        pygame.draw.circle(screen, white, (face_center_x, face_center_y+change), 28, width=5)
        # body

        pygame.draw.line(screen, white, (body_x, body_y+change), (end_x, end_y+change), width=5)
        # legs

        pygame.draw.line(screen, white, (leg_x, leg_y+change), (end_lx, end_ly+change), width=5)
        pygame.draw.line(screen, white, (leg_x, leg_y+change), (end_rx, end_ry+change), width=5)
        # eyes
        # pygame.draw.line(screen, white, (483, 290), (493, 290), width=1)
        # pygame.draw.line(screen, white, (507, 290), (517, 290), width=1)
        # hands
        pygame.draw.line(screen, white, (hand_x, hand_y+change), (end_leftx, end_lefty+change), width=5)
        pygame.draw.line(screen, white, (hand_x, hand_y+change), (end_rightx, end_righty+change), width=5)
        # eyes
        # pygame.draw.line(screen, black, (483, 290), (493, 290), width=2)
        # pygame.draw.line(screen, black, (507, 290), (517, 290), width=2)
        # mouth
        # pygame.draw.line(screen, white, (488, 312), (512, 312), width=2)
    else:
        change = 0


def winning(is_win):
    if is_win:
        # face
        pygame.draw.circle(screen, white, (520, 320), 28, width=2)
        # body
        pygame.draw.line(screen, white, (520, 348), (520, 410), width=2)
        # legs
        pygame.draw.line(screen, white, (520, 410), (495, 480), width=2)
        pygame.draw.line(screen, white, (520, 410), (545, 480), width=2)
        # hands
        pygame.draw.line(screen, white, (520, 360), (470, 320), width=2)
        pygame.draw.line(screen, white, (520, 360), (570, 320), width=2)
        # eyes
        pygame.draw.circle(screen, white, (510, 312), 7, width=2)
        pygame.draw.circle(screen, white, (530, 312), 7, width=2)
        pygame.draw.circle(screen, white, (510, 313), 4)
        pygame.draw.circle(screen, white, (530, 313), 4)
        # pygame.draw.line(screen, black, (503, 310), (513, 310), width=2)
        # pygame.draw.line(screen, black, (527, 310), (537, 310), width=2)
        # mouth
        # pygame.draw.line(screen, black, (508, 332), (532, 332), width=2)
        pygame.draw.arc(screen, white, rect=(510, 330, 20, 10), start_angle=3.14, stop_angle=0, width=2)


def support():
    # pole
    pygame.draw.line(screen, steel, (400, 260), (400, 480), width=5)
    pygame.draw.line(screen, steel, (400, 261), (500, 261), width=5)
    # rope
    pygame.draw.line(screen, steel, (499, 260), (499, 272), width=5)
    # base
    pygame.draw.line(screen, steel, (380, 480), (600, 480), width=5)


# while run_time:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run_time = False
#     screen.fill(red)
#     draw_man(0)
#     support()
#     # chances -= 1
#     winning(True)
#
#     if event.type == pygame.MOUSEBUTTONDOWN:
#         get_pos = pygame.mouse.get_pos()
#         print(get_pos)
#     pygame.display.update()
