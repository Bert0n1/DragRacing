
import logging
from typing import Callable
import pygame as pg

class Event():
    def __init__(self, uid: int):
        self.__event_id = uid
        self.__delegats: list[Callable] = []

    @property
    def uid(self):
        return self.__event_id

    @property
    def delegats(self) -> list[Callable]:
        return self.__delegats
    
    def subscribe(self, func: Callable):
        self.__delegats.append(func)
    
    def unsubscribe(self, func: Callable):
        self.__delegats.remove(func)

    def invoke(self, **kwargs):
        for delegate in self.__delegats:
            delegate(**kwargs)

class EventService():
    def __init__(self):
        self.__events: dict[int, Event] = dict()
        self.__system_events: dict[int, Event]  = {pg.QUIT: Event(pg.QUIT),
                                                   pg.MOUSEBUTTONDOWN: Event(pg.MOUSEBUTTONDOWN),
                                                   pg.MOUSEMOTION: Event(pg.MOUSEMOTION)}
    
    def register_event(self, id: str, event: Event = None):
        if id in self.__system_events and event:
            for f in event.delegats:
                self.__system_events[id].subscribe(f)                
        if not(id in self.__events):
            self.__events[id] = event if event != None else Event(id)
            logging.info(f"[EventService]: register event {id}")

    def subscribe(self, uid: int, func: Callable):
        if uid in self.__events:
            self.__events[uid].subscribe(func)
            logging.info(f"[EventService]: subscribed event {uid}")
        else:
            logging.error(f"[EventService]: event with id {uid} does not exists")
    
    def system_subcribe(self, id: int, func: Callable):
        if id in self.__system_events:
            self.__system_events[id].subscribe(func)
            logging.info(f"[EventService]: subscribed system event {id}")
        else:
             logging.error(f"[EventService]: system event with id {id} does not exists")


    def unsubscribe(self, uid: int, func: Callable):
        if uid in self.__events:
            if func in self.__events[uid].delegats:
                self.__events[uid].unsubscribe(func)
                logging.info(f"[EventService]: unsubscribed event {uid}")
            else:
                logging.error(f"[EventService]: delegats  does not exists")
        else:
             logging.error(f"[EventService]: event with id {uid} does not exists")

    
    def proccess_system_events(self):
        current_system_events = pg.event.get()
        for e in self.__system_events:
            for s_e in current_system_events:
                if e == s_e.type:
                    self.__system_events[e].invoke(**s_e.__dict__)


