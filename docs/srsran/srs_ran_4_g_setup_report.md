# 📅 Rapport hebdomadaire – srsRAN 4G avec EPC (Semaine à compléter)

## 🎯 Objectif de la semaine

- Installer, compiler et tester `srsRAN_4G` localement
- Configurer un core LTE (`srsepc`) et lancer un eNodeB (`srsenb`)
- Connecter un smartphone Android via carte SIM
- Diagnostiquer les problèmes de connexion

---

## 🧪 Étapes réalisées

### 1. Clonage et compilation de `srsRAN_4G`
```bash
git clone https://github.com/srsran/srsRAN_4G.git
cd srsRAN_4G && mkdir build && cd build
cmake .. && make -j$(nproc)
sudo make install
srsran_install_configs.sh user
```
📌 **Résultat** : Compilation réussie, mais le binaire `srsepc` est introuvable

### 2. Tentatives de correction

- Nettoyage + recompilation avec `ENABLE_EPC=ON`
- Tests sur plusieurs branches : `main`, `release_23_11`, `release_22_10`
- Vérification des chemins (`/usr/local/bin`, `build/src/srsepc/`)
- Installation des dépendances système :
```bash
sudo apt install libboost-all-dev libsctp-dev libconfig++-dev libssl-dev
```
- Compilation ciblée :
```bash
make srsepc
```
📌 **Résultat** : Aucun exécutable `srsepc` généré

### 3. Test avec dépôt `srsRAN_project`

- Cloné : `https://github.com/srsran/srsRAN_project.git`
- Compilation + installation → **succès affiché dans les logs**
- ⚠️ Mais toujours **aucun fichier `srsenb` ou `srsepc`** trouvé sur le disque

---

## 🛑 Problèmes rencontrés

- Compilation réussie mais fichiers absents
- Incohérences entre les logs de build et les fichiers réels
- Hypothèse : modules désactivés ou incompatibilité avec Ubuntu 24.04

---

## ✅ Conclusion

- 🔹 `srsepc` introuvable malgré l’activation du module EPC
- 🔹 Aucun fichier utilisable pour tester la chaîne radio

---

## 📌 Prochaine étape recommandée

- Revenir sur une version stable : **Ubuntu 20.04 + dépôt srsLTE**
- Tester un setup **Docker stable (OpenAirInterface ou FireCell)**
- Objectif : pouvoir lancer eNB + EPC et tester une vraie SIM avec USRP ou Quectel

---

*Rédigé par :* Kopethan  
*Encadré par :* M. Labiod

