#!/usr/bin/env python
import argparse
import os
from pkg_resources import iter_entry_points
import re
import sys

import jinja2
import yaml

from resume.schema import Resume
from resume.renderer import Jinja2Renderer

def main():
    # Load all plugins
    renderers = {
        r.name: r.load()
        for r in iter_entry_points(group='pyresume.renderer', name=None)
    }

    parser = argparse.ArgumentParser()
    parser.add_argument('resume', type=argparse.FileType('r'), help='Resume in YAML')
    parser.add_argument('template', type=argparse.FileType('r'), help='Jinja2 template to use')
    parser.add_argument('--output', '-o', type=argparse.FileType('w'), default=sys.stdout)
    parser.add_argument(
        '--renderer', '-r',
        type=str,
        choices=renderers.keys(),
        default='jinja2'
    )

    args = parser.parse_args()

    schema = Resume()
    renderer = renderers[args.renderer]()
    template = renderer.load_template(args.template)

    resume = schema.deserialize(yaml.load(args.resume, Loader=yaml.BaseLoader))

    args.output.write(template.render(**resume))
