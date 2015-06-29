from five import grok
from plone.directives import dexterity, form
from platocdp.dataportal.content.organization import IOrganization

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(IOrganization)
    grok.require('zope2.View')
    grok.template('organization_view')
    grok.name('view')

    def sub_organizations(self):
        return [{
            'title': 'hello',
            'url': 'http://www.google.com'
        }]
