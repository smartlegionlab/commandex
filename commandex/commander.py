# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
from commandex.executors import Executor
from commandex.factories import CommandExFactory
from commandex.maker import PackMaker
from commandex.parsers import Parser


class Commander:
    factories = CommandExFactory()
    executors = Executor()
    maker = PackMaker()
    parser = Parser()
