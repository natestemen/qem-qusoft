import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.1, 2.5, 500)

classical_runtime = np.exp(x ** 2)
quantum_error_mitigation = np.exp(0.9 * x) + 0.2
quantum_error_correction = 0.5 * x + 6

qem_is_lowest = (quantum_error_mitigation < classical_runtime) & (quantum_error_mitigation < quantum_error_correction)

fig, ax = plt.subplots(figsize=(6, 4), facecolor="none")
ax.set_facecolor("none")  # Ensure full transparency

ax.plot(x, classical_runtime, label="Classical", color="#ff67ff", linewidth=2)  # pink
ax.plot(x, quantum_error_mitigation, label="QEM", color="#FFA500", linewidth=2)  # orange
ax.plot(x, quantum_error_correction, label="QEC", color="#02b875", linewidth=2)  # green

# QEM-feasible region
ax.fill_between(x, 0, quantum_error_mitigation, where=qem_is_lowest, color="#FFA500", alpha=0.2)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

axis_color = "#efefef"
ax.spines['left'].set_color(axis_color)
ax.spines['bottom'].set_color(axis_color)
ax.spines['left'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)

ax.set_xticks([])
ax.set_yticks([])

ax.set_xlabel("Quantum Circuit Complexity", fontsize=12, color=axis_color)
ax.set_ylabel("Runtime", fontsize=12, color=axis_color)

legend = ax.legend(fontsize=10, frameon=False)
for text in legend.get_texts():
    text.set_color(axis_color)

ax.set_xlim(0.4, 2.5)
ax.set_ylim(0, 10)

fig.savefig("assets/runtime_vs_complexity_highlight.svg", format="svg", transparent=True)

plt.show()
