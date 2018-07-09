import sys

import setuptools

install_requires = []
if sys.version_info < (3, 4):
    install_requires.append('enum34')

setuptools.setup(
    name='exitstatus',
    version='1.3.0',

    description='POSIX exit status codes',
    long_description=open('README.rst').read(),
    keywords='exit status POSIX',

    author='John Hagen',
    author_email='johnthagen@gmail.com',
    url='https://github.com/johnthagen/exitstatus',
    license='MIT',
    py_modules=['exitstatus'],
    install_requires=install_requires,

    zip_safe=False,

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
