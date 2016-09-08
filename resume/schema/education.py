import colander

from .mixin import PreserveMixin


class Education(PreserveMixin, colander.MappingSchema):
    institution = colander.SchemaNode(colander.String())
    area = colander.SchemaNode(colander.String())
    study_type = colander.SchemaNode(colander.String())
    start_date = colander.SchemaNode(colander.Date())
    end_date = colander.SchemaNode(colander.Date())
    gpa = colander.SchemaNode(colander.Float())
    courses = colander.SequenceSchema(
        colander.SchemaNode(colander.String()),
        missing=[]
    )

