# 🔧 Documentation Hebdomadaire – Sauvegarde et Réinstallation Système (Semaine du 17 au 23 juin 2025)

## 📅 Semaine concernée :

**Du 17 au 23 juin 2025**

---

## 🎯 Objectif principal

Sauvegarder les utilisateurs `etudiant` et `firecell` depuis une ancienne installation Ubuntu, nettoyer le disque, réinstaller le système, puis restaurer les données.

---

## ✅ Étapes réalisées

### 1. 🎯 Analyse des données à sauvegarder

- Exploration des répertoires `/mnt/oldroot/BACKUP_USERS/etudiant` et `/mnt/oldroot/BACKUP_USERS/firecell`
- Liste des plus gros dossiers :
  ```bash
  sudo du -ah . | sort -rh | head -n 30
  ```
- Décision :
  - Dossiers lourds (`VirtualBox VMs`) déplacés sur un autre PC (\~45 Go)
  - Le reste (\~40 Go) transféré sur une clé USB (64 Go)

### 2. 💾 Sauvegarde des données

#### a. Transfert via USB :

```bash
sudo rsync -av --progress ./ /media/ubuntu/Ventoy/etudiant/
```

- Ajout de l’option `--no-o --no-g` si besoin (droits fichiers)

#### b. Transfert réseau avec rsync :

```bash
rsync -ah --info=progress2 ./VirtualBox\ VMs firecell@10.11.20.109:/home/etudiant/
```

- Problème `Permission denied` corrigé en changeant d’utilisateur

### 3. 🖥️ Réinstallation Ubuntu

- Clé bootable préparée
- Réinstallation propre
- Création des comptes `etudiant` et `firecell`

### 4. 🔁 Restauration des données

#### a. Depuis la clé USB :

```bash
sudo rsync -ah --info=progress2 /media/firecell/Ventoy/etudiant/ /home/etudiant/
```

#### b. Résolution des erreurs de droits :

- Depuis `firecell` :

```bash
sudo usermod -aG sudo etudiant
```

---

## 🧱 Problèmes rencontrés

| Problème rencontré                                 | Solution apportée                           |
| -------------------------------------------------- | ------------------------------------------- |
| `rsync: chown failed: Operation not permitted (1)` | Utilisation de `--no-o --no-g`              |
| `etudiant n’est pas dans le fichier sudoers`       | Ajout au groupe `sudo`                      |
| `Permission denied` lors de la copie dans `/home`  | Lancer rsync avec `sudo` ou bon utilisateur |
| Fichiers trop lourds pour USB                      | Transfert sur autre PC                      |

---

## ✅ Conclusion

- Données critiques sauvegardées ✅
- Système Ubuntu réinstallé avec succès ✅
- Droits utilisateurs restaurés ✅
- Structure et accès aux données fonctionnels ✅

---

## 📦 Suggestions pour la suite

- Supprimer les fichiers temporaires (`.cache`, `.iso`)
- Vérifier les permissions des dossiers importants
- Réinstaller les outils nécessaires (VirtualBox, SSH, etc.)

---

*Rédigé par :* Kopethan *Encadré par :* M. Labiod

