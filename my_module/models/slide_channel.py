from odoo import fields, models, tools


class Channel(models.Model):

    _inherit = "slide.channel"

    info_course = fields.Html(string="Información Curso", translate=tools.html_translate, sanitize_attributes=False, sanitize_form=False)
