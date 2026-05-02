import requests

def generate_test_cases(feature):
    prompt = f"""
    Generate test cases for the following feature:

    {feature}

    Include:
    - positive cases
    - negative cases
    - edge cases

    Return in format:

    1. Title:
       Steps:
       Expected Result:
    """

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]


def evaluate_response(feature, response):
    issues = []

    # 1. Coverage check
    if "positive" not in response.lower():
        issues.append("Missing positive test cases")

    if "negative" not in response.lower():
        issues.append("Missing negative test cases")

    if "edge" not in response.lower():
        issues.append("Missing edge cases")

    # 2. Critical domain awareness
    if any(word in feature.lower() for word in ["payment", "booking", "auth", "login"]):
        issues.append("Critical flow detected — requires strict validation")

    # 3. Weak test detection
    if "user logs in" in response.lower():
        issues.append("Generic steps detected — low test quality")

    # 4. Ambiguity detection
    if "etc" in response.lower() or "and so on" in response.lower():
        issues.append("Ambiguous test cases")

    # 5. Length heuristic
    if len(response) < 300:
        issues.append("Too short — likely insufficient coverage")

    return issues


import sys

if len(sys.argv) < 2:
    print("Usage: python3 pipeline.py 'Feature description'")
    exit()

feature = sys.argv[1]

print("\n" + "="*50)
print("AI QA PIPELINE")
print("="*50)

print(f"\nFeature: {feature}")

print("\n--- GENERATED TEST CASES ---\n")
test_cases = generate_test_cases(feature)
print(test_cases)

print("\n--- EVALUATION REPORT ---\n")

issues = evaluate_response(feature, test_cases)

if issues:
    print(f"Detected {len(issues)} potential issues:\n")
    for i, issue in enumerate(issues, 1):
        print(f"{i}. {issue}")
else:
    print("No major issues detected — test coverage looks reasonable")

score = max(0, 100 - len(issues) * 15)

print(f"\nQuality Score: {score}/100")

if score >= 80:
    verdict = "GOOD"
elif score >= 50:
    verdict = "NEEDS IMPROVEMENT"
else:
    verdict = "POOR"

print(f"Verdict: {verdict}")

