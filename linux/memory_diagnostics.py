
import subprocess


def check_memory():
    print("\n[ MEMORY DIAGNOSTICS ]")
    print("-" * 40)

    try:
        result = subprocess.run(
            ["free", "-m"],
            capture_output=True,
            text=True,
            check=True
        )

        memory_line = next(
            line for line in result.stdout.splitlines()
            if line.startswith("Mem:")
        )

        values = memory_line.split()

        total = int(values[1])
        used = int(values[2])
        available = int(values[6])

        usage_percent = (used / total) * 100 if total else 0

        memory_data = {
            "status": "success",
            "total_mb": total,
            "used_mb": used,
            "available_mb": available,
            "usage_percent": round(usage_percent, 2)
        }

        print(f"Total Memory: {total} MB")
        print(f"Used Memory: {used} MB")
        print(f"Available Memory: {available} MB")
        print(f"Memory Usage: {usage_percent:.2f}%")

        print("\n[SUCCESS] Memory diagnostics completed.")

        return memory_data

    except FileNotFoundError:
        print("[ERROR] free command not found.")
        return {
            "status": "error",
            "message": "free command not found"
        }

    except Exception as error:
        print(f"[ERROR] Memory diagnostics failed: {error}")
        return {
            "status": "error",
            "message": str(error)
        }


if __name__ == "__main__":
    check_memory()
