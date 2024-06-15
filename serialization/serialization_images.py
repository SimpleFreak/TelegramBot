from user_data import UserData

from pydantic import ValidationError

import json
import os
from datetime import datetime


def get_user_data(fullname: str, theme: str, photo: str,
                  upload_date=datetime.now().strftime('%Y-%m-%d %H:%M:%S')):
    try:
        user = UserData(full_name=fullname, photo_name=photo,
                        upload_date=upload_date)
    except ValidationError as exception:
        print(exception.errors())
        print(exception.json())

    json_data = json.dumps(user.__dict__, indent=4, separators=(", ", ": "))

    save_directory = f"json/{theme}/{fullname}"

    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    file_name = f"{fullname}.json"
    file_path = f"{save_directory}/{file_name}"

    with open(file_path, "w") as file:
        file.write(json_data)
