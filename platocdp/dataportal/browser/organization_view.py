from five import grok
from plone.directives import dexterity, form
from platocdp.dataportal.content.organization import IOrganization
from Products.CMFCore.utils import getToolByName

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(IOrganization)
    grok.require('zope2.View')
    grok.template('organization_view')
    grok.name('view')

    def sub_organizations(self):
        path = '/'.join(self.context.getPhysicalPath())
        
        catalog = getToolByName(self.context, 'portal_catalog')
        
        brains = catalog(
                path={'query': path, 'depth' : 1}, 
            portal_type=['platocdp.dataportal.organization']
        )
        
        result = []
        for brain in brains:
            if brain.getPath() == path:
                continue
            result.append({'title': brain['Title'], 'url': brain.getURL()})
        return result


    def datasets(self, depth=None):
        path = '/'.join(self.context.getPhysicalPath())
        
        catalog = getToolByName(self.context, 'portal_catalog')
        
        brains = catalog(
            path={'query': path},
            portal_type=['platocdp.dataportal.dataset']
        )

        result = []
        for brain in brains:
            if brain.getPath() == path:
                continue
            result.append({'title': brain['Title'], 'url': brain.getURL()})
        return result


