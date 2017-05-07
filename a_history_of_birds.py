import pygame, numpy
import data.render_engine.display_manager as display
import data.render_engine.loader as l
import data.render_engine.renderer as r

vertices = numpy.array([-0.5, 0.5, 0, -0.5, -0.5, 0, 0.5, -0.5, 0, 0.5, 0.5, 0], dtype = "float32")
indices =  numpy.array([0,1,3,3,1,2], dtype = "int32")

if __name__ == "__main__":
	gameRunning = True
	clock = pygame.time.Clock()
	display = display.display_manager()
	loader = l.loader()
	renderer = r.renderer()
	
	model = loader.load_to_vao(vertices, indices)
	
	while gameRunning == True:
		clock.tick(60)
		pygame.display.set_caption("a history of birds " + "fps: " + str(clock.get_fps()))
		renderer.prepare()
		renderer.render(model)
		display.update_display()
		for event in pygame.event.get():
			if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
				loader.clean_up()
				display.close_display()
				gameRunning = False