from typing import Generic, TypeVar, List
import abc
# pylint: disable=maybe-no-member
import wx


E = TypeVar('E')
class Vec2(Generic[E]):
    x: E
    y: E
    _i: int

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self._i = 0

    def __iter__(self):
        self._i = 0
        return self

    def __next__(self):
        if self._i == 0:
            self._i += 1
            return self.x
        elif self._i == 1:
            self._i += 1
            return self.y
        else:
            raise StopIteration


class Node:
    id_: str
    position: Vec2[int]
    size: Vec2[int]
    fill_color: wx.Colour
    border_color: wx.Colour
    border_width: int

    # force keyword-only arguments
    def __init__(self, *, id_: str, pos: Vec2[int], size: Vec2[int],
                 fill_color: wx.Colour, border_color: wx.Colour, border_width: int):
        self.id_ = id_
        self.position = pos
        self.size = size
        self.fill_color = fill_color
        self.border_color = border_color
        self.border_width = border_width

    def Contains(self, pos: Vec2[int]) -> bool:
        '''Returns whether the given position is contained within the node rectangle
        '''
        return (pos.x >= self.position.x) and (pos.x <= self.position.x + self.size.x) and \
            (pos.y >= self.position.y) and (pos.y <= self.position.y + self.size.y)


class IController(abc.ABC):
    """The inteface class for a controller

    The abc.ABC (Abstract Base Class) is used to enforce the MVC interface more
    strictly.

    The methods with name beginning with Try- are usually called by the View after
    some user input. If the action tried in such a method succeeds, the Controller
    should request the view to be redrawn
    """

    @abc.abstractmethod
    def TryAddNode(self, node: Node):
        """Try to add the given Node to the canvas."""
        pass

    @abc.abstractmethod
    def TryMoveNode(self, node: Node):
        """Try to move the give node. TODO only accept node ID and new location"""
        pass

    @abc.abstractmethod
    def GetListOfNodeIds(self) -> List[str]:
        """Try getting the list of node IDs"""
        pass


class IView(abc.ABC):
    """The inteface class for a controller

    The abc.ABC (Abstract Base Class) is used to enforce the MVC interface more
    strictly.
    """

    @abc.abstractmethod
    def BindController(self, controller: IController):
        """Bind the controller. This needs to be called after a controller is 
        created and before any other method is called.
        """
        pass

    @abc.abstractmethod
    def MainLoop(self):
        """Run the main loop. This is blocking right now. This may be modified to
        become non-blocking in the future if required.
        """
        pass

    @abc.abstractmethod
    def UpdateAll(self, nodes):
        """Update all the graph objects, and redraw everything at the end"""
        pass
