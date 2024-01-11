#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
"""

from datetime import datetime
from fabric.api import *
import os

env.hosts = ["54.87.208.50", "100.26.50.175"]
env.user = "ubuntu"


def do_pack():
    """
        return the archive path if archive has generated correctly.
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


def do_deploy(archive_path):
    """
        Distribute archive.
    """
    if os.path.exists(archive_path):
        archived_file = archive_path[9:]
        newest_version = "/data/web_static/releases/" + archived_file[:-4]
        archived_file = "/tmp/" + archived_file
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(newest_version))
        run("sudo tar -xzf {} -C {}/".format(archived_file,
                                             newest_version))
        run("sudo rm {}".format(archived_file))
        run("sudo mv {}/web_static/* {}".format(newest_version,
                                                newest_version))
        run("sudo rm -rf {}/web_static".format(newest_version))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(newest_version))

        print("New version deployed!")
        return True

    return False


def deploy():
    """Create and distribute an archive to a web server."""
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)
