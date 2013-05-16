from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
	name='ckanext-pat_categories',
	version=version,
	description="Show categories instead groups/organizations",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='Hyperborea',
	author_email='info@hyperborea.com',
	url='',
	license='',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.pat_categories'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
	],
	entry_points=\
	"""
        [ckan.plugins]
	pat_categories=ckanext.pat_categories.plugin:CategoryPlugin
	""",
)
