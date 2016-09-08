import colander


class PreserveMixin(object):
    def schema_type(self, **kw):
        """Keep any unknown items as-is"""
        return colander.Mapping(unknown='preserve')
