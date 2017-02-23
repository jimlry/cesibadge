from setuptools import setup

setup(
    name='raspweb',
    packages=['raspweb'],
    include_package_data=True,
    install_requires=[
        'flask',
	'flaskext.mysql'
    ],
)
