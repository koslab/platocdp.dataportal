from five import grok
from plone.directives import dexterity, form
from platocdp.dataportal.content.application import IApplication

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(IApplication)
    grok.require('zope2.View')
    grok.template('application_view')
    grok.name('view')

