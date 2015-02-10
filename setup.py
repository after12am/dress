from setuptools import setup, find_packages

setup(
    name='rhyme',
    version='pre-alpha',
    packages=find_packages(),
    install_requires=[
        'MySQL-python',
        'PyGreSQL',
        'jinja2',
        'yaml'
    ],
    entry_points={
        'console_scripts':
            'rhyme = rhyme.main:rhyme_main'
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