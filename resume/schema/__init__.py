import colander

from .award import Award
from .basic import Basic
from .education import Education
from .interest import Interest
from .language import Language
from .meta import Meta
from .publication import Publication
from .reference import Reference
from .skill import Skill
from .volunteer import Volunteer
from .work import Work

from .mixin import PreserveMixin


class Resume(PreserveMixin, colander.MappingSchema):
    basic = Basic()
    work = colander.SequenceSchema(Work(), missing=[])
    volunteer = colander.SequenceSchema(Volunteer(), missing=[])
    awards = colander.SequenceSchema(Award(), missing=[])
    publications = colander.SequenceSchema(Publication(), missing=[])
    languages = colander.SequenceSchema(Language(), missing=[])
    interests = colander.SequenceSchema(Interest(), missing=[])
    references = colander.SequenceSchema(Reference(), missing=[])
    meta = Meta(missing=colander.drop)
