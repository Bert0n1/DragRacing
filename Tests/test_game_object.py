
import App.GameObjects.gameObject as go


def test_add_children(): 
    obj = go.GameObject(parent=None, id='main')
    obj1 = go.GameObject(obj, 'a')
    obj2 = go.GameObject(parent=None, id='b')
    obj.add_child(obj2)

    a = obj.get_child('a')
    b = obj.get_child('b')
    assert a == obj1
    assert b == obj2

def test_search_children(): 
    obj = go.GameObject(parent=None, id='main')
    obj1 = go.GameObject(obj, 'a')
    obj2 = go.GameObject(parent=obj, id='b')
    b = obj.search('b')

    assert b == obj2

def test_clear(): 
    obj = go.GameObject(parent=None, id='main')
    obj1 = go.GameObject(obj, 'a')
    obj2 = go.GameObject(parent=obj, id='b')
    obj.clear()
    b = obj.search('b')
    a = obj.search('a')
    assert a == None
    assert b == None