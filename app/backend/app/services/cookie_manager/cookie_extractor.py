import os
import shutil
import sqlite3

from encryption_data import *
from decryptor import *


def cookie_extractor():
    # local sqlite Chrome cookie database path
    db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                            "Google", "Chrome", "User Data", "Default", "Network", "Cookies")

    # copy the file to config to override chrome lock
    filename = os.path.join("app", "config", "Cookies.db")

    if not os.path.isfile(filename):
        # copy file when does not exist in the current directory
        shutil.copyfile(db_path, filename)

    # connect to the database
    db = sqlite3.connect(filename)

    # ignore decoding errors
    db.text_factory = lambda b: b.decode(errors="ignore")
    cursor = db.cursor()

    # get the cookies from `cookies` table
    cursor.execute("""
                        SELECT host_key, name, value, creation_utc, last_access_utc, expires_utc, encrypted_value 
                        FROM cookies
                        WHERE host_key like '%skyscanner%'
                    """)
 
    # get the AES key
    key = get_encryption_key()
    cookies = {"cookies": []}
    for host_key, name, value, creation_utc, last_access_utc, expires_utc, encrypted_value in cursor.fetchall():
        if not value:
            decrypted_value = decrypt_data(encrypted_value, key)
        else:
            # already decrypted
            decrypted_value = value
        
        cookie = {
        "domain": host_key,
        "name": name,
        "value": decrypted_value,
        "expires": expires_utc,
        "path": "/",
        "httpOnly": "true",
        "secure": "false",
        "session": "true"
        }

        cookies["cookies"].append(cookie)

        # update the cookies table with the decrypted value
        # and make session cookie persistent
        cursor.execute("""
        UPDATE cookies SET value = ?, has_expires = 1, expires_utc = 99999999999999999, is_persistent = 1, is_secure = 0
        WHERE host_key = ?
        AND name = ?""", (decrypted_value, host_key, name))

    # commit changes
    db.commit()
    # close connection
    db.close()

    # Export to json
    cookies_location = os.path.join("app", "config", "cookies.json")
    
    with open(cookies_location, "w") as outfile:
        json.dump(cookies, outfile)

if __name__ == "__main__":
    cookie_extractor()
