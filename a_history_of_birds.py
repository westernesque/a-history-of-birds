import pygame, numpy, random
import data.render_engine.display_manager as display
import data.render_engine.loader as l
import data.render_engine.master_renderer as mr
import data.render_engine.light as li
import data.obj_loader.obj_file_loader as o
import data.render_engine.camera as c
import data.shaders.static_shader as ss
import data.textures.model_texture as mt
import data.models.textured_model as tm
import data.terrains.terrain as t
import data.entities.entity as e

# vertices = numpy.array([-0.5, 0.5, 0, -0.5, -0.5, 0, 0.5, -0.5, 0, 0.5, 0.5, 0], dtype = "float32")
# indices =  numpy.array([0,1,3,3,1,2], dtype = "int32")
# texture_coords = numpy.array([0,1,0,0,1,0,1,1], dtype = "int32")

# vertices = numpy.array([-0.5, -0.5, -0.5, -0.5, 0.5, -0.5, 0.5, 0.5 , -0.5, 0.5, -0.5, -0.5, -0.5, 0.5, 0.5,  -0.5, -0.5, 0.5, 0.5, -0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, -0.5, 0.5, -0.5, -0.5, 0.5, -0.5, 0.5, 0.5, 0.5, 0.5, -0.5, 0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, 0.5, -0.5, 0.5, 0.5, -0.5, 0.5, 0.5, -0.5, 0.5, -0.5, 0.5, 0.5, -0.5, 0.5, 0.5, 0.5, -0.5, -0.5, 0.5, -0.5, -0.5, -0.5, 0.5, -0.5, -0.5, 0.5, -0.5, 0.5], dtype = "float32")
# texture_coords = numpy.array([0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1], dtype = "float32")
# indices = numpy.array([0, 1, 3, 3, 1, 2, 4, 5, 7, 7, 5, 6, 8, 9, 11, 11, 9, 10, 12, 13, 15, 15, 13, 14, 16, 17, 19, 19, 17, 18, 20, 21, 23, 23, 21, 22], dtype = "int32")
# normals = numpy.array([0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, -1.0, 0.0, 0.0, 0.0, -1.0, 0.0, 0.0, 0.0, -1.0], dtype = "float32")

if __name__ == "__main__":
	gameRunning = True
	clock = pygame.time.Clock()
	display = display.display_manager()
	loader = l.loader()
	renderer = mr.master_renderer(display.screen)
	
	cube = o.obj_file_loader().load_obj("data\\models\\res\\cube.obj")
	cube_model = loader.load_to_vao(cube.get_vertices(), cube.get_texture_coordinates(), cube.get_normals(), cube.get_indices())
	textured_cube = tm.textured_model(cube_model, mt.model_texture(loader.load_texture("balloons")))

	bush = o.obj_file_loader().load_obj("data\\models\\res\\grass_model.obj")
	bush_model = loader.load_to_vao(bush.get_vertices(), bush.get_texture_coordinates(), bush.get_normals(), bush.get_indices())
	textured_bush = tm.textured_model(bush_model, mt.model_texture(loader.load_texture("grass_texture")))
	textured_bush.get_texture().set_has_transparency(True)
	textured_bush.get_texture().set_use_fake_lighting(True)
	
	entity_list = []
	bush_list = []
	for i in range(200):
		x = random.uniform(-50.0, 50.0)
		y = random.uniform(1.5, 50.0)
		z = random.uniform(-50.0, 50.0)
		rx = random.uniform(0.0, 180)
		ry = random.uniform(0.0, 180)
		entity_list.append(e.entity(textured_cube, (x, y, z), rx, ry, 0, 1))
		bush_list.append(e.entity(textured_bush, (x, 0, z), 0, ry, 0, 1))
	
	terrain = t.terrain(-0.5, -0.5, loader, loader.load_texture("leaf"))
	
	light = li.light((3000, 2000, 2000), (1.0, 1.0, 1.0))
	camera = c.camera()
	
	while gameRunning == True:
		clock.tick(60)
		pygame.display.set_caption("a history of birds " + "fps: " + str(clock.get_fps()))
		
		# entity.increase_position(0.002, 0.0, -0.002)

		camera.move()
		renderer.process_terrain(terrain)
		for entity in entity_list:
			entity.increase_rotation(1.0, 1.0, 0.0)
			renderer.process_entity(entity)
		for bush in bush_list:
			renderer.process_entity(bush)
		renderer.render(light, camera)
		display.update_display()
		for event in pygame.event.get():
			if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
				renderer.clean_up()
				loader.clean_up()
				display.close_display()
				gameRunning = False