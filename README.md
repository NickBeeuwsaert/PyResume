# PyResume
---
PyResume generates a resume

## Resume format
PyResume uses the same [schema](https://jsonresume.org/schema/) defined by [JSON Resume](https://jsonresume.org/).

## Writing a plugin
You can customize which templating engine you use by writing a plugin. By default, PyResume ships with a Jinja2 renderer.

To create your own renderer, that subclasses the `pyresume.renderer.BaseRenderer` class.

Your renderer should have a `load_template` method that accepts a file object, and returns a object with a `render()` method.

To make your renderer visible to PyResume, make sure your setup.py has an `pyresume.renderer` entrypoint.

Sample Mako renderer:

```
import mako
import resume.renderer.BaseRenderer

class MakoRenderer(BaseRenderer):
    def load_template(self, template_fp):
        return mako.Template(template_fp.read())

```

setup.py entry_points:

```
    entry_points={
        'pyresume.renderer': [
            'mako = pyresume_mako:MakoRenderer'
        ]
    }
```
