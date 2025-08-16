from js import document

def proc_read(id: str) -> str:
    try:
        el = document.getElementById(id)
        if not el:
            return "--"
        return el.value if hasattr(el, "value") else el.textContent
    except Exception:
        return "--"

def proc_write(id: str, content) -> None:
    try:
        el = document.getElementById(id)
        if el:
            el.textContent = str(content)
    except Exception:
        pass
