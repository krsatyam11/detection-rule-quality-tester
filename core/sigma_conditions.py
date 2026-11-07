import re

def evaluate_selection(selection_dict, log_record):
    if not isinstance(selection_dict, dict):
        return False

    for field, expected_value in selection_dict.items():
        modifier = None
        if "|" in field:
            parts = field.split("|", 1)
            field = parts[0]
            modifier = parts[1]

        if field not in log_record:
            return False
        
        actual_value = str(log_record[field])
        
        if isinstance(expected_value, list):
            match_found = False
            for val in expected_value:
                if _match_value(actual_value, str(val), modifier):
                    match_found = True
                    break
            if not match_found:
                return False
        else:
            if not _match_value(actual_value, str(expected_value), modifier):
                return False
                
    return True

def _match_value(actual, expected, modifier):
    # Handle Sigma wildcards (*) by converting to Regex
    if "*" in expected and modifier != "re":
        # Escape special regex chars, then convert literal \* to .*
        regex_pattern = re.escape(expected).replace(r"\*", ".*")
        
        if modifier == "startswith":
            regex_pattern = "^" + regex_pattern
        elif modifier == "endswith":
            regex_pattern = regex_pattern + "$"
            
        try:
            return bool(re.search(regex_pattern, actual, re.IGNORECASE))
        except re.error:
            return False

    # Standard exact/modifier matches without wildcards
    actual_lower = actual.lower()
    expected_lower = expected.lower()

    if not modifier:
        return actual_lower == expected_lower
    
    modifier = modifier.lower()
    if modifier == "contains":
        return expected_lower in actual_lower
    elif modifier == "startswith":
        return actual_lower.startswith(expected_lower)
    elif modifier == "endswith":
        return actual_lower.endswith(expected_lower)
    elif modifier == "re":
        try:
            return bool(re.search(expected, actual, re.IGNORECASE))
        except re.error:
            return False
            
    return actual_lower == expected_lower