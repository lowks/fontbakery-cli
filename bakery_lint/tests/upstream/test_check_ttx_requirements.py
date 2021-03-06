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
import re

from fontTools.ttLib import TTFont

from bakery_lint.base import BakeryTestCase as TestCase


class SourceTTXTest(TestCase):
    targets = ['upstream-ttx']
    tool = 'fontTools'
    name = __name__
    path = '.'

    def setUp(self):
        # TODO: Need somebody to check this options
        font = TTFont(None, lazy=False, recalcBBoxes=True,
                      verbose=False, allowVID=False)
        font.importXML(self.path, quiet=True)
        self.font = font
        # You can use ipdb here to interactively develop tests!
        # Uncommand the next line, then at the iPython prompt: print(self.path)
        # import ipdb; ipdb.set_trace()

    def test_ttx_doesnt_contain_duplicate_glyphs(self):
        """ Font doesnt contain duplicated glyphs.

            When fontbakery has resulted files with GlyphID <glyphname>#<int>
            generated, It can't be installed on some Mac OS X.

            For details see https://github.com/girish-dalvi/Ek-Mukta/issues/1
        """
        glyphs = []
        for g in self.font['glyf'].glyphs:
            # Each glyph must not match pattern <glyphname>#<int>
            # TODO: make sure that error occur even if in pattern
            # any characters used after number sign (#)
            self.assertFalse(re.search('#\w+$', g),
                             msg="Font contains incorrectly named glyph %s" % g)
            glyphID = re.sub('#\w+', '', g)

            # Each GlyphID has to be unique in TTX
            self.assertFalse(glyphID in glyphs,
                             msg="GlyphID %s occurs twice in TTX" % g)
            glyphs.append(glyphs)

    def test_os2_in_keys(self):
        """ This very important test checking if OS/2 is in keys method """
        self.assertIn('OS/2', self.font.keys())

    def test_epar_in_keys(self):
        """ Check If font has EPAR table """
        self.assertIn('EPAR', self.font.keys())
