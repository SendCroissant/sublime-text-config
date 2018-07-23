import sublime, sublime_plugin
class AddConsoleLog(sublime_plugin.TextCommand):
    def run(self, edit):
        selection = self.view.sel()
        new_selection = [];
        for region in selection:
            if region.empty():
                print('\n--empty line--\n')
                # line_contents = self.view.substr(line) + '\n'
            else:
                line = self.view.line(region)
                line_contents = self.view.substr(region) + '\n'
                self.view.insert(edit, line.end() + 1, line_contents)
                newBegin = line.end() + 1
                newEnd = newBegin + len(line_contents)
                region.a = newBegin
                region.b = newEnd - 1
                new_selection.append(region)
        selection.clear();
        selection.add_all(new_selection);
