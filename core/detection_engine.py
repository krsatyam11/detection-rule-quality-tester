import time
import re
from core.sigma_conditions import evaluate_selection

class DetectionEngine:
    def __init__(self, rules, log_df):
        self.rules = [r for r in rules if r.is_valid]
        self.log_df = log_df

    def run(self):
        start_time = time.time()
        results = []
        
        records = self.log_df.to_dict('records')
        
        for rule in self.rules:
            rule_matches = []
            for record in records:
                if self._evaluate_rule(rule, record):
                    rule_matches.append(record)
            
            results.append({
                "rule_id": rule.id,
                "title": rule.title,
                "level": rule.level,
                "techniques": rule.get_mitre_techniques(),
                "match_count": len(rule_matches),
                "matches": rule_matches,
                "status": "Success",
                "condition": rule.condition
            })

        execution_time = time.time() - start_time
        return results, execution_time

    def _evaluate_rule(self, rule, record):
        condition_str = rule.condition
        selections = {k: v for k, v in rule.detection.items() if k != "condition"}
        
        eval_env = {}
        for sel_name, sel_dict in selections.items():
            eval_env[sel_name] = evaluate_selection(sel_dict, record)
            
        safe_cond = condition_str
        for sel_name in sorted(eval_env.keys(), key=len, reverse=True):
            val = " True " if eval_env[sel_name] else " False "
            safe_cond = re.sub(rf'\b{sel_name}\b', val, safe_cond)

        allowed_chars = set("TrueFalseandornot() \t")
        if not all(c in allowed_chars for c in safe_cond):
            return False 
            
        try:
            return eval(safe_cond, {"__builtins__": {}}, {})
        except Exception:
            return False