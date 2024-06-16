# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab
# --------------------------------------------------------


class TestPackFilter:
    def test_filter_pack_dict(self, pack_filter, pack_dict):
        add_list = [name for name in pack_dict][:1]
        exc_list = [name for name in pack_dict][1:]
        assert add_list == [name for name in pack_filter.filter_pack_dict(pack_dict, add_list=add_list)]
        assert all([name not in pack_filter.filter_pack_dict(pack_dict, exc_list=exc_list) for name in exc_list])
