import jinja2


class BaseRenderer(object):
    def load_template(self, template_fp):
        pass

class Jinja2Renderer(BaseRenderer):
    def load_template(self, template_fp):
        return jinja2.Template(template_fp.read())
