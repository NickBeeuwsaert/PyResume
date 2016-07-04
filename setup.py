from setuptools import setup

setup(
    name='PyResume',
    version='0.0.1',
    author='Nick Beeuwsaert',
    description='Tool to generate resumes',
    license='MIT',
    packages=[
        'resume'
    ],
    install_requires=[
        'PyYAML==3.11',
        'Jinja2==2.8',
        'colander==1.3.1',
        'pycountry==1.20'
    ],
    entry_points={
        'console_scripts': [
            'pyresume = resume:main'
        ],
        'pyresume.renderer': [
            'jinja2 = resume.renderer:Jinja2Renderer'
        ]
    }
)