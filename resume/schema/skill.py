import colander

from .mixin import PreserveMixin


class Skill(PreserveMixin, colander.MappingSchema):
    name = colander.SchemaNode(colander.String())
    level = colander.SchemaNode(colander.String())
    keywords = colander.SequenceSchema(
        colander.SchemaNode(
            colander.String()
        ),
        missing=[]
    )
