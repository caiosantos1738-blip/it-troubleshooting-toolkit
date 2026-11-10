
import shutil


def check_disk():
    print("\n[ DISK DIAGNOSTICS ]")
    print("-" * 40)

    try:
        disk = shutil.disk_usage("/")

        total = disk.total
        used = disk.used
        free = disk.free

        total_gb = total / (1024 ** 3)
        used_gb = used / (1024 ** 3)
        free_gb = free / (1024 ** 3)

        usage_percent = (used / total) * 100 if total else 0

        if usage_percent >= 90:
            status = "critical"
            message = "Disk usage is critical"
        elif usage_percent >= 75:
            status = "warning"
            message = "Disk usage is high"
        else:
            status = "success"
            message = "Disk space is healthy"

        disk_data = {
            "status": status,
            "filesystem": "/",
            "total_gb": round(total_gb, 2),
            "used_gb": round(used_gb, 2),
            "free_gb": round(free_gb, 2),
            "usage_percent": round(usage_percent, 2),
            "message": message
        }

        print("Filesystem: /")
        print(f"Total Space: {total_gb:.2f} GB")
        print(f"Used Space: {used_gb:.2f} GB")
        print(f"Free Space: {free_gb:.2f} GB")
        print(f"Disk Usage: {usage_percent:.2f}%")

        if status == "critical":
            print(f"\n[WARNING] {message}!")
        elif status == "warning":
            print(f"\n[WARNING] {message}.")
        else:
            print(f"\n[SUCCESS] {message}.")

        return disk_data

    except Exception as error:
        print(f"[ERROR] Disk diagnostics failed: {error}")
        return {
            "status": "error",
            "message": str(error)
        }


if __name__ == "__main__":
    check_disk()
