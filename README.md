# python-boilerplate-package
[![building](https://img.shields.io/travis/fernandojunior/python-boilerplate-package.svg)](https://travis-ci.org/fernandojunior/python-boilerplate-package)

Boilerplate to create a project with a Python [package](https://docs.python.org/3/tutorial/modules.html#packages). More information at [@fernandojunior/python-boilerplate](https://github.com/fernandojunior/python-boilerplate).

```python
>>> from package_name import foo
>>> print(foo.bar())
Hello World
```

Also as a command-line script:
```sh
$ package_name Hello World
Hello World
```

## Features

* [coverage.py](https://coverage.readthedocs.org/) - Code coverage measurement.
* [Flake8](https://flake8.readthedocs.org/) - The modular source code checker: pep8, pyflakes and co.
* [pytest](http://pytest.org/) - A mature full-featured Python testing tool.
* [setuptools](https://pythonhosted.org/setuptools/setuptools.html) - Easily download, build, install, upgrade, and uninstall distribution packages.
* [tox](https://tox.readthedocs.org/) - Auto builds and tests distributions in multiple Python versions using virtualenvs.

## Structure

```sh
├── CONTRIBUTING.md
├── LICENSE
├── Makefile
├── MANIFEST.in
├── package_name  # The core code of the project
│   ├── foo.py
│   ├── __init__.py
│   └── __main__.py
├── README.md
├── requirements
│   ├── dev.txt
│   └── prod.txt
├── requirements.txt
├── setup.cfg
├── setup.py
├── tests
│   ├── __init__.py
│   └── test_foo.py
└── tox.ini
```

More datails [here](https://github.com/fernandojunior/python-boilerplate#structure).

## Keywords

* author_name - Full name of the author.
* github_username - GitHub username.
* package_name - Name of the package using [PEP8 style](https://www.python.org/dev/peps/pep-0008/#package-and-module-names).
* project_name - Short name of your project using [slug style](https://en.wikipedia.org/wiki/Semantic_URL#Slug).

You can use your preferred text editor or IDE to find the keywords. In [Sublime](https://www.sublimetext.com/) and [Atom](https://atom.io/) this is done by `Ctrl + Shift + F`.

## Contributing

See [CONTRIBUTING](/CONTRIBUTING.md).

## License

[![CC0](https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

The MIT License.

-

Copyright (c) 2016 [Fernando Felix do Nascimento Junior](https://github.com/fernandojunior/).
