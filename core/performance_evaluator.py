def calculate_metrics(results):
    total_matches = sum(r["match_count"] for r in results)
    rules_with_hits = sum(1 for r in results if r["match_count"] > 0)
    
    return {
        "total_matches": total_matches,
        "rules_with_hits": rules_with_hits,
        "rules_without_hits": len(results) - rules_with_hits,
        "coverage_percent": round((rules_with_hits / len(results) * 100) if results else 0, 2)
    }

def evaluate_ground_truth(log_df, ground_truth_col):
    if ground_truth_col not in log_df.columns:
        return None
        
    actual_attacks = log_df[ground_truth_col].astype(bool).sum()
    return {
        "status": "Not fully implemented in MVP. Requires row-index tracking.",
        "actual_attacks": int(actual_attacks)
    }