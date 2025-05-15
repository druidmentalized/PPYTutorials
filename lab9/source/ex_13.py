from lab9.source.ex_9 import keyword_filter

def dispatcher():
    handlers = {
        "error": keyword_filter("error"),
        "info": keyword_filter("info"),
        "debug": keyword_filter("debug"),
    }
    for h in handlers.values(): next(h)

    try:
        while True:
            msg = yield
            for prefix, handler in handlers.items():
                if msg.startswith(prefix + ":"):
                    handler.send(msg)
    except GeneratorExit:
        for h in handlers.values():
            h.close()

d = dispatcher(); next(d)
d.send("info: hello")
d.send("error: crash")
d.close()