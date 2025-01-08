# NetEnhance

NetEnhance is a Python-based tool designed to enhance internet connectivity and network performance on Windows machines. It provides fine-tuning options to optimize various network settings, ensuring smoother and faster internet usage.

## Features

- **Optimize TCP Settings**: Adjusts TCP parameters for improved performance.
- **Flush DNS Cache**: Clears the DNS cache to resolve connectivity issues.
- **Reset Network Settings**: Resets the network stack to its default state.

## Requirements

- Windows Operating System
- Python 3.x
- Administrative privileges to execute network commands

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/netenhance.git
   ```

2. Navigate to the project directory:
   ```bash
   cd netenhance
   ```

## Usage

Run the script with administrative privileges to enhance your network settings:

```bash
python net_enhance.py
```

## Note

This script must be run with administrative privileges. If not, it will raise a `PermissionError`.

## Disclaimer

Use this tool at your own risk. The author is not responsible for any damage caused by the use of this tool. Always ensure you have backups of your important data before making changes to system settings.