import colander

from .mixin import PreserveMixin


class Reference(PreserveMixin, colander.MappingSchema):
    name = colander.SchemaNode(colander.String())
    reference = colander.SchemaNode(colander.String())
