import pygame, numpy
import data.render_engine.display_manager as display
import data.render_engine.loader as l
import data.render_engine.renderer as r
import data.shaders.static_shader as ss
import data.textures.model_texture as mt
import data.models.textured_model as tm
import data.entities.entity as e

vertices = numpy.array([-0.5, 0.5, 0, -0.5, -0.5, 0, 0.5, -0.5, 0, 0.5, 0.5, 0], dtype = "float32")
indices =  numpy.array([0,1,3,3,1,2], dtype = "int32")
texture_coords = numpy.array([0,1,0,0,1,0,1,1], dtype = "int32")

if __name__ == "__main__":
	gameRunning = True
	clock = pygame.time.Clock()
	display = display.display_manager()
	loader = l.loader()
	shader = ss.static_shader()
	renderer = r.renderer(shader, display.screen)

	model = loader.load_to_vao(vertices, texture_coords, indices)
	texture = mt.model_texture(loader.load_texture("chicken"))
	textured_model = tm.textured_model(model, texture)
	
	entity = e.entity(textured_model, (0, 0, -1), 0, 0, 0, 1)
	
	while gameRunning == True:
		clock.tick(60)
		pygame.display.set_caption("a history of birds " + "fps: " + str(clock.get_fps()))
		
		entity.increase_position(0.002, 0.0, -0.02)
		entity.increase_rotation(0.0, 1.0, 0.0)
		renderer.prepare()
		shader.start()
		renderer.render(entity, shader)
		shader.stop()
		display.update_display()
		for event in pygame.event.get():
			if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
				shader.clean_up()
				loader.clean_up()
				display.close_display()
				gameRunning = False