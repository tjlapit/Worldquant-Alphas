import json
import os

ALPHA_DIR = "alphas"

def load_alpha_files():
    alphas = []

    for filename in os.listdir(ALPHA_DIR):
        if filename.endswith(".json"):
            path = os.path.join(ALPHA_DIR, filename)

            with open(path, "r", encoding="utf-8") as f:
                alpha = json.load(f)
                alphas.append(alpha)

    return alphas


def main():
    alphas = load_alpha_files()
    print(f"Loaded {len(alphas)} alpha configs")

    for alpha in alphas:
        print("Alpha name:", alpha.get("name"))
        print("Expression:", alpha.get("expression"))
        print("-" * 40)


if __name__ == "__main__":
    main()
