from diagnostics.report_manager import generate_linux_reports
from linux.service_diagnostics import check_services
from linux.disk_diagnostics import check_disk
from linux.memory_diagnostics import check_memory
from network.network_diagnostics import network_menu
from linux.cpu_diagnostics import check_cpu
import platform
import os
from datetime import datetime

def show_header():
    print("=" * 55)
    print("          IT TROUBLESHOOTING TOOLKIT")
    print("          Technical Support Diagnostics")
    print("=" * 55)
    print(f"Operating System: {platform.system()}")
    print(f"Computer: {platform.node()}")
    print(f"Date: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("=" * 55)


def linux_menu():
    while True:
        print("\n[ LINUX DIAGNOSTICS ]")
        print("1. Check CPU")
        print("2. Check memory usage")
        print("3. Check disk space")
        print("4. Check active services")
        print("0. Back to main menu")

        option = input("\nSelect an option: ").strip()

        if option == "1":
            check_cpu()
        elif option == "2":
            check_memory()
        elif option == "3":
            check_disk()
        elif option == "4":
            check_services()
        elif option == "0":
            break
        else:
            print("\nInvalid option.")

        input("\nPress ENTER to continue...")

def windows_menu():
    print("\n[ WINDOWS DIAGNOSTICS ]")
    print("1. Check IP configuration")
    print("2. Check system information")
    print("3. Check network connectivity")
    print("0. Back to main menu")


def main():
    while True:
        os.system("clear" if os.name == "posix" else "cls")

        show_header()

        print("\nMAIN MENU")
        print("1. Network Diagnostics")
        print("2. Linux Diagnostics")
        print("3. Windows Diagnostics")
        print("4. Generate Reports")
        print("0. Exit")

        option = input("\nSelect an option: ").strip()

        if option == "1":
            network_menu()
        elif option == "2":
            linux_menu()
        elif option == "3":
            windows_menu()
        elif option == "4":
            generate_linux_reports()
        elif option == "0":
            print("\nExiting IT Troubleshooting Toolkit...")
            break
        else:
            print("\nInvalid option.")

        input("\nPress ENTER to continue...")


if __name__ == "__main__":
    main()

