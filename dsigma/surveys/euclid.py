"""Module with functions specific to simulations."""

import numpy as np

__all__ = [
    "default_version",
    "known_versions",
    "e_2_convention",
    "default_column_keys",
]

default_version = "TR1"
known_versions = ["TR1"]
e_2_convention = "standard"


def default_column_keys(version=default_version):
    """Return a dictionary of default column keys.

    Parameters
    ----------
    version : string or None, optional
        Version of the catalog.

    Returns
    -------
    keys : dict
        Dictionary of default column keys.

    Raises
    ------
    ValueError
        If `version` does not correspond to a known catalog version.

    """
    if version == "TR1":
        keys = {
            "ra": "ra",
            "dec": "dec",
            "z": "z",
            "e_1": "e_1",
            "e_2": "e_2",
            "w": "w",
            "w_sys": 1,
        }
    else:
        raise ValueError(
            "Unkown version of simulation. Supported versions are {}.".format(
                known_versions
            )
        )

    return keys
