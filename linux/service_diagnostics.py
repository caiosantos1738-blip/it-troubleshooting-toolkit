
import subprocess


def check_services():
    print("\n[ ACTIVE SERVICES DIAGNOSTICS ]")
    print("-" * 55)

    try:
        result = subprocess.run(
            [
                "systemctl",
                "list-units",
                "--type=service",
                "--state=running",
                "--no-legend",
                "--no-pager"
            ],
            capture_output=True,
            text=True,
            timeout=15
        )

        if result.returncode != 0:
            print("[ERROR] Unable to retrieve active services.")

            if result.stderr:
                print(result.stderr.strip())

            return {
                "status": "error",
                "message": result.stderr.strip()
                or "Unable to retrieve active services"
            }

        services = [
            line.strip()
            for line in result.stdout.splitlines()
            if line.strip()
        ]

        service_data = {
            "status": "success",
            "total_active": len(services),
            "services": services
        }

        print(f"Active services found: {len(services)}\n")

        if not services:
            print("No running services found.")
        else:
            for service in services:
                print(service)

        print("\n[SUCCESS] Service diagnostics completed.")

        return service_data

    except FileNotFoundError:
        print("[ERROR] systemctl command not found.")

        return {
            "status": "error",
            "message": "systemctl command not found"
        }

    except subprocess.TimeoutExpired:
        print("[ERROR] Service query timed out.")

        return {
            "status": "error",
            "message": "Service query timed out"
        }

    except Exception as error:
        print(f"[ERROR] Service diagnostics failed: {error}")

        return {
            "status": "error",
            "message": str(error)
        }


if __name__ == "__main__":
    check_services()
