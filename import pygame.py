import pygame
import arabic_reshaper
from bidi.algorithm import get_display
pygame.display.init()
pygame.font.init()

win = pygame.display.set_mode((100, 100))
font = pygame.font.Font('bZb.ttf', 10)
text_to_be_reshaped = 'اللغة العربية رائعة'
reshaped_text = arabic_reshaper.reshape(text_to_be_reshaped)
bidi_text = get_display(reshaped_text)
print(reshaped_text)
text = font.render(bidi_text, True, (255, 255, 255))



win.fill((0, 0, 0))
win.blit(text, (0, 0))
pygame.display.update()

for i in range(5):
    pygame.event.clear()
    pygame.time.delay(1000)

pygame.quit()