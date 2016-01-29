# -*- coding: utf-8 -*-
#
#    Author: Nicolas Bessi, Olivier Jossen, Guewen Baconnier
#    Copyright 2011-2014 Camptocamp SA
#    Copyright 2014 brain-tec AG
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
from . import models


def post_init(cr, registry):
    """Import CSV data as it is faster than xml and because we can't use
    noupdate anymore with csv"""
    from openerp.tools import convert_file
    filename = 'data/res.bank.csv'
    convert_file(cr, 'l10n_ch_bank', filename, None, mode='init',
                 noupdate=True, kind='init', report=None)
