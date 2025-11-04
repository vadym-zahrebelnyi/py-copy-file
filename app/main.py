import os


def copy_file(command: str) -> None:
    if (
        len(command_chain := command.split(" ")) == 3
        and command_chain[0] == "cp"
        and os.path.exists(src := command_chain[1])
        and src != (dst := command_chain[2])
    ):
        with (
            open(src, "r") as file_in,
            open(dst, "w") as file_out
        ):
            file_out.write(file_in.read())
