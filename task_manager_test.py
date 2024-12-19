import pytest
from task_manager import *


def test_add_task():
    notebook = TaskManager()
    notebook.add_task(Task("naucit se python"))
    assert notebook.task_list == [Task("naucit se python")]

