# -*- coding: utf-8 -*-
#
#    Author: Yannick Vaucher
#    Copyright 2015 Camptocamp SA
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
##############################################################################

"""
The banks have been created with dumb xml ids.
Change xml ids to keep track of those bank with
http://www.six-interbank-clearing.com/ (see README.rst for source)
"""


def migrate(cr, version):
    if not version:
        return

    query = (
        "UPDATE ir_model_data"
        "  SET name = 'bank_'||res_bank.clearing||_||res_bank.bank_branchid"
        "  FROM res_bank"
        "  WHERE module = 'l10n_ch_bank'"
        "    AND model = 'res.bank'"
        "    AND res_id = res_bank.id"
        "    AND res_bank.active = TRUE")
    cr.execute(query)
