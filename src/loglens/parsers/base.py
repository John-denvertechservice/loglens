from abc import ABC, abstractmethod
from typing import List, Dict


class BaseParser(ABC):
    """
    Abstract base class for all log parsers.
    Each parser must implement a parse_line method.
    """

    @abstractmethod
    def parse_line(self, line: str) -> Dict:
        """
        Parse a single log line into a structured dictionary.

        Args:
            line (str): Raw log line

        Returns:
            Dict: Structured event data
        """
        pass

    def parse_file(self, file_path: str) -> List[Dict]:
        """
        Parse an entire log file.

        Args:
            file_path (str): Path to the log file

        Returns:
            List[Dict]: List of parsed events
        """
        events = []

        with open(file_path, "r") as f:
            for line in f:
                line = line.strip()

                if not line:
                    continue

                try:
                    event = self.parse_line(line)
                    if event:
                        events.append(event)
                except Exception as e:
                    # For now, fail gracefully and continue
                    print(f"Error parsing line: {line}")
                    print(f"Error: {e}")

        return events
