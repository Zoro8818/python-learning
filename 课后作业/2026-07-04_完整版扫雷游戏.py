import pygame
import random
import sys
import time

# 学习定位：ChatGPT 自动生成的 pygame 扫雷游戏，用于体验完整项目结构。
# 本地修正：将 SysFont 改为 Font(None, size)，避免 Windows 字体扫描兼容问题。


# =========================
# 基础设置
# =========================

pygame.init()

WINDOW_WIDTH = 760
WINDOW_HEIGHT = 680

TOP_HEIGHT = 110

MINE = -1

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Python Minesweeper")

clock = pygame.time.Clock()

font_big = pygame.font.Font(None, 32)
font_mid = pygame.font.Font(None, 24)
font_small = pygame.font.Font(None, 18)


# =========================
# 颜色设置
# =========================

BG_COLOR = (230, 230, 230)
TOP_COLOR = (210, 210, 210)

CELL_HIDDEN = (150, 150, 150)
CELL_REVEALED = (220, 220, 220)
CELL_BORDER = (90, 90, 90)

BUTTON_COLOR = (180, 180, 180)
BUTTON_ACTIVE = (120, 170, 220)
BUTTON_TEXT = (20, 20, 20)

TEXT_COLOR = (20, 20, 20)
RED = (210, 60, 60)
DARK_RED = (120, 0, 0)
GREEN = (40, 150, 80)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (245, 210, 80)

NUMBER_COLORS = [
    BLACK,
    (30, 80, 200),
    (30, 140, 60),
    (200, 50, 50),
    (120, 40, 180),
    (150, 80, 20),
    (20, 150, 150),
    (80, 80, 80),
    BLACK,
]


# =========================
# 扫雷游戏主体
# =========================

class MinesweeperGame:
    def __init__(self):
        # difficulty 的意思是“难度”
        # 格式：名字，行数，列数，雷数，格子大小
        self.difficulties = [
            ("EASY", 9, 9, 10, 40),
            ("NORMAL", 16, 16, 40, 32),
            ("HARD", 16, 22, 99, 28),
        ]

        self.difficulty_index = 0

        self.reset_button = pygame.Rect(310, 60, 140, 36)

        self.difficulty_buttons = [
            pygame.Rect(30, 60, 90, 36),
            pygame.Rect(130, 60, 110, 36),
            pygame.Rect(250, 60, 90, 36),
        ]

        self.set_difficulty(0)

    def set_difficulty(self, index):
        self.difficulty_index = index

        name, rows, cols, mine_count, cell_size = self.difficulties[index]

        self.name = name
        self.rows = rows
        self.cols = cols
        self.mine_count = mine_count
        self.cell_size = cell_size

        self.grid_width = self.cols * self.cell_size
        self.grid_height = self.rows * self.cell_size

        self.grid_x = (WINDOW_WIDTH - self.grid_width) // 2
        self.grid_y = TOP_HEIGHT

        self.board = []
        self.revealed = []
        self.flagged = []

        for row in range(self.rows):
            board_row = []
            revealed_row = []
            flagged_row = []

            for col in range(self.cols):
                board_row.append(0)
                revealed_row.append(False)
                flagged_row.append(False)

            self.board.append(board_row)
            self.revealed.append(revealed_row)
            self.flagged.append(flagged_row)

        self.mines_generated = False

        self.game_over = False
        self.game_won = False

        self.start_time = None
        self.final_time = 0

        # reveal_effects 保存揭开格子的动画
        self.reveal_effects = []

    def restart(self):
        self.set_difficulty(self.difficulty_index)

    def generate_mines(self, first_row, first_col):
        # 第一次点击的位置，以及周围一圈，都尽量不放雷
        safe_cells = []

        for r in range(first_row - 1, first_row + 2):
            for c in range(first_col - 1, first_col + 2):
                if 0 <= r < self.rows and 0 <= c < self.cols:
                    safe_cells.append((r, c))

        all_cells = []

        for r in range(self.rows):
            for c in range(self.cols):
                if (r, c) not in safe_cells:
                    all_cells.append((r, c))

        mine_positions = random.sample(all_cells, self.mine_count)

        for r, c in mine_positions:
            self.board[r][c] = MINE

        self.calculate_numbers()

        self.mines_generated = True

    def calculate_numbers(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c] == MINE:
                    continue

                count = 0

                for nr in range(r - 1, r + 2):
                    for nc in range(c - 1, c + 2):
                        if nr == r and nc == c:
                            continue

                        if 0 <= nr < self.rows and 0 <= nc < self.cols:
                            if self.board[nr][nc] == MINE:
                                count += 1

                self.board[r][c] = count

    def get_cell_from_mouse(self, mouse_pos):
        mouse_x, mouse_y = mouse_pos

        if mouse_x < self.grid_x:
            return None

        if mouse_y < self.grid_y:
            return None

        if mouse_x >= self.grid_x + self.grid_width:
            return None

        if mouse_y >= self.grid_y + self.grid_height:
            return None

        col = (mouse_x - self.grid_x) // self.cell_size
        row = (mouse_y - self.grid_y) // self.cell_size

        return row, col

    def left_click_cell(self, row, col):
        if self.game_over or self.game_won:
            return

        if self.flagged[row][col]:
            return

        if not self.mines_generated:
            self.generate_mines(row, col)
            self.start_time = time.time()

        if self.board[row][col] == MINE:
            self.revealed[row][col] = True
            self.reveal_all_mines()
            self.game_over = True
            self.save_final_time()
            return

        self.reveal_cell(row, col)
        self.check_win()

    def right_click_cell(self, row, col):
        if self.game_over or self.game_won:
            return

        if self.revealed[row][col]:
            return

        self.flagged[row][col] = not self.flagged[row][col]

    def reveal_cell(self, row, col):
        if self.revealed[row][col]:
            return

        if self.flagged[row][col]:
            return

        # 如果这个格子周围有雷，只打开这个格子
        if self.board[row][col] > 0:
            self.revealed[row][col] = True
            self.reveal_effects.append((row, col, time.time()))
            return

        # 如果这个格子周围没有雷，就向外扩散打开
        stack = [(row, col)]

        while len(stack) > 0:
            current_row, current_col = stack.pop()

            if self.revealed[current_row][current_col]:
                continue

            if self.flagged[current_row][current_col]:
                continue

            self.revealed[current_row][current_col] = True
            self.reveal_effects.append((current_row, current_col, time.time()))

            if self.board[current_row][current_col] == 0:
                for nr in range(current_row - 1, current_row + 2):
                    for nc in range(current_col - 1, current_col + 2):
                        if 0 <= nr < self.rows and 0 <= nc < self.cols:
                            if not self.revealed[nr][nc]:
                                if not self.flagged[nr][nc]:
                                    if self.board[nr][nc] != MINE:
                                        stack.append((nr, nc))

    def reveal_all_mines(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c] == MINE:
                    self.revealed[r][c] = True

    def check_win(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c] != MINE:
                    if not self.revealed[r][c]:
                        return

        self.game_won = True
        self.save_final_time()

        # 胜利后自动把所有雷标出来
        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c] == MINE:
                    self.flagged[r][c] = True

    def save_final_time(self):
        if self.start_time is None:
            self.final_time = 0
        else:
            self.final_time = int(time.time() - self.start_time)

    def get_elapsed_time(self):
        if self.game_over or self.game_won:
            return self.final_time

        if self.start_time is None:
            return 0

        return int(time.time() - self.start_time)

    def get_flags_count(self):
        count = 0

        for r in range(self.rows):
            for c in range(self.cols):
                if self.flagged[r][c]:
                    count += 1

        return count

    def draw(self):
        screen.fill(BG_COLOR)

        self.draw_top_panel()
        self.draw_grid()
        self.draw_reveal_effects()

        if self.game_over:
            self.draw_center_message("GAME OVER", RED)

        if self.game_won:
            self.draw_center_message("YOU WIN", GREEN)

    def draw_top_panel(self):
        pygame.draw.rect(screen, TOP_COLOR, (0, 0, WINDOW_WIDTH, TOP_HEIGHT))

        title_text = font_big.render("Minesweeper", True, TEXT_COLOR)
        screen.blit(title_text, (30, 15))

        time_text = font_mid.render("Time: " + str(self.get_elapsed_time()), True, TEXT_COLOR)
        screen.blit(time_text, (520, 18))

        mines_left = self.mine_count - self.get_flags_count()
        mine_text = font_mid.render("Mines: " + str(mines_left), True, TEXT_COLOR)
        screen.blit(mine_text, (520, 55))

        for i in range(len(self.difficulty_buttons)):
            button = self.difficulty_buttons[i]
            name = self.difficulties[i][0]

            if i == self.difficulty_index:
                color = BUTTON_ACTIVE
            else:
                color = BUTTON_COLOR

            pygame.draw.rect(screen, color, button, border_radius=6)
            pygame.draw.rect(screen, CELL_BORDER, button, 2, border_radius=6)

            text = font_small.render(name, True, BUTTON_TEXT)
            text_rect = text.get_rect(center=button.center)
            screen.blit(text, text_rect)

        pygame.draw.rect(screen, BUTTON_COLOR, self.reset_button, border_radius=6)
        pygame.draw.rect(screen, CELL_BORDER, self.reset_button, 2, border_radius=6)

        reset_text = font_small.render("RESTART", True, BUTTON_TEXT)
        reset_rect = reset_text.get_rect(center=self.reset_button.center)
        screen.blit(reset_text, reset_rect)

    def draw_grid(self):
        for r in range(self.rows):
            for c in range(self.cols):
                x = self.grid_x + c * self.cell_size
                y = self.grid_y + r * self.cell_size

                rect = pygame.Rect(x, y, self.cell_size, self.cell_size)

                if self.revealed[r][c]:
                    pygame.draw.rect(screen, CELL_REVEALED, rect)
                else:
                    pygame.draw.rect(screen, CELL_HIDDEN, rect)

                pygame.draw.rect(screen, CELL_BORDER, rect, 1)

                if self.revealed[r][c]:
                    if self.board[r][c] == MINE:
                        self.draw_mine(rect)
                    elif self.board[r][c] > 0:
                        self.draw_number(rect, self.board[r][c])
                else:
                    if self.flagged[r][c]:
                        self.draw_flag(rect)

    def draw_number(self, rect, number):
        color = NUMBER_COLORS[number]

        text = font_mid.render(str(number), True, color)
        text_rect = text.get_rect(center=rect.center)

        screen.blit(text, text_rect)

    def draw_mine(self, rect):
        center_x = rect.centerx
        center_y = rect.centery

        radius = self.cell_size // 4

        pygame.draw.circle(screen, BLACK, (center_x, center_y), radius)
        pygame.draw.circle(screen, DARK_RED, (center_x, center_y), radius // 2)

    def draw_flag(self, rect):
        pole_x = rect.left + self.cell_size // 3
        pole_top = rect.top + self.cell_size // 5
        pole_bottom = rect.bottom - self.cell_size // 5

        pygame.draw.line(screen, BLACK, (pole_x, pole_top), (pole_x, pole_bottom), 3)

        flag_points = [
            (pole_x, pole_top),
            (pole_x + self.cell_size // 2, pole_top + self.cell_size // 6),
            (pole_x, pole_top + self.cell_size // 3),
        ]

        pygame.draw.polygon(screen, RED, flag_points)

    def draw_reveal_effects(self):
        now = time.time()
        still_alive_effects = []

        for row, col, start_time in self.reveal_effects:
            age = now - start_time

            if age < 0.25:
                progress = age / 0.25

                x = self.grid_x + col * self.cell_size
                y = self.grid_y + row * self.cell_size

                pad = int(progress * self.cell_size / 3)

                effect_rect = pygame.Rect(
                    x + pad,
                    y + pad,
                    self.cell_size - pad * 2,
                    self.cell_size - pad * 2
                )

                pygame.draw.rect(screen, YELLOW, effect_rect, 3)

                still_alive_effects.append((row, col, start_time))

        self.reveal_effects = still_alive_effects

    def draw_center_message(self, message, color):
        panel_width = 300
        panel_height = 110

        panel_x = (WINDOW_WIDTH - panel_width) // 2
        panel_y = TOP_HEIGHT + (self.grid_height - panel_height) // 2

        panel = pygame.Surface((panel_width, panel_height))
        panel.set_alpha(230)
        panel.fill(WHITE)

        screen.blit(panel, (panel_x, panel_y))

        pygame.draw.rect(
            screen,
            color,
            (panel_x, panel_y, panel_width, panel_height),
            4,
            border_radius=8
        )

        text = font_big.render(message, True, color)
        text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, panel_y + 38))
        screen.blit(text, text_rect)

        sub_text = font_small.render("Click RESTART to play again", True, TEXT_COLOR)
        sub_rect = sub_text.get_rect(center=(WINDOW_WIDTH // 2, panel_y + 78))
        screen.blit(sub_text, sub_rect)

    def handle_mouse_down(self, event):
        mouse_pos = event.pos

        for i in range(len(self.difficulty_buttons)):
            if self.difficulty_buttons[i].collidepoint(mouse_pos):
                self.set_difficulty(i)
                return

        if self.reset_button.collidepoint(mouse_pos):
            self.restart()
            return

        cell = self.get_cell_from_mouse(mouse_pos)

        if cell is None:
            return

        row, col = cell

        if event.button == 1:
            self.left_click_cell(row, col)

        elif event.button == 3:
            self.right_click_cell(row, col)


# =========================
# 主循环
# =========================

game = MinesweeperGame()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            game.handle_mouse_down(event)

    game.draw()

    pygame.display.flip()
    clock.tick(60)
