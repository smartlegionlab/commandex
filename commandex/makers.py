# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab
# --------------------------------------------------------
from commandex.commandpack import Pack


class PackMaker:
    @classmethod
    def make_pack_list(cls, pack_dict: dict):
        return [Pack(name=name, commands=commands) for name, commands in pack_dict.items()]


class Makers:
    pack_maker = PackMaker()
