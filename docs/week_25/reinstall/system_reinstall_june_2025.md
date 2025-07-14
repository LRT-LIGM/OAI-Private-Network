# Weekly Documentation – System Backup and Reinstallation (Week of June 17–23, 2025)

## Week Covered:

**From June 17 to June 23, 2025**

---

## Main Objective

Back up the `etudiant` and `firecell` users from an old Ubuntu installation, clean the disk, reinstall the system, then restore the data.

---

## Steps Completed

### 1. Data Analysis Before Backup

* Explored the directories:
  `/mnt/oldroot/BACKUP_USERS/etudiant` and `/mnt/oldroot/BACKUP_USERS/firecell`
* Listed largest folders:

  ```bash
  sudo du -ah . | sort -rh | head -n 30
  ```
* Decisions:

  * Heavy folders (`VirtualBox VMs`) moved to another PC (\~45 GB)
  * Remaining data (\~40 GB) transferred to a 64 GB USB drive

### 2. Data Backup

#### a. USB Transfer:

```bash
sudo rsync -av --progress ./ /media/ubuntu/Ventoy/etudiant/
```

* Added `--no-o --no-g` if needed (file permission issues)

#### b. Network Transfer via rsync:

```bash
rsync -ah --info=progress2 ./VirtualBox\ VMs firecell@10.11.20.109:/home/etudiant/
```

* `Permission denied` error solved by switching to the correct user

### 3. Ubuntu Reinstallation

* Bootable USB key prepared
* Clean installation performed
* Created `etudiant` and `firecell` user accounts

### 4. Data Restoration

#### a. From USB drive:

```bash
sudo rsync -ah --info=progress2 /media/firecell/Ventoy/etudiant/ /home/etudiant/
```

#### b. Fixing Permissions:

* From `firecell` user:

```bash
sudo usermod -aG sudo etudiant
```

---

## Issues Encountered

| Issue                                              | Solution Provided                          |
| -------------------------------------------------- | ------------------------------------------ |
| `rsync: chown failed: Operation not permitted (1)` | Used `--no-o --no-g`                       |
| `etudiant is not in the sudoers file`              | Added to the `sudo` group                  |
| `Permission denied` when copying to `/home`        | Used `sudo` or the correct user with rsync |
| Files too large for USB transfer                   | Used another PC for transfer               |

---

## Conclusion

* Critical data successfully backed up ✅
* Ubuntu system reinstalled successfully ✅
* User permissions restored ✅
* Data structure and access functional ✅

---

## Suggestions Going Forward

* Delete temporary files (`.cache`, `.iso`, etc.)
* Check folder permissions
* Reinstall necessary tools (VirtualBox, SSH, etc.)

---

*Written by:* Kopethan
*Supervised by:* Mr. Labiod

---
