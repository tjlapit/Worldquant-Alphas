from ace_lib import ace
import json
import os

ALPHA_DIR = "alphas"

def load_alphas():
    alphas = []
    for file in os.listdir(ALPHA_DIR):
        if file.endswith(".json"):
            with open(os.path.join(ALPHA_DIR, file), "r") as f:
                alphas.append(json.load(f))
    return alphas

def run_simulations():
    alphas = load_alphas()
    print(f"Running {len(alphas)} simulations")

    for alpha in alphas:
        print(f"Simulating: {alpha['name']}")
        ace.simulate(alpha)

if __name__ == "__main__":
    run_simulations()
