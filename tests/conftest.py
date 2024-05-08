# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab
# --------------------------------------------------------
from collections import namedtuple

import pytest

from commandex.commandpack import Pack
from commandex.executors import OsExecutor, SubExecutor
from commandex.factories import ExecutorsFactory, MakersFactory, ParsersFactory, FiltersFactory
from commandex.filters import PackFilter
from commandex.makers import PackMaker
from commandex.parsers import CfgParser


# Pack


@pytest.fixture(scope='session', name='command')
def get_command():
    return 'echo new command'


@pytest.fixture(scope='session', name='commands')
def get_commands():
    commands = ['echo "test"', 'echo "test2"', ]
    return commands


@pytest.fixture(name='pack')
def get_pack():
    return Pack('Test')


# Executors

@pytest.fixture(name='os_executor')
def os_executor():
    return OsExecutor()


@pytest.fixture(name='sub_executor')
def sub_executor():
    return SubExecutor()


@pytest.fixture(name='command_status', params=[('echo "Smart Legion!"', True), ('bad_command', False)],)
def command_status(request):
    yield request.param


# Factories

@pytest.fixture(name='executors_factory')
def get_executors_factory():
    return ExecutorsFactory()


@pytest.fixture(name='filters_factory')
def get_filters_factory():
    return FiltersFactory()


@pytest.fixture(name='makers_factory')
def get_makers_fact():
    return MakersFactory()


@pytest.fixture(name='parsers_factory')
def get_parsers_fact():
    return ParsersFactory()


# Filters

@pytest.fixture(name='pack_dict')
def get_pack_dict():
    return {'one': ['command1', 'command2'], 'two': ['command1', 'command2']}


@pytest.fixture(name='pack_filter')
def get_pack_filter():
    return PackFilter()


# Makers

@pytest.fixture(name='pack_maker')
def get_pack_maker():
    return PackMaker()


# Parsers


@pytest.fixture(name='cfg_parser')
def get_cfg_parser():
    return CfgParser()


@pytest.fixture(name='data')
def get_data():
    data = r"""
# comment

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


@pytest.fixture(name='pack_names')
def get_pack_names():
    return ['Ubuntu', 'Fedora', 'Manjaro', 'default']


@pytest.fixture(name='path')
def get_dir(tmpdir, data):
    file = tmpdir.join('file.cfg')
    file.write(data)
    Path = namedtuple('Path', ('file', 'folder', 'cfg_data'))
    yield Path(file, tmpdir, data)
