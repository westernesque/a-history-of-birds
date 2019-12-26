import pygame, numpy, random
import data.render_engine.display_manager as display
import data.render_engine.loader as l
import data.render_engine.master_renderer as mr
import data.render_engine.light as li
import data.obj_loader.obj_file_loader as o
import data.render_engine.camera as c
import data.render_engine.third_person_camera as tpc
#import data.shaders.static_shader as ss
import data.tools.font as font
import data.tools.mouse_picker as mp
import data.textures.model_texture as mt
import data.models.textured_model as tm
import data.terrains.terrain as t
import data.textures.terrain_texture as tt
import data.textures.terrain_texture_pack as ttp
import data.entities.entity as e
import data.entities.player as p
import data.guis.gui_texture as gt
import data.guis.gui_renderer as gr

if __name__ == "__main__":
	gameRunning = True
	clock = pygame.time.Clock()
	display = display.DisplayManager()
	# numpy.show_config()
	loader = l.Loader()
	renderer = mr.MasterRenderer(display.screen, loader)
	
	'''
	PERFORMANCE CHECKS... 
	1.) verify that fps of pygame is accurate. 
	2.) see about reducing the amount of time numpy.dot takes? <<-- 
	3.) look into high CPU usage for numpy in general.
	4.) create a new scene_manager & state_manager
	5.) maybe have an object_list to hold the lists? // dictionary duh
	'''
	
	guis = []
	entity_list = []
	waypoint_list = []
	bush_list = []
	texture_atlus_test_list = []
	lights = []
	lamp_list = []
	
	gui_one = gt.gui_texture(loader.load_texture("chicken"), (0.5, 0.5), (0.5, 0.5))
	gui_two = gt.gui_texture(loader.load_texture("chicken"), (0.0, 0.0), (0.25, 0.25))
	guis.append(gui_one)
	guis.append(gui_two)
	gui_renderer = gr.gui_renderer(loader)

	text_vertices = numpy.array([-1, 1, 0, -1, -1, 0, 1, -1, 0, 1, 1, 0], dtype="float32")
	text_indices = numpy.array([0, 1, 3, 3, 1, 2], dtype="float32")
	text_texture_coords = numpy.array([0, 1, 0, 0, 1, 0, 1, 1], dtype="int32")
	
	
	cube = o.obj_file_loader().load_obj("data\\models\\res\\cube.obj")
	cube_model = loader.load_to_vao(cube.get_vertices(), cube.get_texture_coordinates(), cube.get_normals(), cube.get_indices())
	textured_cube = tm.textured_model(cube_model, mt.model_texture(loader.load_texture("large_test")))
	textured_cube.get_texture().set_has_transparency(False)
	
	waypoint_cube = o.obj_file_loader().load_obj("data\\models\\res\\cube.obj")
	waypoint_cube_model = loader.load_to_vao(waypoint_cube.get_vertices(), waypoint_cube.get_texture_coordinates(), waypoint_cube.get_normals(), waypoint_cube.get_indices())
	textured_waypoint_cube = tm.textured_model(waypoint_cube_model, mt.model_texture(loader.load_texture("hmm")))
	textured_waypoint_cube.get_texture().set_has_transparency(False)
	waypoint_list.append(e.entity(textured_waypoint_cube, (0.0, 400.0, 0.0), 0.0, 0.0, 0.0, 100.0))
	
	
	bush = o.obj_file_loader().load_obj("data\\models\\res\\pine.obj")
	bush_model = loader.load_to_vao(bush.get_vertices(), bush.get_texture_coordinates(), bush.get_normals(), bush.get_indices())
	textured_bush = tm.textured_model(bush_model, mt.model_texture(loader.load_texture("tree_texture")))
	
	textured_bush.get_texture().set_has_transparency(False)
	textured_bush.get_texture().set_use_fake_lighting(False)
	textured_bush.get_texture().set_shine_damper(5.0)
	textured_bush.get_texture().set_reflectivity(10.0)
	
	texture_atlas_test = mt.model_texture(loader.load_texture("fern"))
	texture_atlas_test.set_number_of_rows(2)
	fern = o.obj_file_loader().load_obj("data\\models\\res\\fern.obj")
	fern_model = loader.load_to_vao(fern.get_vertices(), fern.get_texture_coordinates(), fern.get_normals(), fern.get_indices())
	texture_atlas_test_fern = tm.textured_model(fern_model, texture_atlas_test)
	texture_atlas_test_fern.get_texture().set_has_transparency(True)
	texture_atlas_test_fern.get_texture().set_use_fake_lighting(False)
	
	player_raw_model = o.obj_file_loader().load_obj("data\\models\\res\\bunny.obj")
	player_model = loader.load_to_vao(player_raw_model.get_vertices(), player_raw_model.get_texture_coordinates(), player_raw_model.get_normals(), player_raw_model.get_indices())
	textured_player_model = tm.textured_model(player_model, mt.model_texture(loader.load_texture("hmm")))
	player = p.player(textured_player_model, (400.0 , 0.0, 400.0), 0.0, 0.0, 0.0, 1.0)
	
	t_background_texture = tt.terrain_texture(loader.load_texture("leaf"))
	t_r_texture = tt.terrain_texture(loader.load_texture("dirt"))
	t_g_texture = tt.terrain_texture(loader.load_texture("hmm"))
	t_b_texture = tt.terrain_texture(loader.load_texture("cobblestone"))
	
	t_terrain_texture_pack = ttp.terrain_texture_pack(t_background_texture, t_r_texture, t_g_texture, t_b_texture)
	
	t_blend_map = tt.terrain_texture(loader.load_texture("blend_map"))
	
	terrain = t.terrain(0.0, 0.0, loader, t_terrain_texture_pack, t_blend_map, "height_map")
	
	lamp = o.obj_file_loader().load_obj("data\\models\\res\\lamp.obj")
	lamp_model = loader.load_to_vao(lamp.get_vertices(), lamp.get_texture_coordinates(), lamp.get_normals(), lamp.get_indices())
	textured_lamp = tm.textured_model(lamp_model, mt.model_texture(loader.load_texture("lamp")))
	textured_lamp.get_texture().set_use_fake_lighting(True)

	text = font.font_texture("windfishers")
	text_model = loader.load_to_vao(text_vertices, text_texture_coords, text_indices)
	text_texture = mt.model_texture(loader.load_pygame_texture(text[0], text[1], text[2]))
	text_textured_model = tm.textured_model(text_model, text_texture)
	text_entity = e.entity(text_textured_model, (0, 0, 0), 0, 0, 0, 0.5)
	
	# for i in range(100):
	# 	x = random.uniform(0.0, 800.0)
	# 	t_x = random.uniform(0.0, 800.0)
	# 	z = random.uniform(0.0, 800.0)
	# 	t_z = random.uniform(0.0, 800.0)
	# 	rand_y = random.uniform(0.0, 100.0)
	# 	y = terrain.get_terrain_height(x, z)
	# 	t_y = terrain.get_terrain_height(t_x, t_z)
	# 	rx = random.uniform(0.0, 180)
	# 	ry = random.uniform(0.0, 180)
	# 	entity_list.append(e.entity(textured_cube, (x, rand_y, z), rx, ry, 0, 1))
	# 	bush_list.append(e.entity(textured_bush, (t_x, t_y, t_z), 0, 0, 0, 1))
	# 	texture_atlus_test_list.append(e.entity(texture_atlas_test_fern, (x, y, z), 0, 0, 0, 1, random.randint(0,3)))
	
	lamp_test_y_1 = terrain.get_terrain_height(400.0, 400.0)
	#print "terrain height for lamp_test_y_1: " + str(lamp_test_y_1)
	lamp_test_y_2 = terrain.get_terrain_height(370.0, 300.0)
	lamp_test_y_3 = terrain.get_terrain_height(293.0, 305.0)
	
	lamp_list.append(e.entity(textured_lamp, (400.0, lamp_test_y_1, 400.0), 0, 0, 0, 1))	
	lamp_list.append(e.entity(textured_lamp, (370.0, lamp_test_y_2, 300.0), 0, 0, 0, 1))	
	lamp_list.append(e.entity(textured_lamp, (293.0, lamp_test_y_3, 305.0), 0, 0, 0, 1))	
	
	light = li.light((0, 1000, -7000), (0.4, 0.4, 0.4))
	lights.append(light)
	lights.append(li.light((400.0, lamp_test_y_1 + 15.0, 400.0), (2.0, 0.0, 0.0), (1.0, 0.01, 0.002)))
	lights.append(li.light((370.0, lamp_test_y_2 + 15.0, 300.0), (0.0, 2.0, 0.0), (1.0, 0.01, 0.002)))
	lights.append(li.light((293.0, lamp_test_y_3 + 15.0, 305.0), (2.0, 2.0, 0.0), (1.0, 0.01, 0.002)))
	
	camera = tpc.third_person_camera(player)
	
	mouse_picker = mp.MousePicker(camera, renderer.get_projection_matrix(), display.screen, terrain)
	
	while gameRunning == True:
		clock.tick(60)
		pygame.display.set_caption("a history of birds " + "fps: " + str(clock.get_fps()))
		player.move(display, terrain)
		camera.move()
		mouse_picker.update()
#		print "mouse picker current ray: " +  str(mouse_picker.get_current_ray())
		#terrain_point = mouse_picker.get_current_terrain_point()
		renderer.process_entity(player)
		renderer.process_terrain(terrain)
		for entity in waypoint_list:
			renderer.process_entity(entity)
		for entity in entity_list:
			entity.increase_rotation(1.0, 1.0, 0.0)
			renderer.process_entity(entity)
		for lamp in lamp_list:
			renderer.process_entity(lamp)
		for bush in bush_list:
			renderer.process_entity(bush)
		for fern in texture_atlus_test_list:
			renderer.process_entity(fern)
		renderer.render(lights, camera, clock)
		gui_renderer.render(guis)
		display.update_display()
		mouse_keys = pygame.mouse.get_pressed()
		keys = pygame.key.get_pressed()
		if mouse_keys[0] == True: 
			#print "terrain_point point: " + str(terrain_point)
			print("mouse current_ray: " + str(mouse_picker.current_ray))
			print("plane intersection test: " + str(mouse_picker.intersect_with_y()))
			print("lamp position: " + str(lamp_list[0].position))
			#print("camera position: " + str(camera.position) + "\n")
			#print("waypoint position" + str(waypoint_list[0].position) + "\n")
			#print "get_point_on_ray: " + str(mouse_picker.start + mouse_picker.scaled_ray)
			#if numpy.all(terrain_point) != None:
			#waypoint_list[0].set_position(mouse_picker.intersect_with_y())
			lamp_list[0].set_position(mouse_picker.intersect_with_y())
			#lights[1].set_position((mouse_picker.intersect_with_y()[0], mouse_picker.intersect_with_y[1] + 15.0, mouse_picker.intersect_with_y[2]))
			lights[1].set_position((mouse_picker.intersect_with_y()))
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
				camera.position = lamp_list[0].position
			if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
				gui_renderer.clean_up()
				renderer.clean_up()
				loader.clean_up()
				display.close_display()
				gameRunning = False