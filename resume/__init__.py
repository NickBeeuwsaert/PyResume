#!/usr/bin/env python
import argparse
import os
import re
import sys

import jinja2
import yaml

from resume.schema import Resume

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('resume', type=argparse.FileType('r'), help='Resume in YAML')
    parser.add_argument('template', type=str, help='Jinja2 template to use')
    parser.add_argument('--output', '-o', type=argparse.FileType('w'), default=sys.stdout)

    args = parser.parse_args()

    schema = Resume()
    environment = jinja2.Environment(
        loader=jinja2.FileSystemLoader([
            os.getcwd()
        ])
    )

    resume = schema.deserialize(yaml.load(args.resume, Loader=yaml.BaseLoader))
    template = environment.get_template(args.template)

    template.stream(**resume).dump(args.output)