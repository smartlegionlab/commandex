# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
import json
import os
from collections import namedtuple

import pytest

from commandex.commandpack import Command, Pack
from commandex.executors import OsExecutor, Executor, SubExecutor
from commandex.factories import ExecutorsFactory, CommandPackFactory, ParsersFactory, MakerFactory
from commandex.maker import PackMaker
from commandex.parsers import CfgParser, JsonParser, Parser


@pytest.fixture(scope='session', name='command')
def get_command():
    command = Command('echo "test"')
    return command


@pytest.fixture(scope='session', name='commands')
def get_commands():
    commands = [Command('echo "test"'), Command('echo "test2"'), ]
    return commands


@pytest.fixture(name='command_name')
def get_command_title():
    return 'echo "test"'


@pytest.fixture(name='os_executor')
def os_executor():
    return OsExecutor()


@pytest.fixture(name='sub_executor')
def sub_executor():
    return SubExecutor()


@pytest.fixture(params=[('echo "Smart Legion!"', True), ('bad_command', False)], name='command_status')
def command(request):
    yield request.param


@pytest.fixture(name='os_name', params=['posix', 'win'])
def get_os_names(request):
    yield request.param
    os.name = 'posix'


@pytest.fixture(name='executor')
def get_command_executor():
    return Executor()


@pytest.fixture(name='cfg_parser')
def get_cfg_parser():
    return CfgParser()


@pytest.fixture(name='data')
def get_data():
    data = r"""
[Ubuntu]
echo Ubuntu1
echo Ubuntu2

[Fedora]
echo Fedora1
echo Fedora2

[Manjaro]
echo Manjaro1
echo Manjaro2

[default]
echo default1
echo default2
"""
    return data


@pytest.fixture(name='path')
def get_dir(tmpdir, data):
    file = tmpdir.join('file.cfg')
    file.write(data)
    Path = namedtuple('Path', ('file', 'folder', 'cfg_data'))
    yield Path(file, tmpdir, data)


@pytest.fixture(name='pack_names')
def get_pack_names():
    return ['Ubuntu', 'Fedora', 'Manjaro', 'default']


@pytest.fixture(name='pack')
def get_pack():
    return Pack('Test')


@pytest.fixture(name='json_parser')
def get_json_parser():
    return JsonParser()


@pytest.fixture(name='data_json')
def get_data_json():
    data = {
        "Ubuntu":
            [
                'echo Ubuntu1',
                'echo Ubuntu2'
            ],
        "Fedora":
            [
                'echo Fedora1',
                'echo Fedora2'
            ],

        "Manjaro":
            [
                'echo Manjaro1',
                'echo Manjaro2'
            ],

        "default":
            [
                'echo default1',
                'echo default2'
            ]

    }

    return data


@pytest.fixture(name='file_json')
def get_file_json(tmpdir, data_json):
    file = tmpdir.join('file.json')
    with file.open('w') as f:
        json.dump(data_json, f)
    return file


@pytest.fixture(name='parser')
def get_smart_parser():
    return Parser()


@pytest.fixture(name='pack_list')
def get_pack_list(pack_names):
    pack_list = [Pack(name) for name in pack_names]
    return pack_list


@pytest.fixture(name='add_list')
def get_add_list(pack_names):
    return pack_names[:2]


@pytest.fixture(name='exc_list')
def get_exc_list(pack_names):
    return pack_names[:2]


@pytest.fixture(name='pack_maker')
def get_pack_maker():
    return PackMaker()


@pytest.fixture(name='executors_factory')
def get_executors_factory():
    return ExecutorsFactory()


@pytest.fixture(name='command_pack_factory')
def get_com_pack_fact():
    return CommandPackFactory()


@pytest.fixture(name='parsers_factory')
def get_parsers_fact():
    return ParsersFactory()


@pytest.fixture(name='makers_factory')
def get_makers_fact():
    return MakerFactory()
