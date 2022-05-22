def save_event(event):
    open('event.txt', 'a', encoding='utf-8').write(event + ', ')


def read_event():
    return open('event.txt', 'r', encoding='utf-8').read()