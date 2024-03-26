# Analyse du Besoin

## Contexte du Projet

InfoEvent, ESN spécialisée dans l'événementiel, a été sélectionnée pour répondre au besoin de la mise en place d'une solution de génération et de distribution de e-tickets pour les JO Paris 2024.

## Nom du Projet

Billeterie JO 2024

## Expression du besoin du client JO France

L'administration des JO ne veut plus de visiteurs munis de billets de nature physique pour diminuer les fraudes et ventes illégales.

Il s'agit alors de mettre en place un système de billeterie électronique sur le site des JO France.

JO France attend que le processus d'achat se déroule de la manière suivante :

- Un visiteur doit se rendre sur le site JO France, où il trouvera différentes offres de billet pour assister aux événements sportifs, à réserver selon le besoin.
- Le visiteur devra s'authentifier pour terminer sa réservation. Il deviendra alors utilisateur par l'authentification et pourra payer pour valider sa commande. 
- Lors d'une journée des JO, chaque billet sera scanné et validé par un employé pour authentifier le billet et s'assurer que la personne en face de lui est bien le titulaire de l'achat.

Notons que les JO France insistent énormément sur la sécurité du compte utilisateur et sur l'authenticité d'un billet.

## Description des Besoins

Les besoins du client JO France peuvent être catégorisés comme suit :

### 1. Génération et Distribution de e-tickets

Le système doit permettre la génération et la distribution de e-tickets pour les différents événements sportifs des JO 2024. Les visiteurs doivent pouvoir consulter les offres de billets disponibles et réserver ceux qui les intéressent.

### 2. Authentification des Utilisateurs

Un processus d'authentification sécurisé est nécessaire pour que les visiteurs puissent finaliser leurs réservations. Cela implique la création de comptes utilisateurs protégés par des identifiants uniques et des mots de passe sécurisés.

### 3. Processus de Réservation

Les visiteurs doivent pouvoir sélectionner les billets désirés et les ajouter à leur panier. Ils doivent également pouvoir spécifier les détails pertinents, tels que le nombre de billets et les dates des événements.

### 4. Paiement Sécurisé

Une passerelle de paiement sécurisée doit être intégrée au système pour permettre aux utilisateurs de régler leurs achats en ligne de manière sûre et fiable.

### 5. Validation des Billets

Chaque billet doit être équipé d'un code ou d'une technologie permettant sa validation lors de l'entrée à un événement. Un processus de scan et de vérification doit être mis en place par le personnel des JO pour garantir l'authenticité des billets et l'identification des détenteurs.

### 6. Sécurité et Authenticité

La sécurité des comptes utilisateurs est une priorité absolue. Des mesures robustes doivent être mises en place pour protéger les données personnelles et financières des utilisateurs. De plus, des mécanismes anti-fraude doivent être intégrés pour prévenir les ventes illégales de billets.

### 7. Tableau de bord analytique

Un tableau de bord analytique doit permettre aux administrateurs de suivre graphiquement l'évolution des ventes et de connaitre en temps réel le chiffre d'affaire des ventes et le nombre de billets encore disponible pour chaque événement sportif.

## Fonctionnalités répondant à ce besoin

### 1. Génération et Distribution de e-tickets

- Affichage des événements sportifs disponibles avec les détails pertinents (date, heure, lieu, etc.).
- Présentation des différents types de billets disponibles (catégories, tarifs, etc.).
- Possibilité de sélectionner des billets et de les ajouter au panier.
- Génération automatique de e-tickets après l'achat.

### 2. Authentification des Utilisateurs

- Création de comptes utilisateurs sécurisés avec des informations personnelles.
- Authentification des utilisateurs lors de la connexion au site ou lors de l'achat de billets.
- Possibilité de récupérer le mot de passe en cas d'oubli.

### 3. Processus de Réservation

- Fonctionnalité de recherche avancée pour trouver des événements spécifiques.
- Filtrage des événements par catégorie, date, lieu, etc.
- Ajout, modification et suppression d'articles dans le panier.
- Récapitulatif clair des articles sélectionnés avant le paiement.

### 4. Paiement Sécurisé

- Intégration d'une passerelle de paiement sécurisée acceptant différentes méthodes de paiement (carte de crédit, PayPal, etc.).
- Cryptage des informations financières lors de la transaction.
- Confirmation de paiement avec un reçu électronique envoyé par e-mail.

### 5. Validation des Billets

- Intégration de codes QR ou de technologies similaires sur les e-tickets.
- Mise en place d'un système de scan des billets à l'entrée des événements.
- Validation instantanée des billets et affichage des détails du titulaire.

### 6. Gestion des Comptes Utilisateurs

- Possibilité pour les utilisateurs de modifier leurs informations personnelles.
- Historique des achats et des réservations consultable pour les utilisateurs.
- Option de désinscription pour supprimer définitivement un compte.

### 7. Gestion des Comptes Administrateurs

- Création d'un compte super administrateur.
- Authentification du compte super administrateur.
- Création de comptes sécurisés administrateurs avec des informations personnelles.
- Authentification des administrateurs lors de la connexion au site.

### 8. Accès au tableau de bord analytique

- Possibilité pour les administrateurs de visualiser le tableau de bord analytique.
- Possibilité pour les administreteurs de créer, modifier et supprimer des offres de vente.

### 9. Sécurité et Prévention des Fraudes

- Protection renforcée des comptes utilisateurs avec des mesures de sécurité avancées (authentification à deux facteurs, etc.).
- Surveillance proactive des activités suspectes et des tentatives de fraude.
- Blocage automatique des comptes en cas de comportement frauduleux.

### 10. Support Client

- Mise en place d'un système de support client accessible par chat en direct, e-mail ou téléphone.
- Assistance pour les problèmes liés à l'achat de billets, à l'authentification, etc.

### 11. Accessibilité

- Conception du site web et de l'interface utilisateur pour une accessibilité optimale (compatibilité avec les lecteurs d'écran, contraste élevé, etc.).

### 12. Internationalisation

- Prise en charge de plusieurs langues pour accueillir les visiteurs du monde entier.
- Adaptation des devises et des options de paiement en fonction de la localisation de l'utilisateur.

## Cas d'utilisation

Les cas d'utilisation suivants représentent les différentes actions que les utilisateurs peuvent entreprendre sur la plateforme de billeterie électronique des Jeux Olympiques de Paris 2024 pour interagir avec le système et accomplir leurs tâches.

### 1. Génération et Distribution de e-tickets

- Consulter les événements sportifs disponibles
- Afficher les détails des événements (date, heure, lieu, etc.)
- Présenter les différents types de billets disponibles
- Sélectionner des billets et les ajouter au panier
- Générer automatiquement des e-tickets après l'achat

### 2. Authentification des Utilisateurs

- Créer un compte utilisateur sécurisé
- Se connecter au compte utilisateur
- Récupérer le mot de passe oublié

### 3. Processus de Réservation

- Rechercher des événements spécifiques
- Filtrer les événements par catégorie, date, lieu, etc.
- Ajouter, modifier ou supprimer des articles dans le panier
- Afficher un récapitulatif des articles sélectionnés avant le paiement

### 4. Paiement Sécurisé

- Choisir une méthode de paiement sécurisée
- Saisir les informations de paiement
- Effectuer le paiement en ligne de manière sécurisée
- Recevoir une confirmation de paiement avec un reçu électronique

### 5. Validation des Billets

- Intégrer des codes QR ou des technologies similaires sur les e-tickets
- Scanner les e-tickets à l'entrée des événements
- Valider instantanément les billets et afficher les détails du titulaire

### 6. Gestion des Comptes Utilisateurs

- Modifier les informations personnelles du compte utilisateur
- Consulter l'historique des achats et des réservations
- Se désinscrire et supprimer définitivement le compte utilisateur

### 7. Gestion des Comptes Administrateurs

- Créer un compte super administrateur
- Se connecter en tant qu'administrateur
- Créer des comptes administrateurs sécurisés
- Se connecter en tant qu'administrateur

### 8. Accès au tableau de bord analytique

- Visualiser le tableau de bord analytique
- Créer, modifier et supprimer des offres de vente depuis le tableau de bord

### 9. Sécurité et Prévention des Fraudes

- Appliquer des mesures de sécurité avancées aux comptes utilisateurs
- Surveiller les activités suspectes et les tentatives de fraude
- Bloquer automatiquement les comptes en cas de comportement frauduleux

### 10. Support Client

- Accéder au système de support client via chat en direct, e-mail ou téléphone
- Recevoir de l'aide pour les problèmes liés à l'achat de billets, à l'authentification, etc.

### 11. Accessibilité

- Concevoir le site web et l'interface utilisateur pour une accessibilité optimale
- Assurer la compatibilité avec les lecteurs d'écran, le contraste élevé, etc.

### 12. Internationalisation

- Prise en charge de plusieurs langues pour l'interface utilisateur
- Adaptation des devises et des options de paiement en fonction de la localisation de l'utilisateur