# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2025, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab
# --------------------------------------------------------
from commandex.executors import OsExecutor, SubExecutor, Executors
from commandex.filters import PackFilter, Filters
from commandex.makers import PackMaker, Makers
from commandex.parsers import CfgParser, Parsers


class ExecutorsFactory:
    @classmethod
    def get_os_executor(cls):
        return OsExecutor()

    @classmethod
    def get_sub_executor(cls):
        return SubExecutor()

    @classmethod
    def get_executors(cls):
        return Executors()


class FiltersFactory:
    @classmethod
    def get_pack_filter(cls):
        return PackFilter()

    @classmethod
    def get_filters(cls):
        return Filters()


class MakersFactory:
    @classmethod
    def get_pack_maker(cls):
        return PackMaker()

    @classmethod
    def get_makers(cls):
        return Makers()


class ParsersFactory:
    @classmethod
    def get_cfg_parser(cls):
        return CfgParser()

    @classmethod
    def get_parsers(cls):
        return Parsers()


class Factories:
    executors = ExecutorsFactory()
    filters = FiltersFactory()
    makers = MakersFactory()
    parsers = ParsersFactory()
