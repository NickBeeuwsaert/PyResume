import colander

from .mixin import PreserveMixin


class Interest(PreserveMixin, colander.MappingSchema):
    name = colander.SchemaNode(colander.String())
    keyword = colander.SequenceSchema(
        colander.SchemaNode(colander.String())
    )
