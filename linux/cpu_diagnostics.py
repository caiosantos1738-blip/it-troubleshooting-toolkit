
import os
import platform
import subprocess


def check_cpu():
    print("\n[ CPU DIAGNOSTICS ]")
    print("-" * 40)

    try:
        cpu_model = "Unknown"

        if platform.system() == "Linux":
            result = subprocess.run(
                ["lscpu"],
                capture_output=True,
                text=True,
                check=True
            )

            for line in result.stdout.splitlines():
                if line.startswith("Model name:"):
                    cpu_model = line.split(":", 1)[1].strip()
                    break

        cpu_cores = os.cpu_count()

        load_1, load_5, load_15 = os.getloadavg()

        cpu_data = {
            "status": "success",
            "model": cpu_model,
            "logical_cores": cpu_cores,
            "load_average": {
                "1_min": round(load_1, 2),
                "5_min": round(load_5, 2),
                "15_min": round(load_15, 2)
            }
        }

        print(f"CPU Model: {cpu_model}")
        print(f"Logical CPU Cores: {cpu_cores}")
        print(f"Load Average (1 min): {load_1:.2f}")
        print(f"Load Average (5 min): {load_5:.2f}")
        print(f"Load Average (15 min): {load_15:.2f}")

        print("\n[SUCCESS] CPU diagnostics completed.")

        return cpu_data

    except FileNotFoundError:
        print("[ERROR] lscpu command not found.")
        return {
            "status": "error",
            "message": "lscpu command not found"
        }

    except Exception as error:
        print(f"[ERROR] CPU diagnostics failed: {error}")
        return {
            "status": "error",
            "message": str(error)
        }


if __name__ == "__main__":
    check_cpu()
