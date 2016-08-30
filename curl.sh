#!/bin/sh
################################
## Auteur: HGK
## Date: 27/08/2016
## Version: 1.0
## Description: Script de test
################################

# Constants definition
# -----------------------------------------------------------------------------
HOST = "www.verychic.com"
LOGIN = "exo-verychic.com@travelsoft.fr"
MDP = "travelsoft"
COOKIE = "cookieverychic"
EMAIL = "null@travelsoft.fr"


#Function to connect on website
# -----------------------------------------------------------------------------
Connect() {
	# curl -c cookieverychic -u exo-verychic.com@travelsoft.fr:travelsoft www.verychic.com
	curl -c $4 -u $1:$2 $3
}

#Function to find product
# -----------------------------------------------------------------------------
FindProduct(){
   #curl -b cookieverychic -u exo-verychic.com@travelsoft.fr:travelsoft www.verychic.com -d "destination=spain" -d "Price >= 100"
   curl -c $4 -u $1:$2 $3 -d "destination=spain" -d "Price >= 100" --ignore-content-length > spain100.txt
   Nombre = $(wc -l spain.txt)
   echo "Le Nombre de produit est $Nombre"
}

#Function to send mail
# -----------------------------------------------------------------------------
SendMail() {
	echo $3 | mail -s $2 $1 
}

############ Main Program ##############
Connect $HOST $LOGIN $MDP $COOKIE

if [$? -ne 0];then
	SendMail $EMAIL "Problème de connexion" "Impossible de se connecter au site web"
	exit 1
else
	FindProduct $LOGIN $MDP $HOST $COOKIE
	SendMail $EMAIL "Nombre de produit espagne" "Le nombre de produit à destination de l'espagne dont le prix est supérieur à 100: $Nombre"
	exit 0
fi
