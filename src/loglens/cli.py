import argparse
from loglens.parsers.auth_parser import AuthParser
from loglens.analyzers.stats import summary
from loglens.analyzers.detections import run_all_detections
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def render_summary(stats_report):
    table = Table(title = "Summary")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="magenta")
    table.add_row("Total_events", str(stats_report["total_events"]))
    for event_type, count in stats_report["event_types"].items():
        table.add_row(f"{event_type}", str(count))
    return table

def render_top_ips(top_ips):
    table = Table(title="Top Source IPs")
    table.add_column("IP address", style="green")
    table.add_column("Count", style="yellow")
    for item in top_ips:
        table.add_row(item["ip"], str(item["count"]))
    return table

def render_detections(detections):
    table = Table(title="Detections")

    table.add_column("Type", style="red")
    table.add_column("Details", style="white")

    for ip in detections["bruteforce_ips"]:
        table.add_row(
            "🤖 Brute Force",
            f'{ip["ip"]} ({ip["failed_attempts"]} attempts)'
        )

    for user in detections["targeted_users"]:
        table.add_row(
            "Targeted User",
            f'{user["username"]} ({user["failed_attempts"]} attempts)'
        )

    for spread in detections["ip_spread"]:
        table.add_row(
            "IP Spread",
            f'{spread["ip"]} ({spread["unique_users"]} users)'
        )

    return table
def run():
    parser = argparse.ArgumentParser(
    description="LogLens - Log Analysis Tool"
    )
    parser.add_argument(
    "file",
    help="Path to log file"
    )
    parser.add_argument(
    "--json",
    help="Export results to JSON file",
    default=None
    )
    parser.add_argument(
    "--top",
    type=int,
    default=5,
    help="Number of top results to display"
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
    
    console.print("\n=== LogLens Report ===\n")
    console.print("Summary:")
    console.print(Panel("LogLens Report", style="bold blue"))

    console.print("\n")
    console.print(Panel("Summary", style="bold green"))
    console.print(render_summary(stats_report))

    console.print("\n")
    console.print(Panel("Top Activity", style="bold cyan"))
    console.print(render_top_ips(stats_report["top_source_ips"][:args.top]))

    console.print("\n")
    console.print(Panel("Security Detections", style="bold red"))

    if not detections_report["bruteforce_ips"]:
        console.print("[green]No brute-force activity detected[/green]")
    if not stats_report["top_source_ips"]:
        console.print("[yellow]No IP data available[/yellow]")
    else:
        console.print(render_detections(detections_report))
        
        if args.json:
            import json
            with open(args.json, "w") as f:
                json.dump(report, f, indent=4)

        console.print(f"\nReport saved to {args.json}")

