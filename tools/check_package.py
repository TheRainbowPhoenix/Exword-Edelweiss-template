"""Check the actual template output, including its embedded upstream bootstrap."""
from pathlib import Path
import re
import struct
import sys

base = Path(sys.argv[1])
cache = (base / "CMakeCache.txt").read_text()
def setting(name):
    match = re.search(rf"^{name}:STRING=(.*)$", cache, re.MULTILINE)
    assert match, name
    return match[1]

appid, module = setting("EXWORD_APP_ID"), setting("EXWORD_MODULE")
bootstrap = (base / "edelweiss.d01").read_bytes()
payload = (base / "main.edl").read_bytes()
assert bootstrap[:16] == b"CASIODICPLUGIN10" and 128 < len(bootstrap) <= 131072
assert (base / (module + ".d01")).read_bytes() == bootstrap
assert payload[:7] == b"\x7fELF\x01\x02\x01" and struct.unpack_from(">H", payload, 18)[0] == 42
assert re.fullmatch(r"[0-9a-f]{40}\n", (base / "edelweiss-version.txt").read_text())
for locale in ("ja", "cn"):
    package = base / "packages" / locale / appid
    assert (package / (module + ".d01")).read_bytes() == bootstrap
    assert (package / "main.edl").read_bytes() == payload
    assert (package / "fileinfo.cji").is_file()
    html = list(package.glob("*.htm"))
    assert html
    for page in html:
        data = page.read_bytes()
        assert b"@APP" not in data and b"\r\n" in data
    print(locale, appid, "main.edl + current Edelweiss bootstrap: package passed")
