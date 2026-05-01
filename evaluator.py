def evaluate_response(prompt, response):
    issues = []

    if len(response) < 20:
        issues.append("Response too short — possible low quality")

    if "always" in response.lower():
        issues.append("Contains absolute claims — possible hallucination risk")

    if "maybe" in response.lower():
        issues.append("Uncertain language detected")

    return issues


prompt = input("Enter prompt: ")
response = input("Enter LLM response: ")

issues = evaluate_response(prompt, response)

print("\nDetected issues:")
for issue in issues:
    print(f"- {issue}")
