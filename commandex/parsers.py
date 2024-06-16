# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab
# --------------------------------------------------------
from abc import ABC, abstractmethod


class ParserBase(ABC):
    @abstractmethod
    def parse(self, file):
        """"""


class CfgParser(ParserBase):

    def parse(self, file):
        pack_dict = {}
        name = None
        for line in self._get_lines(file):

            if line and line.startswith('[') and line.endswith(']'):
                name = line.lstrip('[').rstrip(']')
                pack_dict[name] = []
                continue

            if name is not None and line:
                pack_dict[name].append(line)

        return pack_dict

    @staticmethod
    def _get_lines(file):
        try:
            with open(file, 'r', encoding='utf-8') as f:
                return [line.rstrip('\n') for line in f.readlines()
                        if line and not line.startswith('#') and not line == ' ' and not line == '\n']
        except (FileNotFoundError, PermissionError, OSError):
            return {}

    def __call__(self, file):
        return self.parse(file)


class Parsers:
    cfg_parser = CfgParser()
