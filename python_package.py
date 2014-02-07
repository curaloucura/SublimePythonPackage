import sublime, sublime_plugin
import os
import functools

class CreatePackageCommand(sublime_plugin.WindowCommand):
    def run(self, dirs):
        self.window.show_input_panel("Package Name:", "", functools.partial(self.on_done, dirs[0]), None, None)

    def on_done(self, dir, name):
    	new_dir = os.path.join(dir, name)
        os.makedirs(new_dir)
        open(os.path.join(new_dir,"__init__.py"),'w').close()

        v = self.window.new_file()

        v.settings().set('default_dir', new_dir)

    def is_visible(self, dirs):
        return len(dirs) == 1
