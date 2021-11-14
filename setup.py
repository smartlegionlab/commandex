# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
from setuptools import setup, find_packages

setup(
      packages=find_packages(exclude=['tests', 'requirements', 'data']),
)
