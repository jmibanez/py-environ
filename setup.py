# -*- coding: utf-8 -*-
"""Setup script."""

from setuptools import setup

from version import get_git_version

setup(
    name='py-environ',
    version=get_git_version(),
    author="JM Ibanez",
    author_email="hi@jmibanez.com",
    description="A ConfigParser implementation with environment overrides",
    py_modules = ['py_environ'],
    package_dir = {'': '.'},
    install_requires=[
        "six>=1.9.0",
    ]
)
