from __future__ import absolute_import

import os

import panel as pn

pn.extension(sizing_mode="stretch_width")


appName = "Test panel app"
panel_main = pn.template.bootstrap.BootstrapTemplate(title=appName)


panel = pn.Column("Test app")

panel_main.main.append(panel)


async def init():
    print("Init: Start.")
    print("Init: Done.")
    return


if __name__.startswith("bokeh"):
    pn.state.execute(init)
    panel_main.servable()
1
