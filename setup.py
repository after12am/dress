from setuptools import setup, find_packages

setup(
    name='dress',
    version='pre-alpha',
    packages=find_packages(),
    install_requires=[
        'MySQL-python',
        'PyGreSQL',
        'jinja2',
        'PyYAML'
    ],
    entry_points={
        'console_scripts':
            'dress = dress.main:main'
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