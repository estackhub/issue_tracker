from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in issue_tracker_bar/__init__.py
from issue_tracker_bar import __version__ as version

setup(
	name="issue_tracker_bar",
	version=version,
	description="Issues status visual progress representation",
	author="Jide Olayinka",
	author_email="appdev@grossin.co",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
