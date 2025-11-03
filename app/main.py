import os


def copy_file(command: str) -> None:
    if (
        len(command_chain := command.split(" ")) == 3
        and command_chain[0] == "cp"
        and os.path.exists(command_chain[1])
        and command_chain[1] != command_chain[2]
    ):
        with (
            open(command_chain[1], "r") as file_in,
            open(command_chain[2], "w") as file_out
        ):
            file_out.write(file_in.read())
            print("Copy created")
