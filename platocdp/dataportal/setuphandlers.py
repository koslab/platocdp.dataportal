from collective.grok import gs
from platocdp.dataportal import MessageFactory as _

@gs.importstep(
    name=u'platocdp.dataportal', 
    title=_('platocdp.dataportal import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('platocdp.dataportal.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
