import colander


class Award(colander.MappingSchema):
    title = colander.SchemaNode(colander.String())
    date = colander.SchemaNode(colander.Date())
    awarder = colander.SchemaNode(colander.String())
    summary = colander.SchemaNode(colander.String())

    def schema_type(self, **kw):
        return colander.Mapping(unknown='preserve')
