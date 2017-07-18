import pygame, numpy, random
import data.render_engine.display_manager as display
import data.render_engine.loader as l
import data.render_engine.master_renderer as mr
import data.render_engine.light as li
import data.obj_loader.obj_file_loader as o
import data.render_engine.camera as c
import data.render_engine.third_person_camera as tpc
import data.shaders.static_shader as ss
import data.textures.model_texture as mt
import data.models.textured_model as tm
import data.terrains.terrain as t
import data.textures.terrain_texture as tt
import data.textures.terrain_texture_pack as ttp
import data.entities.entity as e
import data.entities.player as p

if __name__ == "__main__":
	gameRunning = True
	clock = pygame.time.Clock()
	display = display.display_manager()
	loader = l.loader()
	renderer = mr.master_renderer(display.screen)
	
	cube = o.obj_file_loader().load_obj("data\\models\\res\\cube.obj")
	cube_model = loader.load_to_vao(cube.get_vertices(), cube.get_texture_coordinates(), cube.get_normals(), cube.get_indices())
	textured_cube = tm.textured_model(cube_model, mt.model_texture(loader.load_texture("large_test")))
	textured_cube.get_texture().set_has_transparency(False)
	
	bush = o.obj_file_loader().load_obj("data\\models\\res\\grass_model.obj")
	bush_model = loader.load_to_vao(bush.get_vertices(), bush.get_texture_coordinates(), bush.get_normals(), bush.get_indices())
	textured_bush = tm.textured_model(bush_model, mt.model_texture(loader.load_texture("grass_texture")))
	
	textured_bush.get_texture().set_has_transparency(True)
	textured_bush.get_texture().set_use_fake_lighting(True)
	
	player_raw_model = o.obj_file_loader().load_obj("data\\models\\res\\bunny.obj")
	player_model = loader.load_to_vao(player_raw_model.get_vertices(), player_raw_model.get_texture_coordinates(), player_raw_model.get_normals(), player_raw_model.get_indices())
	textured_player_model = tm.textured_model(player_model, mt.model_texture(loader.load_texture("hmm")))
	
	player = p.player(textured_player_model, (0.0, 0.0, 0.0), 0.0, 0.0, 0.0, 1.0)
	
	entity_list = []
	bush_list = []
	for i in range(200):
		x = random.uniform(-50.0, 100.0)
		y = random.uniform(1.5, 100.0)
		z = random.uniform(-50.0, 100.0)
		rx = random.uniform(0.0, 180)
		ry = random.uniform(0.0, 180)
		entity_list.append(e.entity(textured_cube, (x, y, z), rx, ry, 0, 1))
		bush_list.append(e.entity(textured_bush, (x, 0, z), 0, ry, 0, 1))
	
	t_background_texture = tt.terrain_texture(loader.load_texture("leaf"))
	t_r_texture = tt.terrain_texture(loader.load_texture("dirt"))
	t_g_texture = tt.terrain_texture(loader.load_texture("hmm"))
	t_b_texture = tt.terrain_texture(loader.load_texture("cobblestone"))
	
	t_terrain_texture_pack = ttp.terrain_texture_pack(t_background_texture, t_r_texture, t_g_texture, t_b_texture)
	
	t_blend_map = tt.terrain_texture(loader.load_texture("blend_map"))
	
	terrain = t.terrain(-0.5, -0.5, loader, t_terrain_texture_pack, t_blend_map, "height_map")
	
	light = li.light((3000, 2000, 2000), (1.0, 1.0, 1.0))
	camera = tpc.third_person_camera(player)
	
	while gameRunning == True:
		clock.tick(60)
		pygame.display.set_caption("a history of birds " + "fps: " + str(clock.get_fps()))
		player.move(display)
		camera.move()
		renderer.render(light, camera)
		renderer.process_entity(player)
		renderer.process_terrain(terrain)
		for entity in entity_list:
			entity.increase_rotation(1.0, 1.0, 0.0)
			renderer.process_entity(entity)
		for bush in bush_list:
			renderer.process_entity(bush)
		display.update_display()
		for event in pygame.event.get():
			if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
				renderer.clean_up()
				loader.clean_up()
				display.close_display()
				gameRunning = False