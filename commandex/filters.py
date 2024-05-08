# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab
# --------------------------------------------------------


class PackFilter:
    @classmethod
    def filter_pack_dict(cls, pack_dict, add_list=None, exc_list=None):
        names = [name for name in pack_dict]

        exc_list = [] if exc_list is None else exc_list
        add_list = [] if add_list is None or exc_list else add_list

        if add_list:
            name_list = [str(name) for name in add_list if name in names and name not in exc_list]
        else:
            name_list = [str(name) for name in names if name in names and name not in exc_list]

        return {name: value for name, value in pack_dict.items() if name in name_list}


class Filters:
    pack_filter = PackFilter()
