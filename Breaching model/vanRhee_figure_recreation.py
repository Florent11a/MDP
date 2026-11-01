"""
Reproduction of Fig. 3 style from van Rhee & Bezuijen (1998):
toe slope ratio (1:n) vs. active wall height B.
"""

import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass


@dataclass
class SoilParams:
    D50: float = 135e-6                 # [m] grain size (van Rhee 135um case)
    phi_deg: float = 22.0               # [deg] friction angle (what does van Rhee use? 35 deg?)
    n0: float = 0.40
    n1: float = 0.47
    rho_s: float = 2650.0               # [kg/m3] sand
    rho_w: float = 1000.0               # [kg/m3] water
    g: float = 9.81                     # [m/s2] gravity
    nu: float = 1.004e-6                # [m2/s] kinematic viscosity of water at 20C
    empirical_coeff: float = 0.0049     # Eq. 5 coefficient
    d15_factor: float = 0.75            # factor to estimate d15 from D50
    vw_factor: float = 0.8               # factor to adjust active wall velocity (Eq. 3)

    def active_wall_velocity(self) -> float:
        """Eq. 3: v_w = (k/delta_n) * Delta * (1-n0) * cot(phi)"""
        d15 = self.D50 * self.d15_factor # well-sorted sand approximation?
        k = (self.g / (160 * self.nu)) * d15**2 * (self.n0**3 / (1 - self.n0)**2)  # Eq. 7
        delta_n = (self.n1 - self.n0) / (1 - self.n1)                              # Eq. 4
        Delta = (self.rho_s - self.rho_w) / self.rho_w
        return (k / delta_n) * Delta * (1 - self.n0) / np.tan(np.radians(self.phi_deg)) * self.vw_factor


def slope_angle_at_toe(B: float, soil: SoilParams) -> float:
    """Eq. 5+6: beta(B), returned in degrees."""
    s = soil.active_wall_velocity() * B * (1 - soil.n0) * soil.rho_s   # Eq. 6
    D50_microm = soil.D50 * 1e6
    i = soil.empirical_coeff * (D50_microm ** 0.92) * (s ** -0.39)     # Eq. 5
    i = np.clip(i, np.tan(np.radians(1.0)), np.tan(np.radians(89.0)))
    return np.degrees(np.arctan(i))


def slope_ratio_n(angle_deg):
    """Convert angle from horizontal [deg] to slope ratio 1:n (n = cot(angle))."""
    return 1.0 / np.tan(np.radians(np.clip(angle_deg, 1e-3, 90.0)))


# --- Compute and plot ---
soil_135micron = SoilParams()
soil_225micron = SoilParams(D50=225e-6)

B_vals = np.linspace(0.01, 10, 500)

n_vals_135 = np.array([slope_angle_at_toe(B, soil_135micron) for B in B_vals])  # mathematical curve based on paper equations in degrees
n_vals_135[n_vals_135 >= soil_135micron.phi_deg] = soil_135micron.phi_deg       # equation curve limited to friction angle of soil 
n_vals_135 = slope_ratio_n(n_vals_135)                                          # convert to slope ratio 1:n

n_vals_225 = np.array([slope_angle_at_toe(B, soil_225micron) for B in B_vals])
n_vals_225[n_vals_225 >= soil_225micron.phi_deg] = soil_225micron.phi_deg
n_vals_225 = slope_ratio_n(n_vals_225)

fig, ax = plt.subplots(figsize=(7, 6))

ax.plot(B_vals, n_vals_135, color='r', lw=1.5, label='D50 = 135 μm')
ax.plot(B_vals, n_vals_225, color='k', lw=1.5, label='D50 = 225 μm')

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_xticks(np.arange(0, 11, 1))
ax.set_yticks(np.arange(0, 11, 1))
ax.set_xlabel('Active Wall Height [m]')
ax.set_ylabel('Slope Angle  1:n')
ax.set_title(f'n0 = {soil_135micron.n0}, n1 = {soil_135micron.n1}, φ = {soil_135micron.phi_deg}°, d15 factor = {soil_135micron.d15_factor}, vw factor = {soil_135micron.vw_factor}', fontsize=10)
ax.legend(loc='upper left', frameon=True, fontsize=10)
ax.grid(True, ls='--', alpha=0.6)
plt.tight_layout()
plt.savefig('vanRhee_reproduction.png', dpi=150)
plt.show()
