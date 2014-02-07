import sublime, sublime_plugin
import os
import functools

class CreatePackageCommand(sublime_plugin.WindowCommand):
    def run(self, dirs):
        self.window.show_input_panel("Package Name:", "", functools.partial(self.on_done, dirs[0]), None, None)

    def on_done(self, dir, name):
        new_dir = os.path.join(dir, name)
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)
            open(os.path.join(new_dir,"__init__.py"),'w').close()

            v = self.window.new_file()

            v.settings().set('default_dir', new_dir)
            v.settings().set('default_extension', 'py')
            v.set_syntax_file('Packages/Python/Python.tmLanguage')

    def is_visible(self, dirs):
        return len(dirs) == 1
