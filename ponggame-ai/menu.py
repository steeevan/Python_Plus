import pygame

def draw_menu(screen, font):
    screen.fill((20, 20, 20))
    options = [
        ("Player vs AI 1", 1),
        ("Player vs AI 2", 2),
        ("AI 1 vs AI 2", 3)
    ]
    buttons = []
    for i, (text, mode_id) in enumerate(options):
        rect = pygame.Rect(250, 150 + i * 100, 300, 60)
        pygame.draw.rect(screen, (50, 50, 200), rect, border_radius=10)
        label = font.render(text, True, (255, 255, 255))
        screen.blit(label, (rect.x + 20, rect.y + 15))
        buttons.append((rect, mode_id))
    return buttons

def menu_loop(screen, font):
    while True:
        buttons = draw_menu(screen, font)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for rect, mode_id in buttons:
                    if rect.collidepoint(mouse_pos):
                        return mode_id
