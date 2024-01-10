#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo.
"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.

    Returns:
        Archive path if successfully generated, otherwise None.
    """
    if not os.path.exists('versions'):
        os.makedirs('versions')

    archive_name = "web_static_{}.tgz".format(
        datetime.now().strftime("%Y%m%d%H%M%S")
    )
    print("Packing web_static to versions/{}".format(archive_name))
    result = local("tar -cvzf versions/{} web_static".format(archive_name))

    if result.failed:
        return None
    else:
        archive_path = f"versions/{archive_name}"
        archive_size = os.path.getsize("./versions/{}".format(archive_name))
        print(f"web_static packed: {archive_path} -> {archive_size}Bytes")
        return archive_path
