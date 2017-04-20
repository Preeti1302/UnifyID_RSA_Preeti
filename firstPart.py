from urllib.request import Request, urlopen

import threading
_LOCK = threading.Lock()

url = "https://www.random.org/integers/?setStart={0}&min={1}&max={2}&col={3}&base={4}&format=plain&rnd=new"

def checkRange(min, max, setStart=1):
    format_of_url = url.format(setStart, min, max, 1, 10)
    request = Request(format_of_url)
    request.add_header("User-agent", "preetipatil@sjsu")
    with _LOCK:
        read_source = urlopen(request).read()
    return [int(x) for x in read_source.splitlines()]
