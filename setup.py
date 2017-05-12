from setuptools import setup, find_packages
import sys, os

version = '0.1'

#packages = find_packages("dab",exclude=["*.tests.*", "tests.*", "tests"])

# setup(
#     name="deepin-auto-build",
#     author="Heysion Yuan",
#     packages = packages,
#     package_dir = {"":"dab"},
# )

setup(name='deepin-auto-discs',
      version=version,
      description="deepin auto build  platform",
      long_description="""build package & customer discs , manager repo
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='deepin-auto-build deepin-maker-discs dab dmd',
      author='heysion',
      author_email='heysion@deepin.com',
      url='deepin.org',
      license='GPLv3',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )


