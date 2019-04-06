# -*- coding: utf-8 -*-

# Copyright 2019 by Christopher C. Little.
# This file is part of Abydos.
#
# Abydos is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Abydos is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Abydos. If not, see <http://www.gnu.org/licenses/>.

"""abydos.tests.tokenizer.test_tokenizer_qgrams.

This module contains unit tests for abydos.tokenizer.QGrams
"""

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from collections import Counter
import unittest

from abydos.tokenizer import QSkipgrams


class QSkipgramsTestCases(unittest.TestCase):
    """Test abydos.tokenizer.QSkipgrams."""

    def test_qskipgrams(self):
        """Test abydos.tokenizer.QSkipgrams."""
        self.assertEqual(sorted(QSkipgrams().tokenize('').get_list()), [])
        self.assertEqual(sorted(QSkipgrams().tokenize('a').get_list()), [])
        self.assertEqual(
            sorted(QSkipgrams().tokenize('ab').get_list()),
            sorted(['$a', '$b', '$#', 'ab', 'a#', 'b#']),
        )

        self.assertEqual(
            sorted(QSkipgrams().tokenize('NELSON').get_list()),
            sorted(
                [
                    '$N',
                    '$E',
                    '$L',
                    '$S',
                    '$O',
                    '$N',
                    '$#',
                    'NE',
                    'NL',
                    'NS',
                    'NO',
                    'NN',
                    'N#',
                    'EL',
                    'ES',
                    'EO',
                    'EN',
                    'E#',
                    'LS',
                    'LO',
                    'LN',
                    'L#',
                    'SO',
                    'SN',
                    'S#',
                    'ON',
                    'O#',
                    'N#',
                ]
            ),
        )
        self.assertEqual(
            sorted(QSkipgrams().tokenize('NEILSEN').get_list()),
            sorted(
                [
                    '$N',
                    '$E',
                    '$I',
                    '$L',
                    '$S',
                    '$E',
                    '$N',
                    '$#',
                    'NE',
                    'NI',
                    'NL',
                    'NS',
                    'NE',
                    'NN',
                    'N#',
                    'EI',
                    'EL',
                    'ES',
                    'EE',
                    'EN',
                    'E#',
                    'IL',
                    'IS',
                    'IE',
                    'IN',
                    'I#',
                    'LS',
                    'LE',
                    'LN',
                    'L#',
                    'SE',
                    'SN',
                    'S#',
                    'EN',
                    'E#',
                    'N#',
                ]
            ),
        )

        self.assertEqual(
            sorted(QSkipgrams(qval=1).tokenize('NEILSEN').get_list()),
            sorted(['N', 'E', 'I', 'L', 'S', 'E', 'N']),
        )
        self.assertEqual(
            QSkipgrams(qval=(2,), scaler='SSK')
            .tokenize('NEILSEN')
            .get_counter(),
            Counter(
                {
                    '$N': 1.2404672100000003,
                    '$E': 1.2072969000000002,
                    '$I': 0.6561,
                    '$L': 0.5904900000000001,
                    '$S': 0.531441,
                    '$#': 0.3874204890000001,
                    'NE': 1.341441,
                    'NI': 0.7290000000000001,
                    'NL': 0.6561,
                    'NS': 0.5904900000000001,
                    'NN': 0.4782969000000001,
                    'N#': 1.2404672100000003,
                    'EI': 0.81,
                    'EL': 0.7290000000000001,
                    'ES': 0.6561,
                    'EE': 0.5904900000000001,
                    'EN': 1.341441,
                    'E#': 1.2072969000000002,
                    'IL': 0.81,
                    'IS': 0.7290000000000001,
                    'IE': 0.6561,
                    'IN': 0.5904900000000001,
                    'I#': 0.531441,
                    'LS': 0.81,
                    'LE': 0.7290000000000001,
                    'LN': 0.6561,
                    'L#': 0.5904900000000001,
                    'SE': 0.81,
                    'SN': 0.7290000000000001,
                    'S#': 0.6561,
                }
            ),
        )
        self.assertEqual(
            QSkipgrams(qval=(4, 6, 5, 1, 0), scaler='SSK')
            .tokenize('NIALL')
            .get_counter(),
            Counter(
                {
                    '$$$N': 0.531441,
                    '$$$I': 0.4782969000000001,
                    '$$$A': 0.4304672100000001,
                    '$$$L': 0.7360989291000002,
                    '$$$#': 0.8504267154039002,
                    '$$NI': 1.4880348000000003,
                    '$$NA': 1.3392313200000003,
                    '$$NL': 2.2900855572000007,
                    '$$N#': 2.645772003478801,
                    '$$IA': 1.3392313200000003,
                    '$$IL': 2.2900855572000007,
                    '$$I#': 2.645772003478801,
                    '$$AL': 2.2900855572000007,
                    '$$A#': 2.645772003478801,
                    '$$LL': 1.0847773692000002,
                    '$$L#': 5.291544006957601,
                    '$$##': 2.460275073345601,
                    '$NIA': 1.4402051100000002,
                    '$NIL': 2.462750738100001,
                    '$NI#': 2.845254813264901,
                    '$NAL': 2.462750738100001,
                    '$NA#': 2.845254813264901,
                    '$NLL': 1.1665661391000004,
                    '$NL#': 5.690509626529802,
                    '$N##': 2.645772003478801,
                    '$IAL': 2.462750738100001,
                    '$IA#': 2.845254813264901,
                    '$ILL': 1.1665661391000004,
                    '$IL#': 5.690509626529802,
                    '$I##': 2.645772003478801,
                    '$ALL': 1.1665661391000004,
                    '$AL#': 5.690509626529802,
                    '$A##': 2.645772003478801,
                    '$LL#': 2.845254813264901,
                    '$L##': 5.291544006957601,
                    '$###': 0.8504267154039002,
                    'NIAL': 1.0097379000000002,
                    'NIA#': 1.1665661391000002,
                    'NILL': 0.4782969000000001,
                    'NIL#': 2.3331322782000004,
                    'NI##': 1.0847773692000002,
                    'NALL': 0.4782969000000001,
                    'NAL#': 2.3331322782000004,
                    'NA##': 1.0847773692000002,
                    'NLL#': 1.1665661391000002,
                    'NL##': 2.1695547384000005,
                    'N###': 0.3486784401000001,
                    'IALL': 0.531441,
                    'IAL#': 2.5923691980000005,
                    'IA##': 1.2053081880000003,
                    'ILL#': 1.2961845990000003,
                    'IL##': 2.4106163760000006,
                    'I###': 0.3874204890000001,
                    'ALL#': 1.4402051100000004,
                    'AL##': 2.6784626400000007,
                    'A###': 0.4304672100000001,
                    'LL##': 1.4880348000000003,
                    'L###': 1.0097379000000002,
                    '$$$$N': 0.4304672100000001,
                    '$$$$I': 0.3874204890000001,
                    '$$$$A': 0.3486784401000001,
                    '$$$$L': 0.5962401325710002,
                    '$$$$#': 0.8741476583623434,
                    '$$$NI': 1.5927286770000002,
                    '$$$NA': 1.4334558093000005,
                    '$$$NL': 2.4512094339030006,
                    '$$$N#': 3.59371815104519,
                    '$$$IA': 1.4334558093000005,
                    '$$$IL': 2.4512094339030006,
                    '$$$I#': 3.59371815104519,
                    '$$$AL': 2.4512094339030006,
                    '$$$A#': 3.59371815104519,
                    '$$$LL': 1.1610992055330005,
                    '$$$L#': 7.187436302090378,
                    '$$$##': 4.91876456439945,
                    '$$NIA': 2.2513435083000006,
                    '$$NIL': 3.849797399193001,
                    '$$NI#': 5.644187966956859,
                    '$$NAL': 3.849797399193001,
                    '$$NA#': 5.644187966956859,
                    '$$NLL': 1.8235882417230007,
                    '$$NL#': 11.28837593391372,
                    '$$N##': 7.725266868411147,
                    '$$IAL': 3.849797399193001,
                    '$$IA#': 5.644187966956859,
                    '$$ILL': 1.8235882417230007,
                    '$$IL#': 11.28837593391372,
                    '$$I##': 7.725266868411147,
                    '$$ALL': 1.8235882417230007,
                    '$$AL#': 11.28837593391372,
                    '$$A##': 7.725266868411147,
                    '$$LL#': 5.644187966956859,
                    '$$L##': 15.4505337368223,
                    '$$###': 4.918764564399449,
                    '$NIAL': 2.812715796861001,
                    '$NIA#': 4.123722629777913,
                    '$NILL': 1.3323390616710005,
                    '$NIL#': 8.247445259555828,
                    '$NI##': 5.644187966956858,
                    '$NALL': 1.3323390616710005,
                    '$NAL#': 8.247445259555828,
                    '$NA##': 5.644187966956858,
                    '$NLL#': 4.123722629777913,
                    '$NL##': 11.288375933913724,
                    '$N###': 3.593718151045189,
                    '$IALL': 1.3323390616710005,
                    '$IAL#': 8.247445259555828,
                    '$IA##': 5.644187966956858,
                    '$ILL#': 4.123722629777913,
                    '$IL##': 11.288375933913724,
                    '$I###': 3.593718151045189,
                    '$ALL#': 4.123722629777913,
                    '$AL##': 11.288375933913724,
                    '$A###': 3.593718151045189,
                    '$LL##': 5.644187966956858,
                    '$L###': 7.187436302090377,
                    '$####': 0.8741476583623434,
                    'NIALL': 0.4304672100000001,
                    'NIAL#': 2.664678123342001,
                    'NIA##': 1.8235882417230007,
                    'NILL#': 1.3323390616710005,
                    'NIL##': 3.6471764834460014,
                    'NI###': 1.1610992055330005,
                    'NALL#': 1.3323390616710005,
                    'NAL##': 3.6471764834460014,
                    'NA###': 1.1610992055330005,
                    'NLL##': 1.8235882417230007,
                    'NL###': 2.322198411066001,
                    'N####': 0.2824295364810001,
                    'IALL#': 1.4803767351900001,
                    'IAL##': 4.0524183149400015,
                    'IA###': 1.2901102283700003,
                    'ILL##': 2.0262091574700007,
                    'IL###': 2.5802204567400007,
                    'I####': 0.31381059609000006,
                    'ALL##': 2.2513435083000006,
                    'AL###': 2.8669116186000005,
                    'A####': 0.3486784401000001,
                    'LL###': 1.5927286770000004,
                    'L####': 0.8178876990000001,
                    'N': 1.0,
                    'I': 1.0,
                    'A': 1.0,
                    'L': 2.0,
                }
            ),
        )


if __name__ == '__main__':
    unittest.main()
