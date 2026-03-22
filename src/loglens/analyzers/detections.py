from collections import Counter
from typing import List, Dict

def detect_bruteforce(events: List[Dict], threshold: int = 3):
    failed_ips = [
        event["source_ips"]
        for event in events
        if event.get("event.type") == "failed_login"
        ]

    counter = Counter(failed_ips)

    return [
        {"ip": ip, "failed_attempts": count}
        for ip, count in counter.items()
        if count >= threshold
    ]

def detect_user_targeting(events: List[Dict], threshold: int = 3)

    usernames = [
    event["username"]
    for event in events
    if event.get("event_type") == "failed_login"
    ]

    counter = Counter(usernames)

    return [
        {"username":user, "failed_attempts": count}
        for user, count in counter.items()
        if count >= threshold
    ]

def detect_ip_spread(events: List[Dict], threshold: int = 3)
    ip_to_users = {}

    for event in events:
        if event.get("event_type") != "failed_login":
            continue

        ip = event.get("source_ip")
        user = event.get("username")
        
        if not ip or not user:
            continue

        ip_to_users.setdefault(ip, set()).add(user)
    
    return [
        {"ip": ip, "unique_users": len(users)}
        for ip, users in ip_to_users.items()
        if len(users) >= threshold
    ]

def run_all_detections(events: List[Dict])
    return {
        "bruteforce_ips": detect_bruteforce(events),
        "targeting_users": detect_user_targeting(events), 
        "ip_spread": detect_ip_spread(events),
    }



