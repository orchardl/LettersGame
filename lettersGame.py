import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up screen
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Learning Time")

# Set up font
font = pygame.font.Font(None, 1200)

# Dictionary mapping keys to corresponding letters/sounds
key_mapping = {
    pygame.K_a: ('A a', 'A'),
    pygame.K_b: ('B b', 'B'),
    pygame.K_c: ('C c', 'C'),
    pygame.K_d: ('D d', 'D'),
    pygame.K_e: ('E e', 'E'),
    pygame.K_f: ('F f', 'F'),
    pygame.K_g: ('G g', 'G'),
    pygame.K_h: ('H h', 'H'),
    pygame.K_i: ('I i', 'I'),
    pygame.K_j: ('J j', 'J'),
    pygame.K_k: ('K k', 'K'),
    pygame.K_l: ('L l', 'L'),
    pygame.K_m: ('M m', 'M'),
    pygame.K_n: ('N n', 'N'),
    pygame.K_o: ('O o', 'O'),
    pygame.K_p: ('P p', 'P'),
    pygame.K_q: ('Q q', 'Q'),
    pygame.K_r: ('R r', 'R'),
    pygame.K_s: ('S s', 'S'),
    pygame.K_t: ('T t', 'T'),
    pygame.K_u: ('U u', 'U'),
    pygame.K_v: ('V v', 'V'),
    pygame.K_w: ('W w', 'W'),
    pygame.K_x: ('X x', 'X'),
    pygame.K_y: ('Y y', 'Y'),
    pygame.K_z: ('Z z', 'Z'),
    # pygame.K_1: ('1', '1'),
    # Add more mappings as needed
    pygame.K_1: (' ', 'nada'),
    pygame.K_2: (' ', 'nada'),
    pygame.K_3: (' ', 'nada'),
    pygame.K_4: (' ', 'nada'),
    pygame.K_5: (' ', 'nada'),
    pygame.K_6: (' ', 'nada'),
    pygame.K_7: (' ', 'nada'),
    pygame.K_8: (' ', 'nada'),
    pygame.K_9: (' ', 'nada'),
    pygame.K_0: (' ', 'nada'),
}

# Set up sound
pygame.mixer.init()

# Move the mouse to the top right corner
pygame.mouse.set_pos((screen.get_width() - 1, 0))

# Block Windows key events
#pygame.event.set_blocked(pygame.KEYUP)
#pygame.event.set_blocked(pygame.KEYUP, pygame.K_LWIN)
#pygame.event.set_blocked(pygame.KEYUP, pygame.K_RWIN)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            if event.key in key_mapping:
                letter, sound = key_mapping[event.key]

                # Check if audio is currently playing
                if not pygame.mixer.get_busy():
                    # Play the sound
                    pygame.mixer.Sound(f"sounds/{sound}.wav").play()

                    # Display letter on the screen
                    text = font.render(letter, True, (255, 255, 255))
                    text_rect = text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
                    screen.fill((0, 0, 0))  # Clear the screen
                    screen.blit(text, text_rect)
                    pygame.display.flip()

    pygame.time.Clock().tick(30)
