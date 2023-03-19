import jax.numpy as jnp
from pyNA.src.noise_model.python.propagation.compute_direct_propagation import compute_direct_propagation
from pyNA.src.noise_model.python.propagation.compute_atmospheric_absorption import compute_atmospheric_absorption
from pyNA.src.noise_model.python.propagation.compute_ground_effects import compute_ground_effects
from pyNA.src.noise_model.python.utils.compute_msap_subbands import compute_msap_subbands


def compute_propagation_effects(msap_source, x, y, z, r, c_bar, rho_0, I_0, beta, x_mic, f_sb, settings, aircraft, tables):

    # Apply spherical spreading and characteristic impedance effects to the MSAP
    # Source: Zorumski report 1982 part 1. Chapter 5.1 Equation 1
    if settings['direct_propagation']:
        msap_prop = compute_direct_propagation(msap_source=msap_source, r=r, I_0=I_0, settings=settings)
    else:
        msap_prop = msap_source

    # Generate msap sub-bands
    if settings['absorption'] or settings['ground_effects']:
        msap_sb = compute_msap_subbands(msap_in=msap_prop, settings=settings)

        if settings['absorption']:
            msap_sb = compute_atmospheric_absorption(msap_sb, r, z, f_sb, settings, tables)

        if settings['ground_effects']:
            msap_sb = compute_ground_effects(msap_sb)

    

    return msap_prop