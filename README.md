# python_intrusion

Collection de scripts Python développés lors du mode Sécurité offensive.

## Organisation

* correction : contient l'ensemble des scripts de Glenn donnés lors de la correction.

Merci de faire un dossier à votre nom et y mettre vos scripts à l'intérieur pour garder l'ensemble organisé.

## Compilation d'un script

```
pip install pyinstaller
# -F : produit un seul fichier
# -w : cache la fenêtre python
# -i : icône du binaire produit
# -n : choix du nom de l'application en sortie
# --clean : nettoyage des fichiers temporaires avant le build de l'application
pyinstaller script.py -F -w -i icone.ico -n app.exe --clean
```
