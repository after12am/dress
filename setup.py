from setuptools import setup, find_packages

setup(
    name='dbdoc',
    version='pre-alpha',
    packages=find_packages(),
    install_requires=[
        'MySQL-python',
        'jinja2'
    ],
    entry_points={
        'console_scripts':
            'dbdoc = dbdoc.main:dbdoc_main'
    },
    zip_safe=False,
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
)