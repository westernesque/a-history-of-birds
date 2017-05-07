import pygame
import data.display_manager as display

if __name__ == "__main__":
	gameRunning = True
	clock = pygame.time.Clock()
	display = display.display_manager()
	while gameRunning == True:
		clock.tick(60)
		pygame.display.set_caption("nano, md " + "fps: " + str(clock.get_fps()))
		for event in pygame.event.get():
			if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
				display.close_display()
				gameRunning = False