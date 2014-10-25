import sublime, sublime_plugin
import os


class PythonCreatePackageCommand(sublime_plugin.WindowCommand):
    """
    Creates a Python Package (new folder with an empty __init__.py file inside it)

    Inspired on SideBarNewDirectoryCommand: https://github.com/curaloucura/SideBarEnhancements
    """
    def run(self, paths=[]):
        import functools
        self.window.run_command('hide_panel');
        if self._is_valid_args(paths):
            self.window.show_input_panel("Package Name:", "", functools.partial(self.on_done, paths[0]), None, None)

    def _is_valid_name(self, name):
        #TODO: is there a function that validates a python module name?
        return not (" " in name)

    def on_done(self, path, name):
        if not self._is_valid_name(name):
            sublime.error_message("Unable to create folder, invalid name.")
            return
            
        new_dir = os.path.join(path, name)
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)
            open(os.path.join(new_dir,"__init__.py"),'w').close()

            v = self.window.new_file()

            v.settings().set('default_dir', new_dir)
            v.settings().set('default_extension', 'py')
            v.set_syntax_file('Packages/Python/Python.tmLanguage')
        else:
            sublime.error_message("Unable to create folder, folder or file exists.")

    def _is_valid_args(self, paths):
        if len(paths) >= 1:
            return os.path.isdir(paths[0])
        else:
            False

    def is_enabled(self, paths = []):
        return self._is_valid_args(paths)

    def is_visible(self, paths= []):
        return self._is_valid_args(paths)
