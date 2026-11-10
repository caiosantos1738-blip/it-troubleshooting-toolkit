
import json
import os
import platform
from datetime import datetime

from linux.cpu_diagnostics import check_cpu
from linux.memory_diagnostics import check_memory
from linux.disk_diagnostics import check_disk
from linux.service_diagnostics import check_services


def generate_recommendations(data):
    """Analyze diagnostic results and generate recommendations."""

    recommendations = []

    # Check diagnostic execution errors
    for category, result in data.items():
        if result.get("status") == "error":
            recommendations.append({
                "severity": "CRITICAL",
                "category": category,
                "message": "Diagnostic execution failed.",
                "action": "Check the command, permissions and system configuration."
            })

    # Check memory usage
    memory = data.get("memory", {})

    if memory.get("status") == "success":
        usage = memory.get("usage_percent", 0)

        if usage >= 90:
            recommendations.append({
                "severity": "CRITICAL",
                "category": "memory",
                "message": f"Memory usage is critical: {usage}%.",
                "action": "Identify processes consuming excessive memory."
            })

        elif usage >= 80:
            recommendations.append({
                "severity": "WARNING",
                "category": "memory",
                "message": f"Memory usage is high: {usage}%.",
                "action": "Monitor memory consumption and review running processes."
            })

    # Check disk usage
    disk = data.get("disk", {})

    if disk.get("status") in ("success", "warning", "critical"):
        usage = disk.get("usage_percent", 0)

        if usage >= 90:
            recommendations.append({
                "severity": "CRITICAL",
                "category": "disk",
                "message": f"Disk usage is critical: {usage}%.",
                "action": "Free disk space and investigate large files."
            })

        elif usage >= 75:
            recommendations.append({
                "severity": "WARNING",
                "category": "disk",
                "message": f"Disk usage is high: {usage}%.",
                "action": "Review disk consumption and remove unnecessary files."
            })

    # Check active services
    services = data.get("services", {})

    if services.get("status") == "success":
        total = services.get("total_active", 0)

        if total == 0:
            recommendations.append({
                "severity": "WARNING",
                "category": "services",
                "message": "No active services were found.",
                "action": "Verify systemd and check whether essential services are running."
            })

    # Informational result when no problems are detected
    if not recommendations:
        recommendations.append({
            "severity": "INFO",
            "category": "system",
            "message": "No issues detected by the available diagnostics.",
            "action": "Continue routine system monitoring."
        })

    return recommendations


def create_report(data, recommendations):
    """Create a structured diagnostic report."""

    now = datetime.now()

    report = {
        "computer": platform.node(),
        "operating_system": platform.system(),
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%H:%M:%S"),
        "diagnostics": data,
        "recommendations": recommendations
    }

    return report


def save_json_report(report):
    os.makedirs("reports", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"reports/diagnostic_report_{timestamp}.json"

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4, ensure_ascii=False)

    return filename


def format_result(data, indent=0):
    """Format structured diagnostic data for TXT reports."""

    lines = []
    prefix = " " * indent

    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, (dict, list)):
                lines.append(f"{prefix}{key.replace('_', ' ').title()}:")
                lines.extend(format_result(value, indent + 4))
            else:
                lines.append(
                    f"{prefix}{key.replace('_', ' ').title()}: {value}"
                )

    elif isinstance(data, list):
        for item in data:
            lines.append(f"{prefix}- {item}")

    else:
        lines.append(f"{prefix}{data}")

    return lines


def save_txt_report(report):
    os.makedirs("reports", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"reports/diagnostic_report_{timestamp}.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write("IT TROUBLESHOOTING TOOLKIT\n")
        file.write("=" * 45 + "\n\n")

        file.write(f"Computer: {report['computer']}\n")
        file.write(f"Operating System: {report['operating_system']}\n")
        file.write(f"Date: {report['date']}\n")
        file.write(f"Time: {report['time']}\n\n")

        file.write("DIAGNOSTIC RESULTS\n")
        file.write("-" * 45 + "\n")

        for category, result in report["diagnostics"].items():
            file.write(f"\n{category.upper()}\n")
            file.write("-" * 30 + "\n")

            for line in format_result(result):
                file.write(line + "\n")

        file.write("\n\nAUTOMATIC RECOMMENDATIONS\n")
        file.write("-" * 45 + "\n")

        for recommendation in report["recommendations"]:
            file.write(
                f"\n[{recommendation['severity']}] "
                f"{recommendation['category'].upper()}\n"
            )
            file.write(f"Message: {recommendation['message']}\n")
            file.write(f"Action: {recommendation['action']}\n")

    return filename


def generate_linux_reports():
    """Run Linux diagnostics and generate JSON and TXT reports."""

    print("\n[ GENERATING LINUX DIAGNOSTIC REPORTS ]")

    diagnostic_data = {
        "cpu": check_cpu(),
        "memory": check_memory(),
        "disk": check_disk(),
        "services": check_services()
    }

    recommendations = generate_recommendations(diagnostic_data)

    print("\n[ AUTOMATIC RECOMMENDATIONS ]")

    for recommendation in recommendations:
        print(
            f"\n[{recommendation['severity']}] "
            f"{recommendation['category'].upper()}"
        )
        print(f"Message: {recommendation['message']}")
        print(f"Action: {recommendation['action']}")

    report = create_report(diagnostic_data, recommendations)

    json_file = save_json_report(report)
    txt_file = save_txt_report(report)

    print("\n[SUCCESS] Reports generated!")
    print(f"JSON Report: {json_file}")
    print(f"TXT Report: {txt_file}")
