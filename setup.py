from setuptools import setup


setup(
    name='rep',
    version='0.1',
    author='Shlomo Tadela',
    py_modules=['rep-cli'],
    install_requires=[
        'Click', 'diskcache', 'censys', 'bs4'
    ],
    entry_points='''
        [console_scripts]
        rep=cli:cli
    ''',
)