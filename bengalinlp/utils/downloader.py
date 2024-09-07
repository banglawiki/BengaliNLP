"""Module providing functions for downloading models."""

import os
import shutil
from typing import Optional, Union, Tuple
from urllib.parse import urlparse
import requests
from tqdm.auto import tqdm
from bengalinlp import ZipFile
from bengalinlp.utils.config import ModelInfo


def _create_dirs(model_name: str) -> str:
    """Create directories for downloading models.

    Args:
        model_name (str): Name of the model.

    Returns:
        str: Absolute path where the model can be downloaded.
    """
    model_dir = os.path.join(os.path.expanduser("~"), "bengalinlp", "models")
    os.makedirs(model_dir, exist_ok=True)
    model_path = os.path.join(model_dir, model_name)
    return model_path


def _unzip_file(zip_file_path: str, unzip_dir: Optional[str] = None) -> None:
    """Extract a .zip archive.

    Args:
        zip_file_path (str): Path of the archive to be extracted.
        unzip_dir (Optional[str]): Directory where the archive will be extracted. Defaults to None, which means the same directory as the zip file.

    Raises:
        zip_error: Error from ZipFile module.
    """
    if unzip_dir is None:
        unzip_dir = os.path.dirname(zip_file_path)

    op_desc = f"Extracting: {os.path.basename(zip_file_path)}"
    try:
        with ZipFile(file=zip_file_path) as zip_file:
            for member_name in tqdm(zip_file.namelist(), desc=op_desc):
                file_name = os.path.basename(member_name)
                if file_name:
                    target_path = os.path.join(unzip_dir, file_name)
                    with zip_file.open(member_name) as source_file, open(
                        target_path, "wb"
                    ) as target_file:
                        shutil.copyfileobj(source_file, target_file)
        os.remove(zip_file_path)
    except Exception as zip_error:
        # Clean up any partial extraction
        zip_file_str = os.path.splitext(os.path.basename(zip_file_path))[0]
        for file_name in os.listdir(unzip_dir):
            if zip_file_str in file_name:
                os.remove(os.path.join(unzip_dir, file_name))
        raise zip_error


def _download_file(file_url: str, file_path: str) -> str:
    """Download a file from a URL.

    Args:
        file_url (str): URL of the file.
        file_path (str): Path where the file will be downloaded.

    Returns:
        str: Path where the file is downloaded.

    Raises:
        network_error: Download related error.
    """
    if os.path.exists(file_path):
        return file_path

    op_desc = f"Downloading {os.path.basename(file_path)}"
    try:
        with requests.Session() as req_sess:
            req_res = req_sess.get(file_url, stream=True)
            total_length = int(req_res.headers.get("Content-Length", 0))
            with tqdm.wrapattr(
                req_res.raw, "read", total=total_length, desc=op_desc
            ) as raw:
                with open(file_path, "wb") as file:
                    shutil.copyfileobj(raw, file)
        return file_path
    except Exception as network_error:
        if os.path.exists(file_path):
            os.remove(file_path)
        raise network_error


def _download_zip_model(model_url: str, model_path: str) -> str:
    """Download and extract a model archive.

    Args:
        model_url (str): URL of the model.
        model_path (str): Path where the model will be downloaded.

    Returns:
        str: Path where the model is extracted after downloading.
    """
    if os.path.exists(model_path):
        return model_path

    extract_dir = os.path.dirname(model_path)
    url_model_name = os.path.basename(urlparse(model_url).path)
    tmp_zip_file_path = os.path.join(extract_dir, url_model_name)
    _download_file(model_url, tmp_zip_file_path)
    _unzip_file(tmp_zip_file_path, extract_dir)
    return model_path


def download_model(name: str) -> str:
    """Download and extract a model if necessary.

    Args:
        name (str): Name of the model.

    Returns:
        str: Path where the model is downloaded or extracted.
    """
    model_name, model_type, model_url = ModelInfo.get_model_info(name)
    model_path = _create_dirs(model_name)

    if model_type == "single":
        model_path = _download_file(model_url, model_path)
    elif model_type == "zip":
        model_path = _download_zip_model(model_url, model_path)
    else:
        print(f"Model type {model_type} not yet implemented")
        model_path = ""

    return model_path


def download_all_models() -> None:
    """Download and extract all available models for BengaliNLP."""
    model_keys = ModelInfo.get_all_models()
    for model_key in model_keys:
        download_model(model_key)
