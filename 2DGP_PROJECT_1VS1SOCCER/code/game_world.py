from pico2d import *

objects = [[], [], []]


def add_object(o, depth=0):
    objects[depth].append(o)


def add_objects(ol, depth=0):
    objects[depth] += ol


def update():
    for layer in objects:
        for o in layer:
            o.update()


def render():
    for layer in objects:
        for o in layer:
            o.draw()


def remove_object(o):
    for layer in objects:
        if o in layer:
            layer.remove(o)
            return
    raise ValueError('존재하지 않은 객체를 지우려고 합니다.')


def clear():
    global objects
    objects.clear()
    objects = [[], [], []]

def handle_events(e):
    for layer in objects:
        for o in layer:
            o.handle_events(e)
