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
import unicodedata

from bakery_lint.base import BakeryTestCase as TestCase, tags
from bakery_cli.ttfont import Font


class CheckGlyphExistence(TestCase):

    path = '.'
    name = __name__
    targets = ['result']
    tool = 'lint'

    def assertExists(self, d):
        font = Font.get_ttfont(self.path)
        glyphs = font.retrieve_cmap_format_4().cmap
        if not bool(ord(unicodedata.lookup(d)) in glyphs):
            self.fail('%s does not exist in font' % d)

    @tags('required')
    def test_nbsp(self):
        """ Check if 'NO-BREAK SPACE' exists in font glyphs """
        self.assertExists('NO-BREAK SPACE')

    @tags('required',)
    def test_space(self):
        """ Check if 'SPACE' exists in font glyphs """
        self.assertExists('SPACE')

    def test_euro(self):
        """ Check if 'EURO SIGN' exists in font glyphs """
        self.assertExists('EURO SIGN')
