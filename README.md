# commandex

***

![GitHub top language](https://img.shields.io/github/languages/top/smartlegionlab/commandex)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/commandex?label=pypi%20downloads)](https://pypi.org/project/commandex/)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/smartlegionlab/commandex)](https://github.com/smartlegionlab/commandex/)
[![GitHub](https://img.shields.io/github/license/smartlegionlab/commandex)](https://github.com/smartlegionlab/commandex/blob/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/commandex)](https://pypi.org/project/commandex)
[![PyPI - Format](https://img.shields.io/pypi/format/commandex)](https://pypi.org/project/commandex)
[![GitHub Repo stars](https://img.shields.io/github/stars/smartlegionlab/commandex?style=social)](https://github.com/smartlegionlab/commandex/)
[![GitHub watchers](https://img.shields.io/github/watchers/smartlegionlab/commandex?style=social)](https://github.com/smartlegionlab/commandex/)
[![GitHub forks](https://img.shields.io/github/forks/smartlegionlab/commandex?style=social)](https://github.com/smartlegionlab/commandex/)

***

## Help the project financially:

- Yandex Money: [https://yoomoney.ru/to/4100115206129186](https://yoomoney.ru/to/4100115206129186)
- PayPal: [https://paypal.me/smartlegionlab](https://paypal.me/smartlegionlab)
- LiberaPay: [https://liberapay.com/smartlegion/donate](https://liberapay.com/smartlegion/donate)
- Visa: 4048 0250 0089 5923

***

## Short Description:

___commandex___ -  A cross-platform library for creation, storage, management of commands and command packages. Execution of commands, parsing of files with command packages.

***

Author and developer: ___A.A Suvorov___

[![smartlegiondev@gmail.com](https://img.shields.io/static/v1?label=email&message=smartlegiondev@gmail.com&color=blue)](mailto:smartlegiondev@gmail.com)

***

## Supported:

- Linux: All.
- Windows: 7/8/10.
- Termux (Android).

***

## Requirements:

- [Python](https://python.org) 3.6+
  - [Download](https://python.org)
  
***

## What's new?

___commandex v0.1.0___


***

## Description:

A cross-platform library for creation, storage, management of commands and command packages. 
Execution of commands, parsing of files with command packages.
 
Used to create utilities for working with commands (execution, launch, autorun, storage).

You can keep your commands in simple and understandable files, collect them in one place,
split into named categories (packages) and execute at any time:

The files must have the extension *.cfg, or *.json and have the correct structure:


### commands.cfg:

```text
[package name 1]
command 1
command 2
command N

[package name 2]
command 1
command 2
command N
```

### commands.json:

```json5
{
  "name1":

  [
    "command1",
    "command2",
    "commandN"
  ],

  "name2":

  [
    "command1",
    "command2",
    "commandN"
  ]
}
```

***


## Help:

### Install and Use:

- `pip3 install commandex`

Available tools:

- Command executors
- Pack makers
- Parsers
- Commands
- Packs
- Factories

```python
from commandex import Commander
from commandex.executors import OsExecutor, SubExecutor, Executor
from commandex.commandpack import Command, Pack
from commandex.parsers import CfgParser, JsonParser, Parser
from commandex.maker import PackMaker
commander = Commander()

os_executor = OsExecutor()
sub_executor = SubExecutor()
executor = Executor()

command = Command('pip list')
pack = Pack('default')

cfg_parser = CfgParser()
json_parser = JsonParser()
parser = Parser()

pack_maker = PackMaker()

```

### Termux support:

Utilities created with use work "commandex", without problems in Termux.

### Windows support:

- Install [python](https://python.org)
- `pip3 install commandex`

Utilities created with use work "commandex", without problems in Windows:

### Test coverage:

#### Run tests:
- `pip3 install pytest`
- `pytest -v`
  

#### __Test coverage 100%__

- `pip install pytest-coverage`
- `pytest --cov`

![commandex image](https://github.com/smartlegionlab/commandex/raw/master/data/images/commandex.png)


#### Report html:

- `pytest --cov --cov-report=html`

***

## Disclaimer of liability:

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
    FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
    DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
    SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
    CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
    OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

***

## Copyright:
    --------------------------------------------------------
    Licensed under the terms of the BSD 3-Clause License
    (see LICENSE for details).
    Copyright © 2018-2021, A.A Suvorov
    All rights reserved.
    --------------------------------------------------------