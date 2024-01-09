# coding: utf-8
# copyright by codeskyblue of openATX

import os
import shutil
import tarfile
import tempfile
import zipfile

import requests
from logzero import logger


def get_scrcpy_server() -> str:
    """下载scrcpy文件"""
    download_path = f"vendor/scrcpy-server"
    target_path = f"vendor/scrcpy-server-1.24.zip"
    if not os.path.exists(target_path):
        mirror_download(
            f"https://github.com/Genymobile/scrcpy/releases/download/v1.24/scrcpy-server-v1.24",
            download_path)

        zp = zipfile.ZipFile(target_path, 'a', zipfile.ZIP_STORED)
        zp.write(download_path, arcname="scrcpy-server")
        zp.close()
        os.remove(download_path)
    return target_path


def mirror_download(url: str, target: str) -> str:
    """更换下载镜像源"""
    if os.path.exists(target):
        return target
    github_host = "https://github.com"
    if url.startswith(github_host):
        mirror_url = "http://tool.appetizer.io" + url[len(
            github_host):]  # mirror of github
        try:
            return download(mirror_url, target)
        except (requests.RequestException, ValueError) as e:
            logger.debug("download from mirror error, use origin source")

    return download(url, target)


def download(url: str, storepath: str):
    """下载包文件"""
    target_dir = os.path.dirname(storepath) or "."
    os.makedirs(target_dir, exist_ok=True)

    r = requests.get(url, stream=True)
    r.raise_for_status()
    total_size = int(r.headers.get("Content-Length", "-1"))
    bytes_so_far = 0
    prefix = "Downloading %s" % os.path.basename(storepath)
    chunk_length = 16 * 1024
    with open(storepath + '.part', 'wb') as f:
        for buf in r.iter_content(chunk_length):
            bytes_so_far += len(buf)
            print(f"\r{prefix} {bytes_so_far} / {total_size}",
                  end="",
                  flush=True)
            f.write(buf)
    if total_size != -1 and os.path.getsize(storepath + ".part") != total_size:
        raise ValueError("download size mismatch")
    shutil.move(storepath + '.part', storepath)


if __name__ == "__main__":
    get_scrcpy_server()
