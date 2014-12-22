import os
from setuptools import find_packages
from setuptools import setup

setup(
    name='AoikProjectStart',

    version='0.1',

    description="""Start code for Python project. Best practices cover package bootstrap, argument parsing, and error handling.""",

    long_description="""`Documentation on Github
<https://github.com/AoiKuiyuyou/AoikProjectStart-Python>`_""",

    url='https://github.com/AoiKuiyuyou/AoikProjectStart-Python',

    author='Aoi.Kuiyuyou',

    author_email='aoi.kuiyuyou@google.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='start python project',

    install_requires=[
    ],

    package_dir={'':'src'},

    packages=find_packages('src'),

    package_data={
    },

    entry_points={
        'console_scripts': [
            'aoikprojectstart=aoikprojectstart.aoikprojectstart:main',
        ],
    },
)
