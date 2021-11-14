# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------


class TestPackMaker:
    def test_get_pack_list(self, path, file_json, pack_maker, pack_names, pack):
        assert isinstance(pack_maker.make_pack_list(path.file), list)
        assert isinstance(pack_maker.make_pack_list(file_json), list)
        packs = pack_maker.make_pack_list(path.file)
        assert all([isinstance(p, type(pack)) for p in packs])
        assert all([p.name in pack_names for p in packs])

    def test_add_list(self, path, pack_maker, add_list, pack_names):
        packs = pack_maker.make_pack_list(path.file, add_list=add_list)
        names = [pack.name for pack in packs]
        exclude_list = [name for name in pack_names if name not in names]
        assert all([name not in exclude_list and name in pack_names for name in names])

    def test_exc_list(self, path, pack_maker, exc_list, pack_names):
        packs = pack_maker.make_pack_list(path.file, exc_list=exc_list)
        names = [pack.name for pack in packs]
        assert all([name in pack_names and name not in exc_list for name in names])
