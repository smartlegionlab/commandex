# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
import pytest


class TestCfgParser:
    def test_parse(self, cfg_parser, path, pack_names):
        assert all([pack.name in pack_names for pack in cfg_parser.parse(path.file)])

    def test__call__(self, cfg_parser, path, pack_names):
        assert all([pack.name in pack_names for pack in cfg_parser(path.file)])

    def test_err(self, cfg_parser):
        assert cfg_parser.parse('bad_path') == []


class TestJsonParser:
    def test_parse(self, json_parser, file_json, pack_names):
        assert all([pack.name in pack_names for pack in json_parser.parse(file_json)])

    def test__call__(self, json_parser, path, pack_names):
        assert all([pack.name in pack_names for pack in json_parser(path.file)])

    def test_error(self, json_parser, path):
        assert json_parser(path.file) == []


class TestParser:
    def test_parse(self, parser, path, pack_names):
        assert all([pack.name in pack_names for pack in parser.parse(path.file)])
        assert all([pack.name in pack_names for pack in parser.cfg(path.file)])
        assert all([pack.name in pack_names for pack in parser.cfg.parse(path.file)])
        assert all([pack.name in pack_names for pack in parser.json(path.file)])
        assert all([pack.name in pack_names for pack in parser.json.parse(path.file)])

    @pytest.mark.parametrize('suffix', ['.json', '.cfg'])
    def test__get_parser(self, parser, cfg_parser, json_parser, suffix):
        if suffix == '.json':
            assert isinstance(parser._get_parser(suffix), type(json_parser))
        else:
            assert isinstance(parser._get_parser(suffix), type(cfg_parser))

    def test__call__(self, parser, path, pack_names):
        assert all([pack.name in pack_names for pack in parser(path.file)])
