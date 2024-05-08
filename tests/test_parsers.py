# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab
# --------------------------------------------------------


class TestCfgParser:
    def test_parse(self, cfg_parser, path, pack_names):
        assert all([name in pack_names for name in cfg_parser.parse(path.file)])

    def test__call__(self, cfg_parser, path, pack_names):
        assert all([name in pack_names for name in cfg_parser(path.file)])

    def test_err(self, cfg_parser):
        assert cfg_parser.parse('bad_path') == {}
