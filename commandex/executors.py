# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab
# --------------------------------------------------------
import os
import subprocess
from abc import ABC, abstractmethod


class ExecutorBase(ABC):
    @abstractmethod
    def execute(self, command):
        """"""

    def __call__(self, command):
        return self.execute(command)


class OsExecutor(ExecutorBase):
    def execute(self, command):
        return not bool(os.system(command))


class SubExecutor(ExecutorBase):
    def execute(self, command):
        p = subprocess.Popen(command, shell=True, stderr=subprocess.DEVNULL)
        status = p.wait()
        return not bool(status)


class Executors:
    os = OsExecutor()
    sub = SubExecutor()
