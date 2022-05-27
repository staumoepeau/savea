from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in niu/__init__.py
from niu import __version__ as version

setup(
	name="niu",
	version=version,
	description="Niu tree of life",
	author="Finau Hoi Taumoepeau",
	author_email="nauhoi.taumoepeau@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
