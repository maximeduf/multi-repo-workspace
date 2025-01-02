from dataclasses import dataclass
from typing import Callable, TypeVar

T = TypeVar('T')


@dataclass
class LineArgument:
    """
    Represents a single program argument. (--path)
    @param name: The name of the argument.  (project_path)
    @param value: The value of the argument. (~/Documents)
    @param prompt_fn: To be given in the command's __init__.
    @param confirm_fn: To be given in the command's __init__.
    """
    name: str
    value: T = None
    prompt_fn: Callable[[str], T] = None
    confirm_fn: Callable[[T], bool] = None
    is_confirmed: bool = False

    def set_prompts(self, *, prompt_fn: Callable[[str], T],
                    confirm_fn: Callable[[T], bool]):
        self.prompt_fn = prompt_fn
        self.confirm_fn = confirm_fn

    def confirm_value(self, value: T) -> bool:
        confirmation = self.confirm_fn(value)
        self.is_confirmed = confirmation
        return confirmation

    def is_confirmed_str(self):
        return "ready" if self.is_confirmed else "not ready"

    def __str__(self):
        repr = f"{self.name}: {self.value} - "
        repr += f"{'prompt ready' if self.prompt_fn else 'prompt missing'}, "
        repr += f"{'confirm ready' if self.prompt_fn else 'confirm missing'}, "
        repr += f"{self.is_confirmed_str()}"
        return repr


class CommandArgs:
    """
    CommandArgs will have arguments passed from command line as a dictionary.
    """

    def __init__(self, *args: LineArgument):
        self.args = {arg.name: arg for arg in args}

    # enable "selection" with `self.args['name']` instead of `self.args.get('name')`
    def __getitem__(self, name: str):
        return self.args.get(name)

    def arg_values(self):
        return self.args.values()

    def is_confirmed(self, name: str = None) -> bool:
        """
        Check if a specific argument or all arguments have been confirmed.
        """
        if name:
            return (self.args.get(name).is_confirmed
                    if name in self.args else False)
        return all(arg.is_confirmed for arg in self.args.values())

    def __repr__(self):
        repr = "CommandArgs:\n"
        for arg in self.args.values():
            repr += f"    - {arg.__repr__()}\n"
        return repr
