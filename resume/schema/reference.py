import colander


class Reference(colander.MappingSchema):
    name = colander.SchemaNode(colander.String())
    reference = colander.SchemaNode(colander.String())

    def schema_type(self, **kw):
        return colander.Mapping(unknown='preserve')
