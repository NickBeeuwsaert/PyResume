import colander

from .mixin import PreserveMixin


class Award(PreserveMixin, colander.MappingSchema):
    title = colander.SchemaNode(colander.String())
    date = colander.SchemaNode(colander.Date())
    awarder = colander.SchemaNode(colander.String())
    summary = colander.SchemaNode(colander.String())
