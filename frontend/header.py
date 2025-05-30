from __future__ import annotations as _annotations

from fastui import AnyComponent
from fastui.components import Link
from fastui import components as c
from fastui.events import GoToEvent

Link.model_rebuild()

def demo_page(*components: AnyComponent, title: str | None = None) -> list[AnyComponent]:
    return [
        c.PageTitle(text=f'Rate Model Demo — {title}' if title else 'Rate Model Demo'),
        c.Navbar(
            title='Rate Model Demo',
            title_event=GoToEvent(url='/'),
            start_links=[
                c.Link(
                    components=[c.Text(text='Add Route')],
                    on_click=GoToEvent(url='/addroute'),
                    active='startswith:/addroute',
                )
            ],
        ),
        c.Page(
            components=[
                *((c.Heading(text=title),) if title else ()),
                *components,
            ],
        ),
    ]