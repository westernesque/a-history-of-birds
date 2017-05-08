import pygame, numpy
import data.render_engine.display_manager as display
import data.render_engine.loader as l
import data.render_engine.renderer as r
import data.obj_loader.obj_file_loader as o
import data.render_engine.camera as c
import data.shaders.static_shader as ss
import data.textures.model_texture as mt
import data.models.textured_model as tm
import data.entities.entity as e

# vertices = numpy.array([-0.5, 0.5, 0, -0.5, -0.5, 0, 0.5, -0.5, 0, 0.5, 0.5, 0], dtype = "float32")
# indices =  numpy.array([0,1,3,3,1,2], dtype = "int32")
# texture_coords = numpy.array([0,1,0,0,1,0,1,1], dtype = "int32")

vertices = numpy.array([-0.5, -0.5, -0.5, -0.5, 0.5, -0.5, 0.5, 0.5 , -0.5, 0.5, -0.5, -0.5, -0.5, 0.5, 0.5,  -0.5, -0.5, 0.5, 0.5, -0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, -0.5, 0.5, -0.5, -0.5, 0.5, -0.5, 0.5, 0.5, 0.5, 0.5, -0.5, 0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, 0.5, -0.5, 0.5, 0.5, -0.5, 0.5, 0.5, -0.5, 0.5, -0.5, 0.5, 0.5, -0.5, 0.5, 0.5, 0.5, -0.5, -0.5, 0.5, -0.5, -0.5, -0.5, 0.5, -0.5, -0.5, 0.5, -0.5, 0.5], dtype = "float32")
texture_coords = numpy.array([0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1], dtype = "float32")
indices = numpy.array([0, 1, 3, 3, 1, 2, 4, 5, 7, 7, 5, 6, 8, 9, 11, 11, 9, 10, 12, 13, 15, 15, 13, 14, 16, 17, 19, 19, 17, 18, 20, 21, 23, 23, 21, 22], dtype = "int32")


if __name__ == "__main__":
	gameRunning = True
	clock = pygame.time.Clock()
	display = display.display_manager()
	loader = l.loader()
	shader = ss.static_shader()
	renderer = r.renderer(shader, display.screen)
	
	data = o.obj_file_loader().load_obj("data\\textures\\res\\stall.obj")
	test = loader.load_to_vao(data.get_vertices(), data.get_texture_coordinates(), data.get_indices())
	test_texture = mt.model_texture(loader.load_texture("stall_texture"))
	textured_test = tm.textured_model(test, test_texture)
	test_entity = e.entity(textured_test, (0, 0, -10), 0, 0, 0, 1)
	
	model = loader.load_to_vao(vertices, texture_coords, indices)
	texture = mt.model_texture(loader.load_texture("balloons"))
	textured_model = tm.textured_model(model, texture)
	
	entity = e.entity(textured_model, (0, 0, -5), 0, 0, 0, 1)
	camera = c.camera()
	
	while gameRunning == True:
		clock.tick(60)
		pygame.display.set_caption("a history of birds " + "fps: " + str(clock.get_fps()))
		
		entity.increase_position(0.002, 0.0, -0.002)
		entity.increase_rotation(1.0, 1.0, 0.0)
		test_entity.increase_rotation(0.0, 1.0, 0.0)
		camera.move()
		renderer.prepare()
		shader.start()
		shader.load_view_matrix(camera)
		renderer.render(entity, shader)
		renderer.render(test_entity, shader)
		shader.stop()
		display.update_display()
		for event in pygame.event.get():
			if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
				shader.clean_up()
				loader.clean_up()
				display.close_display()
				gameRunning = False