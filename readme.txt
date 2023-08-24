Voici un bref aperçu de la structure du projet :

--index.html : 
Il s'agit de la page d'accueil du site web. Elle contient l'en-tête avec le nom de l'association caritative, 
un menu de navigation, une section expliquant la cause et un appel à l'action pour faire un don.

--promesses_enregistrees.html : 
Cette page affiche les promesses de dons qui ont été enregistrées. 
Elle comprend un tableau avec des colonnes pour le nom, le prénom, l'adresse, l'e-mail et le montant promis. 
Les données sont récupérées depuis la base de données à l'aide de la fonction lire_promesses().

--promesse_don.html : 
Cette page permet aux utilisateurs de faire une promesse de don. 
Elle présente un formulaire avec des champs pour le nom, le prénom, l'adresse, l'e-mail, 
le montant promis et une case à cocher pour accepter les conditions de don. Lorsque le formulaire est soumis, 
les données sont envoyées au serveur et stockées dans la base de données à l'aide de la fonction enregistrer_promesse().

--data.py : 
Ce module contient des fonctions pour la connexion à la base de données et la manipulation des données. 
Il fournit des fonctions pour se connecter à la base de données MySQL, insérer des promesses dans la base de données, 
lire toutes les promesses et lire une promesse par son identifiant.

--app.py :
 Il s'agit de l'application principale Flask. Il gère les itinéraires et les opérations côté serveur. 
Il existe trois itinéraires : la page d'accueil (/),
 la page pour faire une promesse de don (/promesse_don) et la page affichant les promesses enregistrées (/promesses_enregistrees). 
 L'application utilise les fonctions de data.py pour interagir avec la base de données et afficher les modèles HTML.