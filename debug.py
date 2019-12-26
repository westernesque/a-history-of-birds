import data.tools.mouse_picker as mp
import data.render_engine.display_manager as display
import data.render_engine.loader as l
import data.render_engine.master_renderer as mr
import data.terrains.terrain as t

if __name__ == "__main__":
	gameRunning = True
	display = display.DisplayManager()
	loader = l.Loader()
	renderer = mr.MasterRenderer(display.screen, loader)

mouse_picker = mp.MousePicker(camera, renderer.get_projection_matrix(), display.screen, terrain)
print("mouse current_ray: " + str(mouse_picker.get_current_ray()))