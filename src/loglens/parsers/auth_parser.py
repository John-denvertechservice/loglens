import re
from typing import Dict

from loglens.parsers.base import BaseParser


class AuthParser(BaseParser):
    LOG_PATTERN =re.compile(
        r"(?P<timestamp>\w+\s+\d+\s+\d+:\d+:\d+)\s+"
        r"(?P<host>\S+)\s+"
        r"sshd\[(?P<pid>\d+)\]:\s+"
        r"(?P<action>Failed|Accepted)\s+password\s+for\s+"
        r"(?P<username>\S+)\s+from\s+"
        r"(?P<ip>\S+)"
         )

    def parse_line(self, line: str) -> Dict:
        match = self.LOG_PATTERN.search(line)

        if not match:
            return {}

        data  = match.groupdict()

        event_type = "failed_login" if data["action"] == "Failed" else "successful login"
        return {
            "timestamp": data["timestamp"],
            "host": data["host"],
            "pid": data["pid"],
            "event_type": event_type,
            "username": data["username"],
            "source_ip": data["ip"],
            "raw": line,
            }
    
