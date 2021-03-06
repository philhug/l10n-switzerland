.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
    :alt: License: AGPL-3

Switzerland Payroll Rules
=========================

This module allows you to manage the salaries of your employees

** Features list :**
    * Add Swiss salary rule categories
    * Add Swiss salary rules
    * Add children in school to employee
    * Add LPP range to contract
    * Add LPP Amount to contract.
    * Add Worked Hours to contract.
    * Add Hourly Rate to contract.
    * Compute the Wage of contract, based on Worked Hours and Hourly Rate.
    * Add Holiday Rate to contract.

** For further information:** 
    * Please visit http://open-net.ch/blog/la-comptabilite-salariale-suisse-avec-odoo-1/tag/salaires-6

** Remarks: **
    * To prevent overwriting your salary rules changes, an update from 1.0.8 and lower to 1.0.9 and higher creates duplicates of the salary rules. This is because with some migrated databases, one may encounter a difficulty with the existing rules (they can not be erased if they are already used). The solution is then to force the existing ones to be non-updatable. And this is done using an included pre-migration script.
    * As this module proposes its own report (same as the original, but with its own footer), don't forget to make it non-updatable.

Known issues / Roadmap
======================

V1.0.0: 2014-11-07/Sge
    * Add Salary rule categories.
    * Add Salary rules.
    * Add Employee children in school.
    * Add Contract LPP rate.

V1.0.1: 2014-11-11/Sge
    * Set the 'LPP rate'' digits to 'Payroll Rate' decimal accuracy.

V1.0.2:
    * Add some minor changes, based on pull request #66 comments.

V1.0.3-4:
    * Add LPP Amount to contract.
    * Add Worked Hours Rate to contract.
    * Add Hourly Rate to contract.
    * Compute the Wage of contract, based on Worked Hours and Hourly Rate.
    * Add new salay rules

V1.0.5:
    * Add Holiday Rate to contract.
    * Update "Indemnité vacances 8,33%" rule to include
      "Holiday Rate" from contract.

V1.0.6:
    * Move salary rules from CSV file to XML file.
    * Import salary rules only at install.
    * Internal reorganization of files (.py and .xml).

V1.0.7:
    * Added: two new dependencies (hr_contract and hr_attendance)

V1.0.8:
    * Updated: the "Appears on slip" settings
    * Integrated: report for the payslip, with its own footer
    * Added: a pre-migration script
    * pre-migration script correctly set

Contributors
------------

* Sebastien Gendre <sge@open-net.ch>
* Yvon-Philippe Crittin <cyp@open-net.ch>

Maintainer
----------

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit http://odoo-community.org.
