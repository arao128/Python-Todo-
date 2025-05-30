import sys

TODO_FILE = "todo.txt"

def add_task(task):
    """タスクをファイルに追加します。"""
    with open(TODO_FILE, "a") as f:
        f.write(task + "\n")
    print(f"'{task}' を追加しました。")

def view_tasks():
    """タスクを表示"""
    try:
        with open(TODO_FILE, "r") as f:
            tasks = [line.strip() for line in f]
            if tasks:
                print("--- Todoリスト ---")
                for i, task in enumerate(tasks):
                    print(f"{i+1}. {task}")
                print("------------------")
            else:
                print("Todoリストは空です。")
    except FileNotFoundError:
        print("Todoリストはまだ作成されていません。")

def complete_task(task_index):
    """指定されたインデックスのタスクを完了にする"""
    try:
        with open(TODO_FILE, "r+") as f:
            tasks = [line.strip() for line in f]
            if 1 <= task_index <= len(tasks):
                tasks[task_index - 1] = "[x] " + tasks[task_index - 1]
                f.seek(0)
                f.truncate()
                f.writelines([task + "\n" for task in tasks])
                print(f"{task_index}番目のタスクを完了にしました。")
            else:
                print("指定された番号のタスクはありません。")
    except FileNotFoundError:
        print("Todoリストはまだ作成されていません。")
    except ValueError:
        print("無効な入力です。番号を入力してください。")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("使い方: python todo.py <コマンド> [タスク内容/番号]")
        print("コマンド:")
        print("  add <タスク内容>   : 新しいタスクを追加します。")
        print("  view               : Todoリストを表示します。")
        print("  complete <番号>    : 指定した番号のタスクを完了にします。")
    else:
        command = sys.argv[1].lower()
        if command == "add":
            if len(sys.argv) > 2:
                task = " ".join(sys.argv[2:])
                add_task(task)
            else:
                print("追加するタスクを入力してください。")
        elif command == "view":
            view_tasks()
        elif command == "complete":
            if len(sys.argv) > 2:
                try:
                    task_index = int(sys.argv[2])
                    complete_task(task_index)
                except ValueError:
                    print("完了するタスクの番号を整数で入力してください。")
            else:
                print("完了するタスクの番号を入力してください。")
        else:
            print(f"不明なコマンド '{command}' です。")