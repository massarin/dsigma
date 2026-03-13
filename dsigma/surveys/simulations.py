"""Module with functions specific to simulations."""

import numpy as np

__all__ = [
    "default_version",
    "known_versions",
    "e_2_convention",
    "default_column_keys",
    "tomographic_redshift_bin",
    "multiplicative_shear_bias",
    "selection_response",
]

default_version = "HAGN"
known_versions = ["flagship", "HAGN"]
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
    if version == "flagship":
        keys = {
            "ra": "ra_mag_gal",
            "dec": "dec_mag_gal",
            "z_true": "observed_redshift_gal",
            "e_1": "gamma1",
            "e_2": "gamma2",
            "w": 1,
        }
    elif version == "HAGN":
        keys = {
            "ra": "RA_IMG",
            "dec": "DEC_IMG",
            "z": "z_true",
            "e_1": "GAMMA1",
            "e_2": "GAMMA2",
            "w": 1,
            "w_sys": 1,
        }
    else:
        raise ValueError(
            "Unkown version of simulation. Supported versions are {}.".format(
                known_versions
            )
        )

    return keys


def tomographic_redshift_bin(
    z_s, z_bins=[0.2, 0.43, 0.63, 0.9, 1.3], version=default_version
):
    """Return the photometric redshift bin.

    Parameters
    ----------
    z_s : numpy.ndarray
        Photometric redshifts.
    version : string, optional
        Which catalog version to use.

    Returns
    -------
    z_bin : numpy.ndarray
        The tomographic redshift bin corresponding to each photometric
        redshift. Returns -1 in case a redshift does not fall into any bin.

    Raises
    ------
    ValueError
        If the `version` does not correspond to a known catalog version or
        if tomographic bins were not assigned based on photometric redshifts
        for the given catalog version.

    """
    if version == "flagship" or version == "HAGN":
        pass
    else:
        raise ValueError(
            "Unkown version of simulation. Supported versions are {}.".format(
                known_versions
            )
        )

    z_bin = np.digitize(z_s, z_bins) - 1
    z_bin = np.where(
        (z_s < np.amin(z_bins)) | (z_s >= np.amax(z_bins)) | np.isnan(z_s), -1, z_bin
    )

    return z_bin
