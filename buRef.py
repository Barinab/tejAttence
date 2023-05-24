import pygame.font

class Button:

	def __init__(self, ai_game, msg):

		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()

		self.width, self.height = 300, 80
		self.buton_color = (0, 255, 0)
		self.text_color = (0, 0, 0)
		self.font = pygame.font.SysFont(None, 50)

		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center

		self._set_msg(msg)


	def _set_msg(self, msg):
		self.img_msg = self.font.render(msg, True, self.text_color,  self.buton_color)
		self.img_msg_rect = self.img_msg.get_rect()
		self.img_msg_rect.center = self.rect.center


	def draw_button(self):
		self.screen.fill(self.buton_color, self.rect)
		self.screen.blit(self.img_msg, self.img_msg_rect)