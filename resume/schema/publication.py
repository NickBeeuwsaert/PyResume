import colander


class Publication(colander.MappingSchema):
    name = colander.SchemaNode(colander.String())
    publisher = colander.SchemaNode(colander.String())
    release_date = colander.SchemaNode(colander.Date())
    website = colander.SchemaNode(colander.String(), validator=colander.url)
    summary = colander.SchemaNode(colander.String())

    def schema_type(self, **kw):
        return colander.Mapping(unknown='preserve')
