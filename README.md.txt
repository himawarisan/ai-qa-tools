AI QA Pipeline

AI-assisted tool for generating and evaluating test cases.

Features:

* Generate test cases from feature descriptions using LLM
* Evaluate test quality (coverage, ambiguity, critical flows)
* Assign quality score

⸻
How it works:

1. User inputs feature description
2. System generates test cases
3. System evaluates:
    * coverage (positive/negative/edge)
    * ambiguity
    * critical flows (payment, login, etc.)
4. Outputs quality score

⸻
Example

Input:
	Login with payment and password reset

Output:
	Quality Score: 70/100
	Issues:
	- Critical flow detected
	- Generic steps detected

⸻
Run locally using terminal commands:

pip3 install requests
python3 pipeline.py

⸻
Tech

* Python
* Ollama (local LLM)
* Heuristic-based evaluation

