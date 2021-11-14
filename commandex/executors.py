# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
"""Tests for executors.py"""
import os
import subprocess
from abc import ABC, abstractmethod


class ExecutorBase(ABC):
    """Abstract Command Executor"""
    @abstractmethod
    def execute(self, command):
        """Execute command"""

    def __call__(self, command):
        return self.execute(command)


class OsExecutor(ExecutorBase):
    def execute(self, command):
        """
        Execute command.

        - To execute the command, os.system is used;

        :param command: <str> - command;
        :return: <bool> - status of execution command.
        """
        return not bool(os.system(command))


class SubExecutor(ExecutorBase):
    def execute(self, command):
        """
        Execute command.

        - To execute the command, subprocess is used;

        WARNING: Use with care, favor OsExecutor;

        :param command: <str> - command;
        :return: <bool> - status of execution command;
        """
        p = subprocess.Popen(command, shell=True, stderr=subprocess.DEVNULL)
        status = p.wait()
        return not bool(status)


class Executor:
    os = OsExecutor()
    sub = SubExecutor()
