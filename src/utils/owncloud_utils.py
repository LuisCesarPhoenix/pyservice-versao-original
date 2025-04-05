import owncloud
from src.config.settings import OWNCLOUD_URL, OWNCLOUD_USER, OWNCLOUD_PASS, WORK_DIR, FINALIZED_DIR

def connect_owncloud():
    oc = owncloud.Client(OWNCLOUD_URL)
    oc.login(OWNCLOUD_USER, OWNCLOUD_PASS)
    return oc

def download_file(file_path):
    oc = connect_owncloud()
    local_path = f"{WORK_DIR}{file_path}"
    oc.get_file(f"{WORK_DIR}{file_path}", local_path)
    return local_path

def upload_file(local_path, remote_path):
    oc = connect_owncloud()
    oc.put_file(f"{FINALIZED_DIR}{remote_path}", local_path)
