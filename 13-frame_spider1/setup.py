#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Power by HPCM   2018-09-27 17:59:47


try:
    # pip 版本小于10导入
    from pip.req import parse_requirements
except:
    # pip 版本大于10导入
    from pip._internal.req import parse_requirements

from setuptools import find_packages, setup

with open("version.txt", "rb") as f:
    version = f.read().decode("utf-8").strip()

setup(
        name = "myscrapy",
        version = version,
        description = "A frame spider, like scrapy",
        packages = find_packages(exclude=[]),
        url = "#",
        install_requires = [str(ir.req) for ir in parse_requirements("requirements.txt", session=False)],
        zip_safe = False,
        classifiers = [
                "Programming Language :: Python",
                "Operating System :: Microsoft :: windows",
                "Operating System :: Uninx",
                "Programming Language :: Python :: 2.7",
                "Programming Language :: Python :: 3.4",
                "Programming Language :: Python :: 3.5",
                "Programming Language :: Python :: 3.6"
            ]
        )
