# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab
# --------------------------------------------------------
from commandex.filters import Filters
from commandex.makers import Makers
from commandex.parsers import Parsers
from commandex.executors import Executors
from commandex.factories import Factories


class Commander:
    factories = Factories()
    executors = Executors()
    filters = Filters()
    makers = Makers()
    parsers = Parsers()
