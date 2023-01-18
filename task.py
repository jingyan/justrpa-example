"""Template robot with Python."""
import argparse
from justrpa.task import TaskHandler

def run_task(taskname:str):
    handler = TaskHandler()
    handler.run(taskname)
    
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("task",default="", nargs="?", help="task name to run")
    args = ap.parse_args()
    task_name = args.task
    run_task(task_name)

if __name__ == "__main__":
    main()