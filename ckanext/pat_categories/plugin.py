import os
import logging

from ckan.plugins import IRoutes, IConfigurer
from ckan.plugins import implements, SingletonPlugin

log = logging.getLogger(__name__)

class CategoryPlugin(SingletonPlugin):
    """
    """
    implements(IRoutes)
    implements(IConfigurer)

    def before_map(self, map):
        controller = 'ckanext.pat_categories.controllers:CategoryController'
        map.connect('/category/{id}', controller=controller, action='read')
        map.connect('/category', controller=controller, action='index')
        map.redirect('/categories', '/category')
        return map

    def after_map(self, map):
        return map

    def update_config(self, config):
        #"""
        #This IConfigurer implementation causes CKAN to look in the
        #```templates``` directory when looking for the group_form()
        #"""
        here = os.path.dirname(__file__)
        rootdir = os.path.dirname(os.path.dirname(here))
        
        template_dir = os.path.join(rootdir, 'ckanext', 'pat_categories', 'templates')
        config['extra_template_paths'] = ','.join([template_dir, config.get('extra_template_paths', '')])

        ## Override /group/* as the default groups urls
        #config['ckan.default.group_type'] = 'organization'

    #def index_template(self):
    #    print "CategoryPlugin index_template..."
    #    """
    #    Returns a string representing the location of the template to be
    #    rendered for the index page
    #    """
    #    return 'category_index.html'
    #
    #def read_template(self):
    #    print "CategoryPlugin read_template..."
    #    """
    #    Returns a string representing the location of the template to be
    #    rendered for the read page
    #    """
    #    return 'category_read.html'
