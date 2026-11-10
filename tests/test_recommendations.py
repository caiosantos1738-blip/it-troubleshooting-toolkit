
from diagnostics.report_manager import generate_recommendations


def test_healthy_system():
    data = {
        "cpu": {"status": "success"},
        "memory": {"status": "success", "usage_percent": 30},
        "disk": {"status": "success", "usage_percent": 40},
        "services": {"status": "success", "total_active": 10}
    }

    recommendations = generate_recommendations(data)

    assert len(recommendations) == 1
    assert recommendations[0]["severity"] == "INFO"


def test_high_memory_usage():
    data = {
        "memory": {"status": "success", "usage_percent": 85}
    }

    recommendations = generate_recommendations(data)

    assert any(
        item["severity"] == "WARNING"
        and item["category"] == "memory"
        for item in recommendations
    )


def test_critical_memory_usage():
    data = {
        "memory": {"status": "success", "usage_percent": 95}
    }

    recommendations = generate_recommendations(data)

    assert any(
        item["severity"] == "CRITICAL"
        and item["category"] == "memory"
        for item in recommendations
    )


def test_high_disk_usage():
    data = {
        "disk": {"status": "success", "usage_percent": 80}
    }

    recommendations = generate_recommendations(data)

    assert any(
        item["severity"] == "WARNING"
        and item["category"] == "disk"
        for item in recommendations
    )


def test_critical_disk_usage():
    data = {
        "disk": {"status": "success", "usage_percent": 95}
    }

    recommendations = generate_recommendations(data)

    assert any(
        item["severity"] == "CRITICAL"
        and item["category"] == "disk"
        for item in recommendations
    )


def test_diagnostic_error():
    data = {
        "cpu": {
            "status": "error",
            "message": "lscpu command not found"
        }
    }

    recommendations = generate_recommendations(data)

    assert any(
        item["severity"] == "CRITICAL"
        and item["category"] == "cpu"
        for item in recommendations
    )


def test_no_active_services():
    data = {
        "services": {
            "status": "success",
            "total_active": 0
        }
    }

    recommendations = generate_recommendations(data)

    assert any(
        item["severity"] == "WARNING"
        and item["category"] == "services"
        for item in recommendations
    )
def test_disk_warning_status():
    data = {
        "disk": {
            "status": "warning",
            "usage_percent": 80
        }
    }

    recommendations = generate_recommendations(data)

    assert any(
        item["severity"] == "WARNING"
        and item["category"] == "disk"
        for item in recommendations
    )


def test_disk_critical_status():
    data = {
        "disk": {
            "status": "critical",
            "usage_percent": 95
        }
    }

    recommendations = generate_recommendations(data)

    assert any(
        item["severity"] == "CRITICAL"
        and item["category"] == "disk"
        for item in recommendations
    )
