import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 426

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
GRAY = (50, 50, 50)

# Traffic light settings
LIGHT_SIZE = 10
LIGHT_GAP = 5

# Load the background image
background_image = pygame.image.load(r"C:\Users\Ishit Bhargava\OneDrive\Pictures\Traffic_Lights_4Way.png")

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('4-Way Intersection Traffic Lights')

# Traffic light positions (top-left of each light)
lights_positions = {
    "N": (258, 165),
    "S": (199, 280),
    "E": (295, 262),
    "W": (159, 178),
}

# Traffic light states
states = ["NS_GREEN", "NS_YELLOW", "EW_GREEN", "EW_YELLOW"]
state_durations = [10, 2, 10, 2]  # durations for each state in seconds

current_state = 0
state_start_time = time.time()

def draw_intersection():
    screen.blit(background_image, (0, 0))

def draw_traffic_lights():
    global current_state

    for direction, (x, y) in lights_positions.items():
        if direction in ("N", "S"):
            if states[current_state] == "NS_GREEN":
                light_color = GREEN if direction == "N" else RED
            elif states[current_state] == "NS_YELLOW":
                light_color = YELLOW if direction == "N" else RED
            else:
                light_color = RED
        else:
            if states[current_state] == "EW_GREEN":
                light_color = GREEN if direction == "E" else RED
            elif states[current_state] == "EW_YELLOW":
                light_color = YELLOW if direction == "E" else RED
            else:
                light_color = RED

        # Draw the light
        pygame.draw.circle(screen, light_color, (x, y), LIGHT_SIZE)

def update_state():
    global current_state, state_start_time

    current_time = time.time()
    if current_time - state_start_time >= state_durations[current_state]:
        current_state = (current_state + 1) % len(states)
        state_start_time = current_time

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_intersection()
    draw_traffic_lights()
    update_state()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
