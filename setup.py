from setuptools import setup

with open("requirements.txt", "r") as f:
    pkgs = f.readlines()


setup(name='jgraph_hist',
      version='1.0',
      description='Create multi-class histograms with jgraph',
      author='Landon Harris',
      author_email='lharri73@vols.utk.edu',
      url='https://www.python.org/sigs/distutils-sig/',
      install_requires=pkgs,
      python_requires='>=3.6' #f-strings!
)
