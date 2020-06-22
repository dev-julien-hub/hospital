# -*- coding: utf-8 -*-

from odoo import models, fields, api


class patient(models.Model):
    _name = 'hospital.patient'

    name = fields.Char(string="Nom du patient", required=True)
    age = fields.Integer(string="Age du patient")
    disease = fields.Char(string="Maladie")
    description = fields.Text()

    # docteur_id = fields.One2many('hospital.doctor', 'doctor_id', string="Docteur")
    docteurs_id = fields.One2many('hospital.doctor', 'doctors_id', string="Docteurs")


class Doctor(models.Model):
    _name = "hospital.doctor"

    name = fields.Char(string="Docteur", reaquired=True)
    specialist = fields.Char(string="spécialiste")
    adress = fields.Char(string='Adress')

    # doctor_id = fields.Many2one('res.partner', ondelete='cascade', required=True)
    doctors_id = fields.Many2one('res.partner', ondelete='cascade', required=True)
