import subprocess
from typing import Optional, Union, List
from _typeshed import StrOrBytesPath

def command(
    command: Union[str, List[str]],
    final_line: Optional[str]=None,
    cwd: Optional[StrOrBytesPath]=None,
    return_output: bool=False
) -> List[bytes]:
    command = command.split() if isinstance(command, str) else command
    popen = subprocess.Popen(command, stdout=subprocess.PIPE, cwd=cwd)
    lines_iterator = iter(popen.stdout.readline, b"")
    output = None
    for line in lines_iterator:
        if return_output:
            if output == None:
                output = [line]
            else:
                output.append(line)
        else:
            print(line)
        if (final_line != None) and (final_line in str(line)):
            return output
    return output