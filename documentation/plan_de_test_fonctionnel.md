# Plan de Test Fonctionnel pour le MVP1

Le plan de Test Fonctionnel suivant concerne les tâches du MVP1 définis plus haut.

## Authentification des Utilisateurs

### Création de Comptes Utilisateurs

* Vérifier que les utilisateurs peuvent créer un compte avec succès en fournissant un nom d'utilisateur, une adresse email et un mot de passe valide.
* Vérifier que les champs obligatoires sont correctement validés et que les messages d'erreur appropriés sont affichés en cas de saisie incorrecte.
* Vérifier que les informations des utilisateurs sont correctement enregistrées dans la base de données après la création du compte.

### Connexion Utilisateur

* Vérifier que les utilisateurs peuvent se connecter avec succès en utilisant leur nom d'utilisateur et leur mot de passe.
* Vérifier que les utilisateurs sont redirigés vers la page appropriée après une connexion réussie.
* Vérifier que les utilisateurs reçoivent un message d'erreur approprié en cas de saisie incorrecte des informations de connexion.

### Récupération de Mot de Passe

* Vérifier que les utilisateurs peuvent demander une réinitialisation de leur mot de passe en fournissant leur adresse email.
* Vérifier que les utilisateurs reçoivent un lien sécurisé de réinitialisation de mot de passe à l'adresse email associée à leur compte.
* Vérifier que les utilisateurs peuvent réinitialiser leur mot de passe avec succès en utilisant le lien reçu.

## Gestion des Comptes Utilisateurs

### Modification des Informations Personnelles

* Vérifier que les utilisateurs peuvent accéder à une interface conviviale pour modifier leurs informations personnelles.
* Vérifier que les modifications apportées sont correctement enregistrées dans la base de données.
* Vérifier que les utilisateurs reçoivent une confirmation de réussite après la modification de leurs informations personnelles.

### Suppression de Compte Utilisateur

* Vérifier que les utilisateurs peuvent supprimer définitivement leur compte avec succès.
* Vérifier qu'une confirmation est requise avant de supprimer définitivement le compte pour éviter les suppressions accidentelles.
* Vérifier que toutes les données associées au compte sont correctement supprimées de la base de données après la suppression du compte.

## Génération et Distribution de e-tickets

### Consulter les Evénements et Sélectionner des Billets

* Vérifier que les utilisateurs peuvent consulter les événements sportifs disponibles sur le site.
* Vérifier que les détails de chaque événement, y compris la date, l'heure et le lieu, sont correctement affichés.
* Vérifier que les utilisateurs peuvent sélectionner des billets et les ajouter au panier avec succès.

### Générer Automatiquement des e-tickets

* Vérifier que les utilisateurs peuvent finaliser leur achat avec succès.
* Vérifier que des e-tickets sont générés automatiquement après la finalisation de l'achat.
* Vérifier que chaque e-ticket contient des informations précises sur l'événement ainsi qu'un code QR unique pour l'authentification à l'entrée.
