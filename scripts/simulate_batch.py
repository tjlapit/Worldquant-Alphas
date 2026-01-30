import json
import os
from ace_lib import ace

ALPHA_DIR = "alphas"

def load_alpha_files():
    alphas = []

    for filename in os.listdir(ALPHA_DIR):
        if filename.endswith(".json"):
            path = os.path.join(ALPHA_DIR, filename)
            with open(path, "r", encoding="utf-8") as f:
                alphas.append(json.load(f))

    return alphas


def simulate_alpha(session, alpha):
    """
    Submit one alpha to WorldQuant BRAIN
    """
    expression = alpha["expression"]

    print(f"Submitting: {alpha.get('name')}")

    alpha_id = session.simulate(
        expression=expression,
        region=alpha["region"],
        universe=alpha["universe"],
        delay=alpha["delay"],
        neutralization=alpha["neutralization"]
    )

    return alpha_id


def main():
    print("Starting WorldQuant session...")
    s = ace.start_session()

    alphas = load_alpha_files()
    print(f"Loaded {len(alphas)} alpha configs")

    for alpha in alphas:
        try:
            alpha_id = simulate_alpha(s, alpha)
            print("Alpha ID:", alpha_id)
            print("-" * 50)
        except Exception as e:
            print("Simulation failed:", e)


if __name__ == "__main__":
    main()
