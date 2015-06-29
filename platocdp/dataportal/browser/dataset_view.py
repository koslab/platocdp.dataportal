from five import grok
from plone.directives import dexterity, form
from platocdp.dataportal.content.dataset import IDataSet

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(IDataSet)
    grok.require('zope2.View')
    grok.template('dataset_view')
    grok.name('view')

