# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
from setuptools import find_packages, setup

setup(
    name="hydra-discovery-test-plugin",
    version="0.1.0",
    author="Omry Yadan",
    author_email="omry@fb.com",
    url="https://github.com/facebookresearch/hydra/",
    packages=find_packages(exclude=["tests"]),
    install_requires=["hydra-core==1.0.*"],
)
