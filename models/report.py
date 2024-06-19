# -*- coding: utf-8 -*-

from odoo import models, fields

class Report(models.Model):
  """
  Define un informe
  """

  _name = 'maya_report.report'
  _description = 'Informe'

  code = fields.Char('Código', size = 9,required = True)
  name = fields.Char('Nombre', required = True)
  description = fields.Char('Descripción', required = True)
  version = fields.Char('Versión', required = True)
  module = fields.Char('Módulo', required = True)
  action = fields.Char('Acción', required = True)


  def run_report(self):
    for report in self:
      print('Ejecutanto report')
      action = self.env.ref(report.action).read()[0]
      return action
