#Author- George Roberts
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        doc = app.activeDocument
        products = doc.products
        des = adsk.fusion.Design.cast(products.itemByProductType("DesignProductType"))
        allcomps = des.rootComponent.allOccurrences
        for comp in allcomps:
            comp.isGrounded = True

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
