import sublime, sublime_plugin, re

class AssignmentCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    for point in self.view.sel():
      if not point.empty():
        text             = self.view.substr(point)
        full_point       = self.view.line(point)
        lines_point      = self.view.lines(point)
        full_selection   = self.view.substr(full_point)
        first_line_point = self.view.substr(lines_point[0])
        indent           = re.findall('^\s+', first_line_point)[0]
        keys             = []
        values           = []
        no_key_values    = []

        for line_point in lines_point:
          line          = self.view.substr(line_point)
          key_value     = line.split('=')

          if len(key_value) == 2:
            keys.append(key_value[0].strip())
            values.append(key_value[1].strip())
          else:
            no_key_values.append(line.encode('utf-8') + "\n")

        if len(keys) < 2:
          return False;

        no_key_value_content = "\n\n"

        for no_key_value in no_key_values:
          no_key_value_content += no_key_value

        duplicates = {}

        for key in keys:
          times = keys.count(key)

          if times > 1:
            duplicates[key.encode('utf-8')] = ("%s times" % times)

        warning = "# WARNING: duplicate assignments: %s" % duplicates

        full_region   = sublime.Region(full_point.begin(), full_point.end())
        output        = '%s = %s' % (', '.join(keys), ', '.join(values))

        final_content = ''

        if len(duplicates) > 0:
          final_content = indent + warning + "\n"

        final_content += indent + output + no_key_value_content

        self.view.replace(edit, full_region, final_content)
