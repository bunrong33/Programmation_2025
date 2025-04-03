import pygame

COLOR_MAPPING = {
    0: (255, 255, 255),  # White
    1: (255, 0, 0),      # Red
    2: (0, 0, 255),      # Blue
    3: (0, 255, 0),      # Green
    4: (0, 0, 0),        # Black (Forbidden)
}
def valid_pairs(grid, used_cells):
    for (i1, j1), (i2, j2) in grid.all_pairs():
        if (i1, j1) not in used_cells and (i2, j2) not in used_cells:
            return True
    return False


def run_visualizer(grid):
    pygame.init()
    WIDTH, GRID_HEIGHT = 600, 500
    INFO_HEIGHT = 100
    HEIGHT = GRID_HEIGHT + INFO_HEIGHT
    ROWS, COLS = grid.n, grid.m
    CELL_SIZE = WIDTH // COLS

    
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("SQUID Game")

   
    score_font = pygame.font.Font(None, 36)
    cell_font = pygame.font.Font(None, 24)

    selected_cells = []
    confirmed_pairs = []
    used_cells = set()
    
    player_turn = 1
    scores = {1: 0, 2: 0}
    winner_txt = None
    running = True
    while running:
        screen.fill((255, 255, 255))
        if not valid_pairs(grid,used_cells):
            if scores[1] < scores[2]:
                winner_txt = "Victory goes to Player 1 "
            elif scores[1] > scores[2]:
                winner_txt = "Victory goes to Player 2 "
            else : 
                winner_txt = "It's tie"
        #Design Grid
        for i in range(ROWS):
            for j in range(COLS):
                color = COLOR_MAPPING.get(grid.color[i][j], (200, 200, 200))
                cell_rect = pygame.Rect(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)

                pygame.draw.rect(screen, color, cell_rect)
                pygame.draw.rect(screen, (0, 0, 0), cell_rect, 1)

                text_color = (255, 255, 255) if grid.color[i][j] == 4 else (0, 0, 0)
                value_str = str(grid.value[i][j])
                text_surface = cell_font.render(value_str, True, text_color)
                text_rect = text_surface.get_rect(center=cell_rect.center)
                screen.blit(text_surface, text_rect)

        # Design pairs 
        for (i1, j1), (i2, j2), p in confirmed_pairs:
            x1, y1 = j1 * CELL_SIZE + CELL_SIZE // 2, i1 * CELL_SIZE + CELL_SIZE // 2
            x2, y2 = j2 * CELL_SIZE + CELL_SIZE // 2, i2 * CELL_SIZE + CELL_SIZE // 2
            color_line = (255, 255, 0) if p == 1 else (0, 0, 255)  # Player1=Yellow, Player 2
            pygame.draw.line(screen, color_line, (x1, y1), (x2, y2), 3)

        # Highlight selected pairs
        for i, j in selected_cells:
            highlight_rect = pygame.Rect(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, (0, 255, 0), highlight_rect, 3)

        # Score zone
        pygame.draw.rect(screen, (230, 230, 230), (0, GRID_HEIGHT, WIDTH, INFO_HEIGHT))
        
        # Score
        score_text = score_font.render(f"Player 1: {scores[1]}   Player 2: {scores[2]}", True, (0, 0, 0)) # color black 
        screen.blit(score_text, (10, GRID_HEIGHT + 20))
        
        turn_text = score_font.render(f"Player {player_turn}'s Turn", True, (0, 0, 255)) # color :blue
        screen.blit(turn_text, (10, GRID_HEIGHT - 50))

        if winner_txt:
            winner_surface = score_font.render(winner_txt,True,(255,0,0))
            screen.blit(winner_surface,(WIDTH//10,GRID_HEIGHT+60))

    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if y >= GRID_HEIGHT: 
                    continue

                j, i = x // CELL_SIZE, y // CELL_SIZE
                # Ignore cells that already used 
                if grid.color[i][j] == 4 or (i, j) in used_cells:
                    continue

                if (i, j) not in selected_cells:
                    selected_cells.append((i, j))

                
                if len(selected_cells) == 2:
                    (i1, j1), (i2, j2) = selected_cells
                    if ((i1, j1), (i2, j2)) in grid.all_pairs() or ((i2, j2), (i1, j1)) in grid.all_pairs():
                        confirmed_pairs.append(((i1, j1), (i2, j2), player_turn))
                        used_cells.add((i1, j1))
                        used_cells.add((i2, j2))
                        difference = abs(grid.value[i1][j1] - grid.value[i2][j2])
                        scores[player_turn] += difference
                        # change player
                        player_turn = 2 if player_turn == 1 else 1
                    selected_cells = []

        pygame.display.flip()

    pygame.quit()
