import matplotlib.pyplot as plt
import atlas_mpl_style as ampl

ampl.use_atlas_style(usetex=False)

x_mass = [
    5,
    7,
    9,
    11,
    13,
    15,
    17,
    19,
    23,
    27,
    31,
    35,
    39,
    42,
    45,
    48,
    51,
    54,
    57,
    60,
    63,
    66,
    69,
    72,
    75,
]
limit_3sigma = [
    0.00399804,
    0.003579603,
    0.003205793,
    0.003022748,
    0.002887032,
    0.002950174,
    0.003330216,
    0.003332242,
    0.00461788,
    0.005605542,
    0.006418881,
    0.009847898,
    0.013009986,
    0.01491775,
    0.017223378,
    0.018619195,
    0.020850975,
    0.029121828,
    0.041606548,
    0.063259227,
    0.096375198,
    0.131566792,
    0.17576541,
    0.200502527,
    0.225521115,
]
limit_2sigma = [
    0.003979482,
    0.00344226,
    0.003147143,
    0.003021182,
    0.00284535,
    0.002938525,
    0.00328705,
    0.003250518,
    0.004609637,
    0.005490398,
    0.006506959,
    0.009916452,
    0.012653611,
    0.015435809,
    0.016442772,
    0.018133999,
    0.020902835,
    0.028906354,
    0.041528273,
    0.063146003,
    0.095181988,
    0.135387996,
    0.176572817,
    0.208996401,
    0.227103782,
]
limit_1p5sigma = [
    0.004039859,
    0.003458726,
    0.00317017,
    0.003026576,
    0.002833254,
    0.003048457,
    0.003220197,
    0.003290241,
    0.004618977,
    0.005479031,
    0.00638543,
    0.009462891,
    0.012375576,
    0.014815125,
    0.016892575,
    0.018372789,
    0.020264597,
    0.029341109,
    0.040961735,
    0.063488348,
    0.096900958,
    0.133622926,
    0.178524398,
    0.212635397,
    0.233461519,
]


fig, ax = plt.subplots()
ax.plot(x_mass, limit_3sigma, label="$\pm3\sigma$")
ax.plot(x_mass, limit_2sigma, label="$\pm2\sigma$")
ax.plot(x_mass, limit_1p5sigma, label="$\pm1.5\sigma$")
ax.set_title("limit curve with different fitting mass window")
ax.set_xlabel("mass [GeV]]")
ax.set_ylabel("coupling limit g")
ax.set_ylim(0.001, 10)
ax.set_yscale('log')
ax.legend(loc="upper right")
ampl.plot.draw_atlas_label(0.05, 0.95, ax=ax, status="wip", energy="13 TeV", lumi=139)
fig.savefig("limit_different_window.png")