import logging

from ckan.lib.base import BaseController, c, model, request, render, h, g
from ckan.lib.base import ValidationException, abort, gettext
from pylons.i18n import get_lang, _
from ckan.lib.alphabet_paginate import AlphaPage
from ckan.lib.dictization.model_dictize import package_dictize
from ckan.lib.helpers import Page
from ckan.model.domain_object import DomainObject
import ckan.logic as logic
from ckan.logic import get_action, NotFound
_get_or_bust = logic.get_or_bust
_check_access = logic.check_access

import ckan.forms
import ckan.authz as authz
import ckan.lib.dictization.model_save as model_save
import ckan.lib.mailer as mailer
import ckan.lib.navl.dictization_functions as dict_func
import ckan.lib.dictization.model_dictize as model_dictize
import ckan.logic as logic
import ckan.logic.action as action
import ckan.logic.schema as schema
import ckan.model as model

import pylons.config as config
from ckan.lib.navl.validators import (ignore_missing,
                                      not_empty,
                                      empty,
                                      ignore,
                                      keep_extras,)

from ckanext.pat.plugin import CATEGORY_VOCAB

class CategoryController(BaseController):
    
    def _get_category_list(self, context):
        vocab_data = {'id': CATEGORY_VOCAB}
        try:
            vocab = get_action('vocabulary_show')(context, vocab_data)
        except NotFound:
            raise
        data_dict = {'all_fields': True, 'vocabulary_id':vocab['id']}
        tag_list = get_action('tag_list')(context, data_dict)
        
        results = []
        for tag in tag_list:
            tag_data_dict = {'id': tag['id'], 'package_details':False}
            try:
                tag_details = self._tag_show(context, tag_data_dict)
                results.append(Category(tag['id'], tag['display_name'], u'', len(tag_details['packages'])))
            except NotFound:
                #abort(404, _('Tag not found'))
                pass
        return results

    def index(self, data=None, errors=None, error_summary=None):
        
        context = {'model': model, 'session': model.Session,
                   'user': c.user or c.author, 'for_view': True,
                   'with_private': False}
        
        results = self._get_category_list(context)
        
        c.page = Page(
            collection=results,
            page=request.params.get('page', 1),
            url=h.pager_url,
            items_per_page=20
        )
        
        return render('category_index.html')
        

    def read(self, id):

        context = {'model': model, 'session': model.Session,
                   'user': c.user or c.author, 'for_view': True,
                   'with_private': False}

        tag_data_dict = {'id': id}
        tag_details = self._tag_show(context, tag_data_dict)
  
        c.page = Page(
            collection=tag_details['packages'],
            page=request.params.get('page', 1),
            url=h.pager_url,
            items_per_page=20
        )
        
        c.category = Category(tag_details['id'], tag_details['display_name'], u'', len(tag_details['packages']))
        c.categories = self._get_category_list(context)
        
        return render('category_read.html')

    def _tag_show(self, context, data_dict):
        '''Return the details of a tag and all its datasets.
    
        :param id: the name or id of the tag
        :type id: string
    
        :param package_details: if False details are not returned
        :type package_details: boolean
    
        :returns: the details of the tag, including a list of all of the tag's
            datasets and their details (if needed)
        :rtype: dictionary
    
        '''
        model = context['model']
        id = _get_or_bust(data_dict, 'id')
    
        tag = model.Tag.get(id)
        context['tag'] = tag
    
        if tag is None:
            raise NotFound
    
        _check_access('tag_show',context, data_dict)
    
        tag_dict = model_dictize.tag_dictize(tag,context)
    
        if data_dict.has_key('package_details') and data_dict['package_details'] == False:
            pass
        else:
            extended_packages = []
            for package in tag_dict['packages']:
                pkg = model.Package.get(package['id'])
                extended_packages.append(model_dictize.package_dictize(pkg,context))
        
            tag_dict['packages'] = extended_packages
    
        return tag_dict

class Category:

    def __init__(self, id=u'', title=u'', description=u'', packages=0):
        self.id = id
        self.title = title
        self.description = description
        self.packages = packages

    @property
    def display_name(self):
        if self.title is not None and len(self.title):
            return self.title
        else:
            return self.id
