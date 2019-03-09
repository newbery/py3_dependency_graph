import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()


setuptools.setup(
  name="py3_dependecy_graph",
  version="0.0.1",
  author="Cha Chen",
  author_email="chencha92111@gmail.com",
  description="A simple jedi based python3 dependency analysis tool",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/jam-world/py3_dependency_graph",
  packages=setuptools.find_packages(),
  install_requires=[
    'git', 'jedi', 'networkx'
  ],
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
)
