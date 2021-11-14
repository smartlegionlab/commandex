# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# -------------------------------------------------------


class TestOsExecutor:
    def test_execute(self, os_executor, command_status):
        command, status = command_status
        assert os_executor.execute(command) == status

    def test__call__(self, os_executor, command_status):
        command, status = command_status
        assert os_executor(command) == status


class TestSubExecutor:
    def test_execute(self, sub_executor, command_status):
        command, status = command_status
        assert sub_executor.execute(command) == status

    def test__call__(self, sub_executor, command_status):
        command, status = command_status
        assert sub_executor(command) == status
