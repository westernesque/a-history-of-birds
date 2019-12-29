class Scene:
    def __init__(self, window, master_renderer, renderer, obj_file_loader, loader):
        self.current_scene = self

    def input_listener(self, events):
        pass

    def update(self):
        pass

    def render(self):
        print("master renderer stuff, renderer, loader stuff here")
        pass

    def switch_to_scene(self, next_scene):
        self.current_scene = next_scene
