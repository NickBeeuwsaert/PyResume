import colander


class Interest(colander.MappingSchema):
    name = colander.SchemaNode(colander.String())
    keyword = colander.SequenceSchema(
        colander.SchemaNode(colander.String())
    )

    def schema_type(self, **kw):
        return colander.Mapping(unknown='preserve')
