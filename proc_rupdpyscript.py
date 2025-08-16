from js import document, window

def proc_read(id: str) -> str:
    try:
        el = document.getElementById(id)
        if not el:
            return "--"
        if hasattr(el, "value"):
            return el.value
        return el.textContent
    except Exception:
        return "--"

def proc_write(id: str, content) -> None:
    try:
        el = document.getElementById(id)
        if el:
            if hasattr(el, "value"):
                el.value = str(content)     # input / textarea
            else:
                el.textContent = str(content)  # div / span / p
    except Exception:
        pass

def proc_alert(msg: str) -> None:
    try:
        window.alert(str(msg))
    except Exception:
        pass
