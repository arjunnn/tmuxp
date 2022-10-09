import argparse
import os
import typing as t

from .constants import VALID_CONFIG_DIR_FILE_EXTENSIONS
from .utils import get_config_dir


def create_ls_subparser(
    parser: argparse.ArgumentParser,
) -> argparse.ArgumentParser:
    return parser


def command_ls(
    parser: t.Optional[argparse.ArgumentParser] = None,
):
    tmuxp_dir = get_config_dir()
    if os.path.exists(tmuxp_dir) and os.path.isdir(tmuxp_dir):
        for f in sorted(os.listdir(tmuxp_dir)):
            stem, ext = os.path.splitext(f)
            if os.path.isdir(f) or ext not in VALID_CONFIG_DIR_FILE_EXTENSIONS:
                continue
            print(stem)
