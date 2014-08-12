# coding: utf-8
# Copyright 2013 The Font Bakery Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# See AUTHORS.txt for the list of Authors and LICENSE.txt for the License.

from setuptools import setup

setup(
    name="FontBakery-cli",
    version='0.1',
    url='https://github.com/googlefonts/fontbakery-cli/',
    description='fontbakery-cli',
    author='Vitaliy Volkov',
    author_email='hash3g@gmail.com',
    packages=["bakery_cli",
              "bakery_cli.pipe",
              "bakery_cli.scripts",
              "bakery_lint",
              "bakery_lint.tests",
              "bakery_lint.tests.downstream",
              "bakery_lint.tests.upstream",
              "bakery_cli.scrapes",
              "bakery_cli.scrapes.familynames",
              "bakery_cli.scrapes.familynames.familynames",
              "bakery_cli.scrapes.familynames.familynames.spiders"],
    scripts=['tools/fontbakery.py',
             'tools/font2ttf.py',
             'tools/genmetadata.py',
             'tools/bakery-ascii-fix.py',
             'tools/bakery-fstype-fix.py',
             'tools/bakery-nbsp-fix.py',
             'tools/bakery-stylenames-fix.py',
             'tools/bakery-vmet-fix.py',
             'tools/bakery-lint.py'
             ],
    zip_safe=False,
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    package_data={
        '': [
            'defaults.yaml',
            'scrapes/familynames/scrapy.cfg',
            'tests/upstream/diacritics.txt',
            'tests/*.txt',
            'tests/*.mkd'
        ]
    },
    install_requires=[
        'lxml',
        'requests',
        'fonttools',
        'pyyaml',
        'robofab',
        'fontaine'
    ],
    dependency_links=['https://github.com/behdad/fontTools/tarball/master#egg=fontTools-2.4'],
)
