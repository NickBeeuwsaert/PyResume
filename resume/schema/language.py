import colander


class Language(colander.MappingSchema):
    language = colander.SchemaNode(colander.String())
    fluency = colander.SchemaNode(colander.String())

    def schema_type(self, **kw):
        return colander.Mapping(unknown='preserve')
