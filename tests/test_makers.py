# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab
# --------------------------------------------------------
from commandex.commandpack import Pack


class TestPackMaker:
    def test_make_pack_list(self, pack_maker, pack_dict):
        assert isinstance(pack_maker.make_pack_list(pack_dict), list)
        assert all([isinstance(obj, Pack) for obj in pack_maker.make_pack_list(pack_dict)])
        assert len(pack_dict) == len(pack_maker.make_pack_list(pack_dict))
