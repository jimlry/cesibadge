# cesibadge

**Installation de pip**
```
sudo apt-get install python-pip
```

**Installation de virtualenv pour créer un environnement de développement isolé**
```
sudo pip install virtualenv
```

**Création d'un environnement de développement custom**
```
cd admin
virtualenv venv
```

**Activation de l'environnement virtuel**
```
. venv/bin/activate
```

**Installation des dépendances du projet**
```
python setup.py develop
```

**Configuration des variables d'environnement et lancement du serveur**
```
sh run.sh
```

**Désactivation de l'environnement virtuel**
```
deactivate
```
