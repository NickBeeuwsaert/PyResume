import colander

from .mixin import PreserveMixin


class Meta(PreserveMixin, colander.MappingSchema):
    url = colander.SchemaNode(colander.String(), validator=colander.url)
