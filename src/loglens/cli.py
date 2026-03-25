import argparse
from loglens.parsers.auth_parser import AuthParser
from loglens.analyzers.stats import summary
from loglens.analyzers.detections import run_all_detections

def run():
    parser = argparse.ArgumentParser(
    description="LogLens - Log Analysis Tool"
    )
    parser.add_argument(
    "file",
    help="Path to log file"
    )
    parser.add_argument(
    "-json",
    help="Export results to JSON file",
    default=None
    )

    args = parser.parse_args()
    log_parser = AuthParser()
    events = log_parser.parse_file(args.file)
    stats_report = summary(events)
    detections_report = run_all_detections(events)

    report = {
        "summary":stats_report,
        "detections": detections_report
    }
    
    print("\n=== LogLens Report ===\n")
    print("Summary:")
    print(stats_report)

    print("\nDetections")
    print(detections_report)

    if args.json:
        import json
        with open(args.json, "w") as f:
            json.dump(report, f, indent=4)

        print(f"\nReport saved to {args.json}")

