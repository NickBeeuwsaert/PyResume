import colander
import pycountry

from .mixin import PreserveMixin


class Address(PreserveMixin, colander.MappingSchema):
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


class Profile(PreserveMixin, colander.MappingSchema):
    network = colander.SchemaNode(colander.String())
    username = colander.SchemaNode(colander.String())
    url = colander.SchemaNode(
        colander.String(),
        validator=colander.url
    )


class Basic(PreserveMixin, colander.MappingSchema):
    name = colander.SchemaNode(colander.String())
    label = colander.SchemaNode(colander.String())
    picture = colander.SchemaNode(
        colander.String(),
        missing=colander.drop
    )
    email = colander.SchemaNode(
        colander.String(),
        validator=colander.Email()
    )
    phone = colander.SchemaNode(colander.String())
    website = colander.SchemaNode(
        colander.String(),
        validator=colander.url
    )
    summary = colander.SchemaNode(colander.String(), missing=colander.drop)
    location = Address()
    profiles = colander.SequenceSchema(Profile(), missing=[])

