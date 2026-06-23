# Source: https://github.com/hummbl-dev/arbiter/blob/main/pyproject.toml

[hummbl-dev](https://github.com/hummbl-dev) / **[arbiter](https://github.com/hummbl-dev/arbiter)** Public

- [Notifications](https://github.com/login?return_to=%2Fhummbl-dev%2Farbiter) You must be signed in to change notification settings
- [Fork 0](https://github.com/login?return_to=%2Fhummbl-dev%2Farbiter)
- [Star 0](https://github.com/login?return_to=%2Fhummbl-dev%2Farbiter)
 

 

## FilesExpand file tree

 main

/

# pyproject.toml

Copy path

Blame

More file actions

Blame

More file actions

## Latest commit

## History

[History](https://github.com/hummbl-dev/arbiter/commits/main/pyproject.toml)

History

46 lines (40 loc) · 1.48 KB

 main

/

# pyproject.toml

Copy path

Top

## File metadata and controls

- Code
 
- Blame
 

46 lines (40 loc) · 1.48 KB

[Raw](https://github.com/hummbl-dev/arbiter/raw/refs/heads/main/pyproject.toml)

Copy raw file

Download raw file

Open symbols panel

Edit and raw actions

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

32

33

34

35

36

37

38

39

40

41

42

43

44

45

46

\[build-system\]

requires = \["setuptools>=82.0.1"\]

build-backend = "setuptools.build\_meta"

\[project\]

name = "arbiter-score"

version = "0.6.0"

description = "Deterministic, polyglot code quality scoring with governance integration"

readme = "README.md"

license = {text = "Apache-2.0"}

requires-python = "\>=3.11"

authors = \[

{name = "Reuben Bowlby", email = "reuben@hummbl.io"},

\]

keywords = \["code-quality", "linting", "scoring", "governance", "arbiter", "hummbl"\]

classifiers = \[

"Development Status :: 4 - Beta",

"Intended Audience :: Developers",

"Topic :: Software Development :: Quality Assurance",

"Topic :: Software Development :: Testing",

"Programming Language :: Python :: 3.11",

"Programming Language :: Python :: 3.12",

"Programming Language :: Python :: 3.13",

"Programming Language :: Python :: 3.14",

\]

\[project.urls\]

Homepage = "https://hummbl.io/audit"

Repository = "https://github.com/hummbl-dev/arbiter"

Documentation = "https://github.com/hummbl-dev/arbiter#readme"

Changelog = "https://github.com/hummbl-dev/arbiter/releases"

Issues = "https://github.com/hummbl-dev/arbiter/issues"

\[project.optional-dependencies\]

analyzers = \["ruff>=0.4.0", "radon>=6.0.1", "vulture>=2.16", "bandit>=1.9.4"\]

test = \["pytest>=9.0.3"\]

all = \["ruff>=0.4.0", "radon>=6.0.1", "vulture>=2.16", "bandit>=1.9.4", "pytest>=9.0.3"\]

\[project.scripts\]

arbiter = "arbiter.\_\_main\_\_:main"

\[tool.setuptools.packages.find\]

where = \["src"\]

\[tool.pytest.ini\_options\]

testpaths = \["tests"\]