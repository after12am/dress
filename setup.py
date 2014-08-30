from setuptools import setup, find_packages

setup(
    name='ddd',
    version='pre-alpha',
    packages=find_packages(),
    install_requires=[
        'MySQL-python',
        'PyGreSQL',
        'jinja2'
    ],
    entry_points={
        'console_scripts':
            'ddd = ddd.main:ddd_main'
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