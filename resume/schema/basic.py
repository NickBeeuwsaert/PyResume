import colander
import pycountry


class Address(colander.MappingSchema):
    address = colander.SchemaNode(colander.String())
    postal_code = colander.SchemaNode(colander.String())
    city = colander.SchemaNode(colander.String())
    country_code = colander.SchemaNode(
        colander.String(),
        validator=colander.OneOf([
            country.alpha2
            for country in pycountry.countries
        ])
    )
    region = colander.SchemaNode(colander.String())

    def schema_type(self, **kw):
        return colander.Mapping(unknown='preserve')


class Profile(colander.MappingSchema):
    network = colander.SchemaNode(colander.String())
    username = colander.SchemaNode(colander.String())
    url = colander.SchemaNode(colander.String())

    def schema_type(self, **kw):
        return colander.Mapping(unknown='preserve')

class Basic(colander.MappingSchema):
    name = colander.SchemaNode(colander.String())
    label = colander.SchemaNode(colander.String())
    picture = colander.SchemaNode(
        colander.String(),
        missing=colander.drop
    )
    email = colander.SchemaNode(colander.String())
    phone = colander.SchemaNode(colander.String())
    website = colander.SchemaNode(colander.String())
    summary = colander.SchemaNode(colander.String(), missing=colander.drop)
    location = Address()
    profiles = colander.SequenceSchema(Profile(), missing=[])

    def schema_type(self, **kw):
        return colander.Mapping(unknown='preserve')
