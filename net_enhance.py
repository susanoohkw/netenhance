import os
import subprocess
import ctypes
from typing import List

class NetEnhance:
    def __init__(self):
        self.admin_check()

    def admin_check(self):
        """ Check if the script is run as an administrator """
        try:
            is_admin = ctypes.windll.shell32.IsUserAnAdmin()
        except Exception as e:
            raise PermissionError("Unable to check admin status: " + str(e))
        if not is_admin:
            raise PermissionError("This script requires administrative privileges. Please run as administrator.")

    def execute_command(self, command: List[str]) -> str:
        """ Execute a system command and return the output """
        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Command '{' '.join(command)}' failed with error: {e.output}")

    def optimize_tcp(self):
        """ Optimize TCP settings for better internet performance """
        print("Optimizing TCP settings...")
        self.execute_command(["netsh", "int", "tcp", "set", "global", "autotuninglevel=normal"])
        self.execute_command(["netsh", "int", "tcp", "set", "global", "rss=enabled"])
        self.execute_command(["netsh", "int", "tcp", "set", "global", "chimney=enabled"])
        print("TCP settings optimized.")

    def flush_dns(self):
        """ Flush DNS cache """
        print("Flushing DNS cache...")
        self.execute_command(["ipconfig", "/flushdns"])
        print("DNS cache flushed.")

    def reset_network(self):
        """ Reset network settings """
        print("Resetting network settings...")
        self.execute_command(["netsh", "int", "ip", "reset"])
        self.execute_command(["netsh", "winsock", "reset"])
        print("Network settings reset.")

    def enhance_connectivity(self):
        """ Enhance internet connectivity """
        print("Enhancing internet connectivity...")
        self.optimize_tcp()
        self.flush_dns()
        self.reset_network()
        print("Internet connectivity enhanced.")

if __name__ == "__main__":
    try:
        enhancer = NetEnhance()
        enhancer.enhance_connectivity()
    except PermissionError as e:
        print(f"Permission Error: {e}")
    except RuntimeError as e:
        print(f"Runtime Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")