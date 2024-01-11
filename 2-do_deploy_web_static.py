#!/usr/bin/python3
"""
Based on the file 1-pack_web_static.py, this script distributes an
archive to the web servers, using the function do_deploy.
"""
from fabric.api import env, put, run, sudo
from os import path

env.hosts = ['54.87.208.50', '100.26.50.175']


def do_deploy(archive_path):
    """Distributes an archive to web servers."""
    if not path.exists(archive_path):
        return False

    try:
        filename = path.basename(archive_path).split(".")[0]
        release_path = f"/data/web_static/releases/{filename}"

        print("Basename", path.basename(archive_path).split(".")[0])
        put(archive_path, "/tmp/")

        run(f"mkdir -p {release_path}")
        run(f"tar -xzf /tmp/{path.basename(archive_path)} -C {release_path}")
        run(f"rm /tmp/{path.basename(archive_path)}")

        sudo(f"mv {release_path}/web_static/* {release_path}/")
        sudo("rm -rf /data/web_static/current")
        sudo(f"ln -s {release_path} /data/web_static/current")
        return True
    except Exception as e:
        return False
