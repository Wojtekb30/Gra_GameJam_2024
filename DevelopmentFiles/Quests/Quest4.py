def quest4(tip: int):
    import pygame
    import sys
    import math
    import random
    from tkinter import messagebox  # Import tkinter if using messagebox

    # Declare global variables to manage state
    global angle, spinning, spin_speed

    # Initialize global variables
    angle = 0
    spin_speed = 0
    spinning = False

    def ShowTips():
        line = ""
        all_tips = []
        with open("messages.txt", "r") as f:
            line = f.readline().strip()
            while line != "":
                all_tips.append(line)
                line = f.readline().strip()
        messagebox.showinfo("Brawo!", f"Twoja wskazówka: {all_tips[tip]}")

    # Initialize Pygame
    pygame.init()

    # Window settings
    WIDTH, HEIGHT = 800, 600
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Spróbuj swoich szans")

    # Color definitions
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (220, 20, 60)
    GREEN = (34, 139, 34)
    BLUE = (30, 144, 255)
    YELLOW = (255, 215, 0)
    ORANGE = (255, 165, 0)
    PURPLE = (128, 0, 128)

    COLORS = [RED, BLACK, GREEN, BLUE, YELLOW, ORANGE, PURPLE]
    CENTER = (WIDTH // 2, HEIGHT // 2)
    RADIUS = 250
    NUM_SECTORS = 12
    ANGLE_PER_SECTOR = 360 / NUM_SECTORS

    WINNING_SECTORS = [2, 5, 8, 11]  # Indices of winning sectors (1/3 probability)
    clock = pygame.time.Clock()

    def draw_wheel(surface, center, radius, sectors, angle):
        start_angle = math.radians(angle)
        font = pygame.font.SysFont(None, 24)
        for i in range(sectors):
            end_angle = start_angle + math.radians(ANGLE_PER_SECTOR)
            color = COLORS[i % len(COLORS)]
            pygame.draw.polygon(
                surface,
                color,
                [
                    center,
                    (
                        center[0] + radius * math.cos(start_angle),
                        center[1] + radius * math.sin(start_angle)
                    ),
                    (
                        center[0] + radius * math.cos(end_angle),
                        center[1] + radius * math.sin(end_angle)
                    )
                ]
            )
            pygame.draw.line(surface, BLACK, center,
                             (
                                 center[0] + radius * math.cos(start_angle),
                                 center[1] + radius * math.sin(start_angle)
                             ), 2)
            mid_angle = (start_angle + end_angle) / 2
            text_radius = radius * 0.7
            text_x = center[0] + text_radius * math.cos(mid_angle)
            text_y = center[1] + text_radius * math.sin(mid_angle)
            text_on_area = "Wygrana" if i in WINNING_SECTORS else "Przegrana"
            text = font.render(text_on_area, True, WHITE)
            text_rect = text.get_rect(center=(text_x, text_y))
            surface.blit(text, text_rect)

            start_angle = end_angle

    def rotate_wheel():
        global angle, spin_speed, spinning
        if spinning:
            angle += spin_speed
            spin_speed *= 0.99
            if spin_speed < 0.1:
                spinning = False
                spin_speed = 0
                determine_result()

    def draw_spin_button(surface):
        button_rect = pygame.Rect(WIDTH // 2 - 50, HEIGHT - 100, 100, 50)
        pygame.draw.rect(surface, GREEN, button_rect)
        font = pygame.font.SysFont(None, 36)
        text = font.render("Spin", True, WHITE)
        text_rect = text.get_rect(center=button_rect.center)
        surface.blit(text, text_rect)
        return button_rect

    def handle_spin_click(pos, button_rect):
        global spinning, spin_speed
        if button_rect.collidepoint(pos) and not spinning:
            spinning = True
            spin_speed = random.uniform(10, 20)

    def determine_result():
        global angle
        normalized_angle = angle % 360
        sector = int((360 - normalized_angle + ANGLE_PER_SECTOR / 2) % 360 // ANGLE_PER_SECTOR)
        result = "Wygrana" if sector in WINNING_SECTORS else "Przegrana"
        show_result(result)

    def show_result(result):
        font = pygame.font.SysFont(None, 48)
        text = font.render(f"Wynik: {result}", True, BLACK)
        text_rect = text.get_rect(center=(WIDTH // 2, 50))
        WINDOW.blit(text, text_rect)
        pygame.display.update()
        pygame.time.delay(1000)
        correct = 1 if result == "Wygrana" else 0
        if correct:
            ShowTips()
        try:
            with open("AnswerCorrect.txt", "w", encoding="utf-8") as file:
                file.write(str(correct))
        except IOError as e:
            print(f"Nie można zapisać pliku: {e}")
        pygame.time.delay(1000)
        pygame.quit()
        sys.exit()

    def main():
        global angle, spinning, spin_speed
        while True:
            WINDOW.fill(WHITE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    spin_button_rect = draw_spin_button(WINDOW)
                    handle_spin_click(pos, spin_button_rect)

            draw_wheel(WINDOW, CENTER, RADIUS, NUM_SECTORS, angle)
            spin_button_rect = draw_spin_button(WINDOW)
            rotate_wheel()
            pygame.display.flip()
            clock.tick(60)

    main()

#quest4(1)
