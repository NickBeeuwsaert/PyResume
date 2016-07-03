import colander

from resume.schema.award import Award
from resume.schema.basic import Basic
from resume.schema.education import Education
from resume.schema.interest import Interest
from resume.schema.language import Language
from resume.schema.meta import Meta
from resume.schema.publication import Publication
from resume.schema.reference import Reference
from resume.schema.skill import Skill
from resume.schema.volunteer import Volunteer
from resume.schema.work import Work


# RESUME
class Resume(colander.MappingSchema):
    basic = Basic(unknown='preserve')
    work = colander.SequenceSchema(Work(), missing=[])
    volunteer = colander.SequenceSchema(Volunteer(), missing=[])
    awards = colander.SequenceSchema(Award(), missing=[])
    publications = colander.SequenceSchema(Publication(), missing=[])
    languages = colander.SequenceSchema(Language(), missing=[])
    interests = colander.SequenceSchema(Interest(), missing=[])
    references = colander.SequenceSchema(Reference(), missing=[])
    meta = Meta(missing=colander.drop)
