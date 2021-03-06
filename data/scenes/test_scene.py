import pygame, numpy, random
import data.tools.scene_manager as sm
import data.textures.model_texture as mt
import data.models.textured_model as tm
import data.terrains.terrain as t
import data.textures.terrain_texture as tt
import data.textures.terrain_texture_pack as ttp
import data.entities.entity as e
import data.entities.player as p
import data.guis.gui_texture as gt
import data.guis.gui_renderer as gr
import data.render_engine.display_manager as display
import data.render_engine.loader as l
import data.render_engine.master_renderer as mr
import data.render_engine.light as li
import data.obj_loader.obj_file_loader as o
import data.render_engine.camera as c
import data.render_engine.third_person_camera as tpc

def test_scene(screen, obj_list):	
	guis = []
	gui_one = gt.GuiTexture(loader.load_texture("chicken"), (0.5, 0.5), (0.5, 0.5))
	gui_two = gt.GuiTexture(loader.load_texture("chicken"), (0.0, 0.0), (0.25, 0.25))
	guis.append(gui_one)
	guis.append(gui_two)
	gui_renderer = gr.GuiRenderer(loader)
	
	
	cube = o.obj_file_loader().load_obj("data\\models\\res\\cube.obj")
	cube_model = loader.load_to_vao(cube.get_vertices(), cube.get_texture_coordinates(), cube.get_normals(), cube.get_indices())
	textured_cube = tm.textured_model(cube_model, mt.model_texture(loader.load_texture("large_test")))
	textured_cube.get_texture().set_has_transparency(False)
	
	bush = o.obj_file_loader().load_obj("data\\models\\res\\pine.obj")
	bush_model = loader.load_to_vao(bush.get_vertices(), bush.get_texture_coordinates(), bush.get_normals(), bush.get_indices())
	textured_bush = tm.textured_model(bush_model, mt.model_texture(loader.load_texture("tree_texture")))
	
	textured_bush.get_texture().set_has_transparency(False)
	textured_bush.get_texture().set_use_fake_lighting(False)
	# textured_bush.get_texture().set_shine_damper(0.5)
	# textured_bush.get_texture().set_reflectivity(10.0)
	
	texture_atlas_test = mt.model_texture(loader.load_texture("fern"))
	texture_atlas_test.set_number_of_rows(2)
	fern = o.obj_file_loader().load_obj("data\\models\\res\\fern.obj")
	fern_model = loader.load_to_vao(fern.get_vertices(), fern.get_texture_coordinates(), fern.get_normals(), fern.get_indices())
	# texture_atlas_test_fern = tm.textured_model(fern_model, mt.model_texture(loader.load_texture("fern")))
	texture_atlas_test_fern = tm.textured_model(fern_model, texture_atlas_test)
	texture_atlas_test_fern.get_texture().set_has_transparency(True)
	texture_atlas_test_fern.get_texture().set_use_fake_lighting(False)
	# texture_atlas_test_fern.get_texture().set_shine_damper(0.1)
	# texture_atlas_test_fern.get_texture().set_reflectivity(100.0)
	
	player_raw_model = o.obj_file_loader().load_obj("data\\models\\res\\bunny.obj")
	player_model = loader.load_to_vao(player_raw_model.get_vertices(), player_raw_model.get_texture_coordinates(), player_raw_model.get_normals(), player_raw_model.get_indices())
	textured_player_model = tm.textured_model(player_model, mt.model_texture(loader.load_texture("hmm")))
	# textured_player_model.get_texture().set_shine_damper(0.5)
	# textured_player_model.get_texture().set_reflectivity(10.5)
	player = p.player(textured_player_model, (400.0 , 0.0, 400.0), 0.0, 0.0, 0.0, 1.0)
	
	t_background_texture = tt.terrain_texture(loader.load_texture("leaf"))
	t_r_texture = tt.terrain_texture(loader.load_texture("dirt"))
	t_g_texture = tt.terrain_texture(loader.load_texture("hmm"))
	t_b_texture = tt.terrain_texture(loader.load_texture("cobblestone"))
	
	t_terrain_texture_pack = ttp.terrain_texture_pack(t_background_texture, t_r_texture, t_g_texture, t_b_texture)
	
	t_blend_map = tt.terrain_texture(loader.load_texture("blend_map"))
	
	terrain = t.terrain(0.0, 0.0, loader, t_terrain_texture_pack, t_blend_map, "height_map")
	
	entity_list = []
	bush_list = []
	texture_atlus_test_list = []
	
	lamp = o.obj_file_loader().load_obj("data\\models\\res\\lamp.obj")
	lamp_model = loader.load_to_vao(lamp.get_vertices(), lamp.get_texture_coordinates(), lamp.get_normals(), lamp.get_indices())
	textured_lamp = tm.textured_model(lamp_model, mt.model_texture(loader.load_texture("lamp")))
	textured_lamp.get_texture().set_use_fake_lighting(True)
	
	for i in range(100):
		x = random.uniform(0.0, 800.0)
		t_x = random.uniform(0.0, 800.0)
		z = random.uniform(0.0, 800.0)
		t_z = random.uniform(0.0, 800.0)
		rand_y = random.uniform(0.0, 100.0) 
		y = terrain.get_terrain_height(x, z)
		t_y = terrain.get_terrain_height(t_x, t_z)
		rx = random.uniform(0.0, 180)
		ry = random.uniform(0.0, 180)
		entity_list.append(e.entity(textured_cube, (x, rand_y, z), rx, ry, 0, 1))
		bush_list.append(e.entity(textured_bush, (t_x, t_y, t_z), 0, 0, 0, 1))
		texture_atlus_test_list.append(e.entity(texture_atlas_test_fern, (x, y, z), 0, 0, 0, 1, random.randint(0,3)))
	
	lamp_test_y_1 = terrain.get_terrain_height(400.0, 400.0)
	lamp_test_y_2 = terrain.get_terrain_height(370.0, 300.0)
	lamp_test_y_3 = terrain.get_terrain_height(293.0, 305.0)
	
	entity_list.append(e.entity(textured_lamp, (400.0, lamp_test_y_1, 400.0), 0, 0, 0, 1))	
	entity_list.append(e.entity(textured_lamp, (370.0, lamp_test_y_2, 300.0), 0, 0, 0, 1))	
	entity_list.append(e.entity(textured_lamp, (293.0, lamp_test_y_3, 305.0), 0, 0, 0, 1))	
	
	lights = []
	light = li.light((0, 1000, -7000), (0.4, 0.4, 0.4))
	lights.append(light)
	lights.append(li.light((400.0, lamp_test_y_1 + 15.0, 400.0), (2.0, 0.0, 0.0), (1.0, 0.01, 0.002)))
	lights.append(li.light((370.0, lamp_test_y_2 + 15.0, 300.0), (0.0, 2.0, 0.0), (1.0, 0.01, 0.002)))
	lights.append(li.light((293.0, lamp_test_y_3 + 15.0, 305.0), (2.0, 2.0, 0.0), (1.0, 0.01, 0.002)))
	# lights.append(li.light((-200.0, 10.0, -200.0), (10.0, 0.0, 0.0)))
	# lights.append(li.light((200.0, 10.0, 200.0), (0.0, 0.0, 10.0)))
	
		# PERFORMANCE CHECKS... 
		### 1.) verify that fps of pygame is accurate. 
		### 2.) see about reducing the amount of time numpy.dot takes?
		### 3.) look into high CPU usage for numpy in general.
		####
	camera = tpc.ThirdPersonCamera(player)

	func_status = "incomplete"
	next_func = None
	return func_status, next_func