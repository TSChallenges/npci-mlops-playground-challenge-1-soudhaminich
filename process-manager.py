import psutil
import time

def get_top_cpu_processes(limit=5):
    processes = sorted(
        [(p.info['pid'], p.info['name'], p.info['cpu_percent']) 
         for p in psutil.process_iter(['pid', 'name', 'cpu_percent'])], 
        key=lambda x: x[2], 
        reverse=True
    )

    print(f"\nTop {limit} processes by CPU usage:")
    for pid, name, cpu in processes[:limit]:
        print(f"PID: {pid}, Name: {name}, CPU: {cpu:.2f}%")

def get_top_mem_processes(limit=5):
    processes = sorted(
        [(p.info['pid'], p.info['name'], p.info['memory_percent']) 
         for p in psutil.process_iter(['pid', 'name', 'memory_percent'])], 
        key=lambda x: x[2], 
        reverse=True
    )

    print(f"\nTop {limit} processes by Memory usage:")
    for pid, name, mem in processes[:limit]:
        print(f"PID: {pid}, Name: {name}, Memory: {mem:.2f}%")

def get_process_info(pid):
    p = psutil.Process(pid)
    print(f"\nProcess Info for PID {pid}:")
    print(f"Name: {p.name()}")
    print(f"Status: {p.status()}")
    print(f"CPU Usage: {p.cpu_percent(interval=1)}%")
    print(f"Memory Usage: {p.memory_percent():.2f}%")
    print(f"Executable: {p.exe()}")

def search_process(name=None, pid=None):
    for p in psutil.process_iter(['pid', 'name']):
        if (name and p.info['name'].lower() == name.lower()) or (pid and p.info['pid'] == pid):
            print(f"\nFound Process - PID: {p.info['pid']}, Name: {p.info['name']}")
            get_process_info(p.info['pid'])
            return
    print("No matching process found.")

def kill_process(pid=None, name=None):
    if pid:
        p = psutil.Process(pid)
        p.terminate()
        print(f"Terminated process PID {pid}")
    elif name:
        for p in psutil.process_iter(['pid', 'name']):
            if p.info['name'].lower() == name.lower():
                p.terminate()
                print(f"Terminated process {name} (PID {p.info['pid']})")
                return
    else:
        print("Provide either PID or Name to terminate.")

def monitor_process(pid=None, name=None):
    if not pid and not name:
        print("Provide either PID or process name to monitor.")
        return

    p = psutil.Process(pid) if pid else next(
        (p for p in psutil.process_iter(['pid', 'name']) if p.info['name'].lower() == name.lower()), None)

    if not p:
        print("Process not found.")
        return

    print(f"\nMonitoring process: {p.info['name']} (PID: {p.info['pid']})")
    try:
        while True:
            print(f"CPU: {p.cpu_percent(interval=1)}%, Memory: {p.memory_percent():.2f}%")
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

def main():
    """Interactive menu using switch-case (match-case)."""
    while True:
        print("\nSelect an option:")
        print("1. Top CPU-consuming processes")
        print("2. Top Memory-consuming processes")
        print("3. Get Process Info (by PID)")
        print("4. Search Process (by Name or PID)")
        print("5. Kill Process (by Name or PID)")
        print("6. Monitor Process (by Name or PID)")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        match choice:
            case "1":
                limit = input("Enter number of processes (default: 5): ") or "5"
                get_top_cpu_processes(int(limit))
            case "2":
                limit = input("Enter number of processes (default: 5): ") or "5"
                get_top_mem_processes(int(limit))
            case "3":
                pid = int(input("Enter PID: "))
                get_process_info(pid)
            case "4":
                search_by = input("Search by (1: Name, 2: PID): ")
                if search_by == "1":
                    name = input("Enter process name: ")
                    search_process(name=name)
                elif search_by == "2":
                    pid = int(input("Enter PID: "))
                    search_process(pid=pid)
                else:
                    print("Invalid choice.")
            case "5":
                kill_by = input("Kill by (1: Name, 2: PID): ")
                if kill_by == "1":
                    name = input("Enter process name: ")
                    kill_process(name=name)
                elif kill_by == "2":
                    pid = int(input("Enter PID: "))
                    kill_process(pid=pid)
                else:
                    print("Invalid choice.")
            case "6":
                monitor_by = input("Monitor by (1: Name, 2: PID): ")
                if monitor_by == "1":
                    name = input("Enter process name: ")
                    monitor_process(name=name)
                elif monitor_by == "2":
                    pid = int(input("Enter PID: "))
                    monitor_process(pid=pid)
                else:
                    print("Invalid choice.")
            case "7":
                print("Exiting...")
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
