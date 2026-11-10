
import socket
import subprocess
import platform


# ==========================================
# NETWORK DIAGNOSTICS
# ==========================================

def check_connectivity():
    """Test network connectivity using ping."""

    print("\n[ INTERNET CONNECTIVITY TEST ]")

    host = input("Enter host (default: 8.8.8.8): ").strip()
    host = host or "8.8.8.8"

    if not host:
        print("[ERROR] Invalid host.")
        return

    command = ["ping", "-c", "4", host]

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=20
        )

        if result.stdout:
            print(result.stdout)

        if result.returncode == 0:
            print("[SUCCESS] Host is reachable.")
        else:
            print("[WARNING] Host is unreachable or ICMP is blocked.")

    except subprocess.TimeoutExpired:
        print("[ERROR] Ping operation timed out.")

    except FileNotFoundError:
        print("[ERROR] Ping command is not installed.")

    except OSError as error:
        print(f"[ERROR] System error: {error}")


def check_dns():
    """Resolve a domain name using DNS."""

    print("\n[ DNS RESOLUTION TEST ]")

    domain = input(
        "Enter domain (default: google.com): "
    ).strip()

    domain = domain or "google.com"

    try:
        results = socket.getaddrinfo(
            domain,
            None,
            family=socket.AF_UNSPEC,
            type=socket.SOCK_STREAM
        )

        addresses = sorted({
            result[4][0] for result in results
        })

        print(f"\n[SUCCESS] DNS resolution for {domain}")

        for address in addresses:
            print(f"IP Address: {address}")

    except socket.gaierror as error:
        print(f"[ERROR] DNS resolution failed: {error}")


def check_gateway():
    """Identify the default network gateway on Linux."""

    print("\n[ DEFAULT GATEWAY CHECK ]")

    if platform.system() != "Linux":
        print("[INFO] This function currently supports Linux only.")
        return

    try:
        result = subprocess.run(
            ["ip", "route", "show", "default"],
            capture_output=True,
            text=True,
            timeout=5
        )

        if result.returncode != 0:
            print("[ERROR] Could not retrieve routing information.")
            if result.stderr:
                print(result.stderr)
            return

        output = result.stdout.strip()

        if output:
            print("[SUCCESS] Default gateway information:")
            print(output)
        else:
            print("[WARNING] No default gateway found.")

    except FileNotFoundError:
        print("[ERROR] The 'ip' command is not installed.")

    except subprocess.TimeoutExpired:
        print("[ERROR] Gateway check timed out.")

    except OSError as error:
        print(f"[ERROR] System error: {error}")


def check_tcp_port():
    """Test TCP connectivity to a specific host and port."""

    print("\n[ TCP PORT CONNECTIVITY TEST ]")

    host = input("Enter hostname or IP address: ").strip()

    if not host:
        print("[ERROR] Host cannot be empty.")
        return

    port_input = input("Enter TCP port (1-65535): ").strip()

    try:
        port = int(port_input)

        if not 1 <= port <= 65535:
            print("[ERROR] Port must be between 1 and 65535.")
            return

    except ValueError:
        print("[ERROR] Please enter a valid numeric port.")
        return

    try:
        with socket.create_connection(
            (host, port),
            timeout=5
        ):
            print(
                f"[SUCCESS] TCP port {port} is OPEN on {host}."
            )

    except socket.timeout:
        print(
            f"[WARNING] Connection to {host}:{port} timed out."
        )

    except ConnectionRefusedError:
        print(
            f"[WARNING] Connection refused by {host}:{port}."
        )

    except socket.gaierror:
        print(f"[ERROR] Could not resolve hostname: {host}")

    except OSError as error:
        print(f"[ERROR] Connection failed: {error}")


# ==========================================
# NETWORK MENU
# ==========================================

def network_menu():

    while True:

        print("\n" + "=" * 45)
        print("          NETWORK DIAGNOSTICS")
        print("=" * 45)

        print("1. Check internet connectivity")
        print("2. Check DNS resolution")
        print("3. Check default gateway")
        print("4. Test TCP port")
        print("0. Back to main menu")

        option = input("\nSelect an option: ").strip()

        if option == "1":
            check_connectivity()

        elif option == "2":
            check_dns()

        elif option == "3":
            check_gateway()

        elif option == "4":
            check_tcp_port()

        elif option == "0":
            print("\nReturning to main menu...")
            break

        else:
            print("\n[ERROR] Invalid option. Try again.")

        input("\nPress ENTER to continue...")


# ==========================================
# STANDALONE EXECUTION
# ==========================================

if __name__ == "__main__":
    network_menu()
