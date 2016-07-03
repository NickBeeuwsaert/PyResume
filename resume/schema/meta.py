import colander


class Meta(colander.MappingSchema):
    url = colander.SchemaNode(colander.String(), validator=colander.url)

    def schema_type(self, **kw):
        return colander.Mapping(unknown='preserve')
