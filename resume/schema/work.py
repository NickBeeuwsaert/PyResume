import colander

from .mixin import PreserveMixin


class Work(PreserveMixin, colander.MappingSchema):
    company = colander.SchemaNode(colander.String())
    position = colander.SchemaNode(colander.String())
    url = colander.SchemaNode(
        colander.String(),
        validator=colander.url,
        missing=colander.drop
    )
    start_date = colander.SchemaNode(colander.Date())
    end_date = colander.SchemaNode(colander.Date(), missing=colander.drop)
    summary = colander.SchemaNode(colander.String(), missing=colander.drop)
    highlights = colander.SequenceSchema(
        colander.SchemaNode(colander.String()),
        missing=[]
    )
