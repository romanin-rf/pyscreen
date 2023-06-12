import subprocess
from vbml import Pattern, Patcher
from typing import Optional, List, Dict, Any

def command(*args: str) -> List[str]:
    return subprocess.getstatusoutput(list(args))[1].replace("\r", "").split("\n")

def screen(*args: str) -> List[str]:
    return command("screen", *args)

def check_pattern(text: str, patcher: Patcher, pattern: Pattern) -> Optional[Dict[str, Any]]:
    if isinstance(d := patcher.check(pattern, text), dict): return d
