from pathlib import Path

import setuptools

project_dir = Path(__file__).parent

setuptools.setup(
    name='exitstatus',
    version='2.0.1',

    description='POSIX exit status codes',
    long_description=project_dir.joinpath('README.rst').read_text(encoding='utf-8'),
    keywords='exit status POSIX',

    author='John Hagen',
    author_email='johnthagen@gmail.com',
    url='https://github.com/johnthagen/exitstatus',

    py_modules=['exitstatus'],
    python_requires='>=3.5',
    zip_safe=False,

    license='MIT',
    license_files=['LICENSE.txt'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
