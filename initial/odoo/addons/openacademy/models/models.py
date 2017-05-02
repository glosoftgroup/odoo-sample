# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
	_name = 'openacademy.course'

	name = fields.Char(string="Title", required=True)
	description = fields.Text()

	responsible_id = fields.Many2one('res.users', ondelete='set null', string="Responsible", index=True)
	session_ids = fields.One2many('openacademy.session', 'course_id', string="Sessions")

#-- a session is an occurence of a course taught # at a given time for a given audience.
#a session has a name, startdate, duration & number of seats. # add action and menu item to display them.
#make the new model visible via a menu item

class Session(models.Model):
	_name='openacademy.session'

	name = fields.Char(required=True)
	start_date = fields.Date()
	duration = fields.Float(digits(6,2), help="Duration in days")
	#digits=(6, 2) specifies the precision of a float number: 6 is #the total number of digits, while 2 is the number of digits after the comma.
	# Note that it results in the number digits before the comma is a maximum 4
	seats = fields.Integer(string="Number of seats")

	instructor_id = fields.Many2one('res.partners', string="Instructor")
	course_id = fields.Many2one('openacademy.course',ondelete='cascade', string="Course", required=True)
	attendee_ids = fields.Many2many('res.partner', string="Attendees")
