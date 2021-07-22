#!/usr/bin/env python3

#Copyright (C) 2021  tuxifreund <kaiser.barbarossa@yandex.com>
#
#This file is part of MyBrowse.
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <https://www.gnu.org/licenses/>.

import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='mybrowse',
    version='0.4',
    author='tuxifreund',
    author_email='kaiser.barbarossa@yandex.com',
    description='MyBrowse is a simple browser written in Python3 using WebKit and GTK',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/KaiserBarbarossa/MyBrowse',
    project_urls={
        'Bug Tracker': 'https://github.com/KaiserBarbarossa/MyBrowse/issues',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: POSIX :: Linux',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Browsers',
        'Environment :: X11 Applications :: GTK',
    ],
    scripts=['mybrowse'],
    python_requires='>=3.6',
)

