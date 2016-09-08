import colander

from .mixin import PreserveMixin


class Language(PreserveMixin, colander.MappingSchema):
    language = colander.SchemaNode(colander.String())
    fluency = colander.SchemaNode(colander.String())
