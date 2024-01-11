#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo,
"""
from fabric import task
from datetime import datetime
import os


@task
def do_pack(c):
    source_folder = "web_static"

    if not os.path.exists('versions'):
        os.makedirs('versions')

    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")

    archive_name = f"web_static_{timestamp}.tgz"

    result = c.local(f"tar -czvf versions/{archive_name} {source_folder}")

    if result.failed:
        return None
    else:
        archive_path = f"versions/{archive_name}"
        archive_size = os.path.getsize(archive_path)
        print(f"web_static packed: {archive_path} -> {archive_size}Bytes")
        return archive_path
