import colander


class Skill(colander.MappingSchema):
    name = colander.SchemaNode(colander.String())
    level = colander.SchemaNode(colander.String())
    keywords = colander.SequenceSchema(
        colander.SchemaNode(
            colander.String()
        ),
        missing=[]
    )

    def schema_type(self, **kw):
        return colander.Mapping(unknown='preserve')
