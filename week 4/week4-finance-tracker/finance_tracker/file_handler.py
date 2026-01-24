import json, csv, os, shutil, datetime

DATA_FILE = "data/expenses.json"
BACKUP_DIR = "data/backup/"
EXPORT_DIR = "data/exports/"

class FileHandler:

    @staticmethod
    def load():
        try:
            if not os.path.exists(DATA_FILE):
                return []
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except Exception:
            FileHandler.recover_backup()
            return []

    @staticmethod
    def save(data):
        FileHandler.backup()
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def backup():
        os.makedirs(BACKUP_DIR, exist_ok=True)
        if os.path.exists(DATA_FILE):
            name = datetime.datetime.now().strftime("backup_%Y%m%d_%H%M%S.json")
            shutil.copy(DATA_FILE, BACKUP_DIR + name)

    @staticmethod
    def recover_backup():
        backups = sorted(os.listdir(BACKUP_DIR), reverse=True)
        if backups:
            shutil.copy(BACKUP_DIR + backups[0], DATA_FILE)

    @staticmethod
    def export_csv(data):
        os.makedirs(EXPORT_DIR, exist_ok=True)
        path = EXPORT_DIR + "expenses.csv"
        with open(path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
