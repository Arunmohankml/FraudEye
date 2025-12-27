def analyze_transaction(txn):
    risk = 0
    reasons = []

    if txn.amount > 50000:
        risk += 40
        reasons.append("Unusually high transaction amount")

    if txn.country != "IN":
        risk += 30
        reasons.append("Cross-border transaction")

    if txn.account_age_days < 7:
        risk += 20
        reasons.append("Newly created account")

    return {
        "fraud_flag": risk >= 60,
        "risk_score": risk,
        "explanation": reasons
    }
