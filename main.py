"""
Entrance point of the program.
"""

import logging

import fire

from sync_memos import sync_memos

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    fire.Fire(
        {
            "sync_memos": sync_memos,
        }
    )
