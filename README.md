# Projet final : prêt pour le feu d'artifices ?

*Projet N°13 - Parcours développeur d'application Python*

## Sujet du projet
Menez un projet numérique de la forme qui vous semblera la plus adaptée (réalisez une application web ; codez un site ou une application mobile…) pour répondre à un besoin autour de vous. Il peut s’agir d’un site de réservation pour l’association de théâtre de votre ville, d’une application pour localiser et référencer les objets trouvés pendant un festival, etc. Prenez le temps de choisir un sujet qui vous touche et pour lequel vous ressentez un véritable besoin.

Le choix du projet s'est porté vers la création d'une application d'inventaire informatique, notamment parce qu'il s'agit d'un besoin professionnel. Cette application est nommée pour le projet, ***OC-Inventory***.

## Structure de l'application
Le but de cette application et de pouvoir suivre le matériel informatique au sein d'une entreprise. L'intérêt est donc de pouvoir facilement identifier un périphérique et de savoir à quel utilisateur il est assigné. Il faut également pouvoir rechercher un utilisateur et identifier tous les périphériques en sa possession.

L'application est, évidemment, développée en **Python** en utilisant notamment le **framework Django**. Un template Boostrap a été intégré à l'application. **HTML5**, **CSS3** et **Boostrap5** ont été utilisés durant le développement, entre autres, pour la gestion de la partie graphique de l'application. **JavaScript** est également utilisé pour l'intégration de différents éléments du **Dashboard** notamment.
Différentes ressources graphiques ont été utilisées, elles proviennent principalement de [**Fontawesome.com**](https://fontawesome.com/icons) et [**Icomoon.io**](https://icomoon.io/).

Lors de l'ouverture de l'application, l'utilisateur se retrouve sur la page d'accueil dans laquelle il est expliqué la nécessité de s'authentifier pour utiliser l'application.

 * **Users** :
L'utilisateur est invité à s'enregistrer puis une fois le formulaire saisie et valide, une notification lui indique de valider son inscription en cliquant sur le lien reçu à l'adresse mail indiquée dans le formulaire. Une fois cette action effectuée, le compte est activé et l'utilisateur peut maintenant se connecter à l'application. Cette fonctionnalité est parfaitement intégrée à Django et se met facilement en place. Elle permet notamment de vérifier aisément qu'un utilisateur est connecté et d'interagir avec le modèle **User** (intégré par défaut dans ***Django***). Dans le projet, cette partie est traitée par l'application **Users**.

* **Product** :
Cette application intègre la gestion de l'index de notre application, les mentions ainsi que le formulaire de contact ("*Contact_Us*"). Dans l'index nous retrouvons un "mini-dashboard" intégrant dans un tableau les derniers périphériques enregistrés dans la base, ainsi que des graphiques détaillant la répartition des périphériques par marque et type sur le parc informatique.

* **Product User** :
L'application **Product User** est en quelque sorte le coeur du projet. C'est ici que sont gérées toutes les parties faisant références aux périphériques, catégories, marques, etc… Une fois l'utilisateur authentifié, il a la possibilité de consulter l'état du parc informatique mais également de rechercher un périphérique. Une fois le périphérique sélectionné, il a la possibilité de consulter sa fiche, détaillant les informations techniques et administratives, mais également la possibilité de savoir qui est l'utilisateur associé à celui-ci. D'ailleurs, il est tout à fait possible de rechercher des utilisateurs plutôt que des périphériques. On peut alors consulter la fiche de l'utilisateur qui indique également les différents périphériques en sa possession.
Une rubrique nommée "**Nouveau périphérique**" permet également d'ajouter un nouveau périphérique à la base de données, puis de l'attribuer ensuite à un utilisateur (si les droits sur l'application le permettent).

* **Dashboard** :
L'application **Dashboard** a également une place importante dans l'utilisation de l'application. Elle est composée de plusieurs "*cartes*" ayant pour but d'indiquer l'état du parc informatique. On peut en effet rapidement connaitre, le nombre total de périphériques enregistrés, la répartition des périphériques par entité/service ou encore les types de systèmes d'exploitation présents sur le parc informatique etc... Cela permet en un coup d'oeil, d'avoir une idée de l'état général du parc. Et si nous n'y trouvons pas l'information recherchée, nous avons la possibilité d'effectuer des recherches précises dans la partie "*Recherche avancée*" de l'application, avec la possibilité de faire des recherches sous différents critères et également de les affiner en utilisant les filtres.

* **Remplissage de la base de données** :
`python manage.py fill_main_db (num)`
Pour fonctionner, l'application exploite une base de données (**PostgreSQL**), dont un script de remplissage, nommé "*fill_main_db.py*", permet de fournir les différentes tables de la base de données. Ce script a été intégré en tant que commande de *manage.py*, il peut donc être appelé de la façon suivante : 
L'argument "*num*" permet de spécifier le nombre de périphériques que nous souhaitons intégrer depuis les différentes **API**. En effet, les différentes informations de notre base proviennent de différentes sources extérieures à l'application. Dans notre cas, un outil nommé **OCS Inventory** récolte les informations "techniques" des différents périphériques et une base administrative nommée "**Immo**" fait le lien entre le périphérique (Serial number) et le numéro de bon de commande, date d'acquisition, entité etc... Concernant l'utilisateur du périphérique, nous interrogeons un annuaire. 
Bien évidemment, il est tout à fait possible de l'adapter à n'importe quel source d'information et donc structure, l'important étant d'adapter les scripts en conséquence.

## Installation de l'application
Pour la mise en place du projet, il est recommandé de créer un  **environnement virtuel python**. Les commandes ci-dessous sont à adapter selon le système d'exploitation utilisé. Il faut également avoir préalablement installé les dépendances éventuellement nécessaires.

A savoir que le projet a été testé sur des versions  **3.8**, **3.9** et **3.10** de **Python**. Il est donc recommandé de créer un environnement virtuel basé sur une version compatible.
1.  **Installation de l'environnement virtuel**  :    
    ```
     Python -m venv (nom_environnement)
    ```
    
2.  **Clonage du projet à l'intérieur de l'environnement virtuel**  :
    ```
     Git clone git@github.com:Eidocode/OC_Project13.git
    ```
    
3.  **Activation de l'environnement virtuel depuis la racine (à adapter selon l'OS)**  :
    ```
     ./Scripts/activate
    ```
    
4.  **Installation des dépendances**  :    
    ```
     pip install -r requirements.txt    
    ```
     
5.  **Configuration de l'application**  :    
Pour fonctionner, l'application utilise des variables d'environnement qui sont appelées dans le fichier de configuration du projet [**settings**](https://github.com/Eidocode/OC_Project13/blob/main/inventory/settings/__init__.py). Une première variable **['SECRET_KEY']** doit être générée aléatoirement et liée uniquement à l'installation en cours du projet. Il est indispensable que cette clé ne soit pas visible ou facilement accessible. 
Une autre variable **['ENV']** aura comme valeur '***PRODUCTION***' si le déploiement a lieu sur un serveur de production. Cela dans le but d'avoir un seul fichier de configuration quelque soit le type d'environnement dans lequel l'application est installée.

6.  **Execution de l'environnement Django**  :
    ```
     python manage.py runserver
    ```
    L'application  **Django**  est alors exécutée. Il ne reste qu'à ouvrir un navigateur et se rendre à l'adresse  **ip_du_serveur:8000**.

## Déploiement de l'application

L'application a été déployée sur la plateforme d'hébergement  **DigitalOcean**, nous pouvons la retrouver à l'adresse suivante :  [**http://oc-inventory.ovh/**](http://oc-inventory.ovh/)

Pour effectuer ce déploiement, il est nécessaire de suivre la documentation de l'hébergeur souhaité.
Une [**documentation Django**](https://docs.djangoproject.com/fr/4.2/howto/deployment/checklist/) très complète existe également et détaille certains aspects très importants.

Il est également indispensable d'utiliser des variables d'environnements que ce soit par l'intermédiaire de l'interface graphique de l'hébergeur ou directement dans le système d'exploitation du serveur. Les valeurs de ces variables ne doivent jamais apparaitre dans les fichiers de l'application. Que ce soit dans le code ou les fichiers de configuration de l'application.

Comme indiqué précédemment, ces variables d'environnement sont appelées dans le fichier  **[settings](https://github.com/Eidocode/OC_Project13/blob/main/inventory/settings/__init__.py)** de l'application, de la façon suivante :

```
    import os
    
    SECRET_KEY = os.environ['SECRET_KEY']
    ENV = os.environ.get('ENV')
```