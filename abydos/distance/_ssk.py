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

"""abydos.distance._ssk.

String subsequence kernel (SSK) similarity
"""

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from ._token_distance import _TokenDistance
from ..tokenizer import QSkipgrams

__all__ = ['SSK']


class SSK(_TokenDistance):
    r"""String subsequence kernel (SSK) similarity.

    This is based on :cite:`Lodhi:2002`.


    .. versionadded:: 0.4.1
    """

    def __init__(self, tokenizer=None, ssk_lambda=0.9, **kwargs):
        """Initialize SSK instance.

        Parameters
        ----------
        tokenizer : _Tokenizer
            A tokenizer instance from the :py:mod:`abydos.tokenizer` package
        ssk_lambda : float
            A value in the range (0.0, 1.0) used for discouting gaps between
            characters according to the method described in :cite:`Lodhi:2002`.
        **kwargs
            Arbitrary keyword arguments

        Other Parameters
        ----------------
        qval : int
            The length of each q-skipgram. Using this parameter and
            tokenizer=None will cause the instance to use the QGramskipgrams
            tokenizer with this q value.


        .. versionadded:: 0.4.1

        """
        super(SSK, self).__init__(
            tokenizer=tokenizer, ssk_lambda=ssk_lambda, **kwargs
        )

        qval = 2 if 'qval' not in self.params else self.params['qval']
        self.params['tokenizer'] = (
            tokenizer
            if tokenizer is not None
            else QSkipgrams(qval=qval, start_stop='', scaler='SSK')
        )

    def sim_score(self, src, tar):
        """Return the SSK similarity of two strings.

        Parameters
        ----------
        src : str
            Source string for comparison
        tar : str
            Target string for comparison

        Returns
        -------
        float
            String subsequence kernel similarity

        Examples
        --------
        >>> cmp = SSK()
        >>> cmp.dist_abs('cat', 'hat')
        0.49743589743589733
        >>> cmp.dist_abs('Niall', 'Neil')
        0.35914053833129245
        >>> cmp.dist_abs('aluminum', 'Catalan')
        0.10798833377524023
        >>> cmp.dist_abs('ATCG', 'TAGC')
        -0.006418485237489689


        .. versionadded:: 0.4.1

        """
        self._tokenize(src, tar)

        src_wts = self._src_tokens
        tar_wts = self._tar_tokens

        score = 0.0
        for token in src_wts & tar_wts:
            score += src_wts[token] * tar_wts[token]

        return score

    def sim(self, src, tar):
        """Return the normalized SSK similarity of two strings.

        Parameters
        ----------
        src : str
            Source string (or QGrams/Counter objects) for comparison
        tar : str
            Target string (or QGrams/Counter objects) for comparison

        Returns
        -------
        float
            Normalized string subsequence kernel similarity

        Examples
        --------
        >>> cmp = SSK()
        >>> cmp.sim('cat', 'hat')
        0.7487179487179487
        >>> cmp.sim('Niall', 'Neil')
        0.6795702691656462
        >>> cmp.sim('aluminum', 'Catalan')
        0.5539941668876202
        >>> cmp.sim('ATCG', 'TAGC')
        0.49679075738125517


        .. versionadded:: 0.4.1

        """
        self._tokenize(src, tar)

        src_wts = self._src_tokens
        tar_wts = self._tar_tokens

        score = 0.0
        for token in src_wts & tar_wts:
            score += src_wts[token] * tar_wts[token]

        norm_src = 0.0
        for token in src_wts:
            norm_src += src_wts[token] * src_wts[token]

        norm_tar = 0.0
        for token in tar_wts:
            norm_tar += tar_wts[token] * tar_wts[token]

        return score / (norm_src * norm_tar) ** 0.5


if __name__ == '__main__':
    import doctest

    doctest.testmod()
