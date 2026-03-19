# LogLens

LogLens is a Python-based log analysis tool designed to parse, analyze, and report on system and network-related log files.

The project begins as a command-line tool for analyzing authentication logs and producing summary statistics, suspicious activity detections, and exportable JSON reports. Over time, it will expand to support additional log formats, a web interface, and richer reporting.

## Goals

- Parse raw log files into structured event data
- Analyze log activity for useful patterns and anomalies
- Detect suspicious behavior such as repeated failed login attempts
- Export analysis results to JSON
- Provide both a CLI and a lightweight web interface

## Planned Features

- Authentication log parser
- Event statistics and summaries
- Suspicious activity detection
- JSON report export
- Command-line interface
- Flask web dashboard
- Support for additional log formats

## Project Structure

```text
loglens/
├── README.md
├── requirements.txt
├── .gitignore
├── sample_logs/
├── reports/
├── src/
│   └── loglens/
│       ├── __init__.py
│       ├── main.py
│       ├── cli.py
│       ├── parsers/
│       ├── analyzers/
│       ├── exporters/
│       └── web/
└── tests/
