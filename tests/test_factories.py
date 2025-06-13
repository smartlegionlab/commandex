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


class TestExecutorsFactory:

    def test_get_os_executor(self, executors_factory):
        assert isinstance(executors_factory.get_os_executor(), OsExecutor)

    def test_get_sub_executor(self, executors_factory):
        assert isinstance(executors_factory.get_sub_executor(), SubExecutor)

    def test_get_executors(self, executors_factory):
        assert isinstance(executors_factory.get_executors(), Executors)


class TestFiltersFactory:
    def test_get_pack_filter(self, filters_factory):
        assert isinstance(filters_factory.get_pack_filter(), PackFilter)

    def test_get_filters(self, filters_factory):
        assert isinstance(filters_factory.get_filters(), Filters)


class TestMakersFactory:
    def test_get_pack_maker(self, makers_factory):
        assert isinstance(makers_factory.get_pack_maker(), PackMaker)

    def test_get_makers(self, makers_factory):
        assert isinstance(makers_factory.get_makers(), Makers)


class TestParsersFactory:
    def test_get_cfg_parser(self, parsers_factory):
        assert isinstance(parsers_factory.get_cfg_parser(), CfgParser)

    def test_get_parser(self, parsers_factory):
        assert isinstance(parsers_factory.get_parsers(), Parsers)
