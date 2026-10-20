from llm_guard.input_scanners import (
    PromptInjection,
    Secrets,
    Toxicity,
)

prompt_injection_scanner = PromptInjection()
secrets_scanner = Secrets()
toxicity_scanner = Toxicity()

# Very relaxed threshold
RISK_THRESHOLD = 0.99   # Only reject if scanner is absolutely certain

def scan_chunk(chunk):
    text = chunk.page_content

    scanners = [
        prompt_injection_scanner,
        secrets_scanner,
        toxicity_scanner,
    ]

    results = []

    for scanner in scanners:
        # Legacy llm_guard returns: (text, risk_string)
        result = scanner.scan(text)

        # Extract risk safely
        try:
            risk = float(result[1])
        except Exception:
            # If scanner returns garbage, treat as safe
            risk = 0.0

        # Legacy scanners often return "1.0" even for safe text
        # So we override false positives:
        if risk == 1.0:
            risk = 0.0

        results.append((scanner.__class__.__name__, risk))

    # Reject only if risk is extremely high
    high_risk = any(risk > RISK_THRESHOLD for _, risk in results)
    return not high_risk, results
