# commandex <sup>v1.0.0</sup>

A cross-platform library for creation, storage, management of commands and command packages. Execution of commands, parsing of files with command packages.

---

![Platform](https://img.shields.io/badge/Windows%20%7C%20Linux%20%7C%20macOS%20%7C%20Termux-666?style=flat-square)
[![PyPI Downloads](https://static.pepy.tech/badge/commandex)](https://pepy.tech/projects/commandex)
![GitHub top language](https://img.shields.io/github/languages/top/smartlegionlab/commandex)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/commandex?label=pypi%20downloads)](https://pypi.org/project/commandex/)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/smartlegionlab/commandex)](https://github.com/smartlegionlab/commandex/)
[![GitHub](https://img.shields.io/github/license/smartlegionlab/commandex)](https://github.com/smartlegionlab/commandex/blob/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/commandex)](https://pypi.org/project/commandex)
[![PyPI - Format](https://img.shields.io/pypi/format/commandex)](https://pypi.org/project/commandex)
[![GitHub Repo stars](https://img.shields.io/github/stars/smartlegionlab/commandex?style=social)](https://github.com/smartlegionlab/commandex/)
[![GitHub watchers](https://img.shields.io/github/watchers/smartlegionlab/commandex?style=social)](https://github.com/smartlegionlab/commandex/)
[![GitHub forks](https://img.shields.io/github/forks/smartlegionlab/commandex?style=social)](https://github.com/smartlegionlab/commandex/)

---

## Description:

A cross-platform library for creation, storage, management of commands and command packages. 
Execution of commands, parsing of files with command packages.

- Store the required commands under a given name in a simple file with a clear structure.
- Read named command packages from a file.
- Use only the required command packages from a file using filtering.
- Execute command packages cross-platform. 

### How it works?

1. Create a file with any name, with the extension * .cfg
2. Use # as a comment, line break for convenience or separation.
3. Use [package name] to specify the name of the command package.
4. After the name, write the commands that you decided to combine under this name, one per line.
5. To create the next batch of commands, use points 2, 3 again.
6. Between commands, you can insert blank lines or comments, see point 2.

Used to create utilities for working with commands (execution, launch, autorun, storage).

You can keep your commands in simple and understandable files, collect them in one place,
split into named categories (packages) and execute at any time:

The files must have the extension *.cfg, and have the correct structure:


### commands.cfg:

```ini
# Comments

[package name 1]
command 1
command 2
command N

[package name 2]
command 1
command 2
command N
```

---


## Help:

### Install and Use:

- `pip install commandex`

Available tools:

- Pack - storing commands.
- Command executors - command execution.
- Pack makers - create a list with objects of command packages.
- Parsers - parsers for files with command packages.
- Filters - filtering commands.
- Factories - Fabric for creating objects. 

Principle of operation:

- Reading command packages from a file.
- Filter packages if needed.
- We create a list of package objects for future use.
- We execute commands from each package.


### Simplest implementation:

```python
from commandex import Commander

commander = Commander()
# Reading command packages from a file.
pack_dict = commander.parsers.cfg_parser.parse('file.cfg')
# Filter packages if needed.
packs = commander.filters.pack_filter.filter_pack_dict(pack_dict, add_list=[], exc_list=[])
# We create a list of package objects for future use.
pack_list = commander.makers.pack_maker.make_pack_list(packs)

# We execute commands from each package.
for pack in pack_list:
    print(pack.name)
    for command in pack.commands:
        print(command)
        commander.executors.os.execute(command)

```

### Termux, Windows support:

Utilities created with use work "commandex", without problems in Termux, Windows.

For example: [commandman](https://github.com/smartlegionlab/commandman).

---

### Test coverage:

#### Run tests:
- `pip install pytest`
- `pytest -v`
  

#### __Test coverage 100%__

- `pip install pytest-cov`
- `pytest --cov`

![commandex image](https://github.com/smartlegionlab/commandex/raw/master/data/images/commandex.png)


#### Report html:

- `pytest --cov --cov-report=html`

---

## ⚠️ Disclaimer

**By using this software, you agree to the full disclaimer terms.**

**Summary:** Software provided "AS IS" without warranty. You assume all risks.

**Full legal disclaimer:** See [DISCLAIMER.md](https://github.com/smartlegionlab/commandex/blob/master/DISCLAIMER.md)

---

## License

**[BSD 3-Clause License](https://github.com/smartlegionlab/commandex/blob/master/LICENSE)**

Copyright (©) 2026, [Alexander Suvorov](https://github.com/smartlegionlab)

---

