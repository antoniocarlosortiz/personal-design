from setuptools import setup, find_packages
from pip.req import parse_requirements
import uuid

install_reqs = parse_requirements('requirements.txt', session=uuid.uuid1())
requirements = [str(ir.req) for ir in install_reqs]

config = {
    'description': 'Nodes and Edges',
    'author': 'SVI',
    'url': '',
    'download_url': '',
    'author_email': '',
    'version': '0.1',
    'install_requires': requirements,
    'packages': find_packages(),
    'scripts': [],
    'name': 'nodes_and_edges'
}

setup(**config)