from collections import Counter
from typing import List, Dict


def total_events(events: List[Dict]) -> int:
    return len(events)


def count_by_event_type(events: List[Dict]) -> Dict[str, int]:
    return dict(
        Counter(
            event.get("event_type")
            for event in events
            if event.get("event_type")
        )
    )


def top_source_ips(events: List[Dict], limit: int = 5) -> List[Dict]:
    counter = Counter(
        event.get("source_ip")
        for event in events
        if event.get("source_ip")
    )

    return [
        {"ip": ip, "count": count}
        for ip, count in counter.most_common(limit)
    ]


def top_usernames(events: List[Dict], limit: int = 5) -> List[Dict]:
    counter = Counter(
        event.get("username")
        for event in events
        if event.get("username")
    )

    return [
        {"username": username, "count": count}
        for username, count in counter.most_common(limit)
    ]


def activity_by_hour(events: List[Dict]) -> Dict[str, int]:
    counter = Counter()

    for event in events:
        timestamp = event.get("timestamp")
        if not timestamp:
            continue

        try:
            hour = timestamp.split()[2].split(":")[0]
            counter[hour] += 1
        except Exception:
            continue

    return dict(counter)


def summary(events: List[Dict]) -> Dict:
    return {
        "total_events": total_events(events),
        "event_types": count_by_event_type(events),
        "top_source_ips": top_source_ips(events),
        "top_usernames": top_usernames(events),
        "activity_by_hour": activity_by_hour(events),
    }