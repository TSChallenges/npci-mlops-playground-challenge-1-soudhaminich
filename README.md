# AIML MLOps Playground Challenge 1

## Title: Process Management in Linux using Python

### Challenge Details:
The **Playground Challenge 1** was released on **Thursday, Nov 28, 2024**. 

-  Prepare for the challenge individually beforehand.
-  Teams will be announced at the start of the session on **Saturday, Nov 30, 2024**.
-  Solutions must be implemented on a virtual machine.
-  Collaborate with your team in Zoom breakout rooms to implement and finalize your solution.
-  Reach out to the instructor for guidance if you face challenges.

---

### Evaluation:
1. Present your solution to the instructor for evaluation (20 points).
2. Submit the solution files on the GitHub Classroom post-evaluation (individually).

---

### Challenge Description:
As a system administrator, your task is to optimize server performance in a Linux environment. The challenge involves creating a Python script to monitor system processes and simulate partition management using loop devices. This will aid in managing resources effectively and ensuring smooth application operation.

---

### Challenge Requirements:
Create a Python script named **`process-manager.py`** with the following functionality:

1. **`get_top_cpu_processes(sort_by='cpu', limit=5)`**  
   Retrieve and display the top 5 processes by CPU usage.

2. **`get_top_mem_processes(sort_by='mem', limit=5)`**  
   Retrieve and display the top 5 processes by memory usage.

3. **`get_process_info(pid)`**  
   Fetch and display detailed information about a specific process using its PID.

4. **`search_process(name=None, pid=None)`**  
   Search for a process by name or PID and display its details.

5. **`kill_process(pid=None, name=None)`**  
   Terminate a process by its PID or name.

6. **`monitor_process(pid=None, name=None)`**  
   Continuously monitor a process and display its CPU and memory usage.

