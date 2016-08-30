#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

################################
## Auteur: HGK
## Date: 27/08/2016
## Version: 1.0
## Description: Script de test
################################

# Import des modules standard
# -----------------------------------------------------------------------------
from subprocess import call
from os import chdir
from smtplib import SMTP
from sys import exit

# Constants definition
# -----------------------------------------------------------------------------
HOST = "www.verychic.com"
LOGIN = "exo-verychic.com@travelsoft.fr"
MDP = "travelsoft"
COOKIE = "cookieverychic"

FOLDER = "/home/test"
FILE = "spain100.txt"

SENDER = "hervekouamo@gmail.com"
RECEVEIR = "null@travelsoft.fr"


# Définition de la classe CConnexionFTP
# -----------------------------------------------------------------------------
class CVerychic(object):

	def __init__(self, host, login, mdp, sender, receiver cookie):
		"""" Constructor
		"""
		# Init new connection object
		self.host, self.login, self.mdp, self.sender, self.receiver self.cookie = host, login, mdp, sender, receiver, cookie
	
	def connection(self):
		""" Function to connect on website
		"""
		self.statusconnect = False
		try:
			call(['curl', '-c', self.cookie, '-u', self.login:self.mdp, self.host])
			self.status = True
		except e:
			print "Connexion Error: %s" %e

	def findproduct(self):
		""" Function to find product
		"""
		self.statusfind = False
		try:
			chdir(FOLDER)
			call(['curl', '-c', self.cookie, '-u', self.login:self.mdp, self.host, '-d', 'destination=spain', '-d', 'Price >= 100', '--ignore-content-length', '>', FILE])

			fp = open(FILE 'rb')
			for i, line in enumerate(fp):
				self.NombreLigne = i + 1

			self.statusfind = True
		except e:
			print e

	def sendmail(self, sujet, message):
		"""Function to send mail
		"""
		message = """From: %s
		To: %s
		Subject: %s

		%s
		""" %(self.sender, self.receiver, sujet, message )

		try:
		   smtpObj = SMTP('localhost')
		   smtpObj.sendmail(self.sender, self.receiver, message)         
		   print "Successfully sent email"

		except SMTPException:
		   print "Error: unable to send email"


if __name__ == '__main__':

	""" Programme principal
	"""
	chic = CVerychic(HOST, LOGIN, MDP, SENDER, RECEVEIR, COOKIE)
	chic.connection()
	if chic.statusconnect:
		chic.findproduct()
		if chic.statusfind:
			chic.sendmail("Nombre de produit", "Le nombre de produit est: %s" % chic.NombreLigne )
			exit(0)
		else:
			chic.sendmail("Find Product Error", "Error during request to find product")
			exit(1)
	else:
		chic.sendmail("Connection Error", "Impossible to connect on website")
		exit(2)

