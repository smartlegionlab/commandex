from commandex.commandpack import Command, Pack
from commandex.executors import OsExecutor, SubExecutor, Executor
from commandex.maker import PackMaker
from commandex.parsers import CfgParser, JsonParser, Parser


class TestExecutorsFactory:

    def test_get_os_executor(self, executors_factory):
        assert isinstance(executors_factory.get_os_executor(), OsExecutor)

    def test_get_sub_executor(self, executors_factory):
        assert isinstance(executors_factory.get_sub_executor(), SubExecutor)

    def test_get_executor(self, executors_factory):
        assert isinstance(executors_factory.get_executor(), Executor)


class TestCommandPackFactory:
    def test_create_command(self, command_pack_factory):
        assert isinstance(command_pack_factory.create_command('name'), Command)

    def test_create_pack(self, command_pack_factory):
        assert isinstance(command_pack_factory.create_pack('name'), Pack)


class TestParsersFactory:
    def test_get_cfg_parser(self, parsers_factory):
        assert isinstance(parsers_factory.get_cfg_parser(), CfgParser)

    def test_get_json_parser(self, parsers_factory):
        assert isinstance(parsers_factory.get_json_parser(), JsonParser)

    def test_get_parser(self, parsers_factory):
        assert isinstance(parsers_factory.get_parser(), Parser)


class TestMakerFactory:
    def test_get_pack_maker(self, makers_factory):
        assert isinstance(makers_factory.get_pack_maker(), PackMaker)
