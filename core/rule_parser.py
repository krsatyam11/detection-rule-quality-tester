import re

class SigmaRule:
    def __init__(self, raw_dict, file_name=""):
        self.raw = raw_dict
        self.file_name = file_name
        self.title = raw_dict.get("title", "Unknown Rule")
        self.id = raw_dict.get("id", "No ID")
        self.status = raw_dict.get("status", "unknown")
        self.level = raw_dict.get("level", "unknown")
        self.tags = raw_dict.get("tags", [])
        self.logsource = raw_dict.get("logsource", {})
        self.detection = raw_dict.get("detection", {})
        self.condition = self.detection.get("condition", "")
        self.is_valid, self.errors = self._validate()

    def _validate(self):
        errors = []
        if not self.detection:
            errors.append("Missing 'detection' block.")
        if not self.condition:
            errors.append("Missing 'condition' in detection block.")
        return len(errors) == 0, errors

    def get_mitre_techniques(self):
        techniques = []
        technique_pattern = re.compile(r'attack\.t\d{4}(?:\.\d{3})?')
        for tag in self.tags:
            match = technique_pattern.search(tag.lower())
            if match:
                techniques.append(match.group(0).upper().replace("ATTACK.", ""))
        return techniques