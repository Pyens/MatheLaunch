import pygame
import random
import sys
import time

# Settings
WIDTH, HEIGHT = 800, 600
ROWS, COLS = 3, 3
PIECE_WIDTH = WIDTH // COLS
PIECE_HEIGHT = HEIGHT // ROWS
TIME_LIMIT = 60  # seconds
SNAP_TOLERANCE = 30  # pixels

# Initialize
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jigsaw Puzzle with Timer, Snapping, and Win Check")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 48)

# Load and slice image
image = pygame.image.load("licensed-image.jpg")
image = pygame.transform.scale(image, (WIDTH, HEIGHT))

# Create original pieces
original_positions = []
pieces = []

for row in range(ROWS):
    for col in range(COLS):
        x, y = col * PIECE_WIDTH, row * PIECE_HEIGHT
        rect = pygame.Rect(x, y, PIECE_WIDTH, PIECE_HEIGHT)
        piece = image.subsurface(rect).copy()
        pieces.append([piece, (x, y)])
        original_positions.append((x, y))

# Scramble pieces
def scramble_pieces(pieces):
    scrambled = pieces[:]
    random.shuffle(scrambled)
    for i, pos in enumerate(original_positions):
        scrambled[i][1] = (
            pos[0] + random.randint(-100, 100),
            pos[1] + random.randint(-100, 100),
        )
    return scrambled

pieces = scramble_pieces(pieces)
start_time = time.time()
dragging = None
offset = (0, 0)

# Game loop
running = True
won = False

while running:
    screen.fill((255, 255, 255))
    elapsed_time = int(time.time() - start_time)
    remaining_time = max(0, TIME_LIMIT - elapsed_time)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and not won:
            for i, (piece, pos) in enumerate(pieces):
                rect = pygame.Rect(pos, (PIECE_WIDTH, PIECE_HEIGHT))
                if rect.collidepoint(event.pos):
                    dragging = i
                    offset = (event.pos[0] - pos[0], event.pos[1] - pos[1])
                    break

        elif event.type == pygame.MOUSEBUTTONUP and dragging is not None:
            # Snap to original position if close enough
            current_piece = pieces[dragging]
            for i, target_pos in enumerate(original_positions):
                dx = current_piece[1][0] - target_pos[0]
                dy = current_piece[1][1] - target_pos[1]
                if abs(dx) < SNAP_TOLERANCE and abs(dy) < SNAP_TOLERANCE:
                    pieces[dragging][1] = target_pos
                    break
            dragging = None

        elif event.type == pygame.MOUSEMOTION and dragging is not None:
            x, y = event.pos
            pieces[dragging][1] = (x - offset[0], y - offset[1])

    # Draw pieces
    for piece, pos in pieces:
        screen.blit(piece, pos)

    # Draw timer
    timer_text = font.render(f"Time Left: {remaining_time}", True, (0, 0, 0))
    screen.blit(timer_text, (10, 10))

    # Check win condition
    win = all(pos == original_positions[i] for i, (piece, pos) in enumerate(pieces))
    if win and not won:
        won = True
        win_time = int(time.time() - start_time)

    if won:
        win_msg = font.render(f"You Win! Time: {win_time}s", True, (0, 128, 0))
        screen.blit(win_msg, (WIDTH // 2 - 150, HEIGHT // 2))

    # Time's up
    if remaining_time <= 0 and not won:
        lose_msg = font.render("Time's Up! Better Luck Next Time!", True, (200, 0, 0))
        screen.blit(lose_msg, (WIDTH // 2 - 180, HEIGHT // 2))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
