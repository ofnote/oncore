import sys
import logging
import re
from pathlib import Path

log = logging.getLogger(__name__)


def add_sys_paths (paths):
    sys.path.extend(paths)


def canonical_name(fn):
    parts = Path(fn).parts
    #print (parts)
    prefix, (textlid, header, fn) = parts[:-3], parts[-3:] 
    return '/'.join(list(prefix) + [textlid, header, f'{header}_{fn}.txt'])

def get_method(path):
    return get_class(path)

#https://stackoverflow.com/questions/44492803/python-dynamic-import-how-to-import-from-module-name-from-variable/44492879#44492879
def get_module_dict_safe (module, update=False):
    if hasattr(module, '__all__'):
        d = {n: getattr(module, n) for n in module.__all__} 
    else:
        d = {k: v for (k, v) in module.__dict__.items() if not k.startswith('_')}

    if update:
        globals().update(d)
    return d

def get_module(path_to_module):
    try:
        from importlib import import_module
        mod = import_module(path_to_module)
        return mod
    except ValueError as e:
        log.error(f"Error loading module {path_to_module}: {e}")

def get_class (module, class_name: str):
    try:
        klass = getattr(module, class_name)
    except AttributeError:
        raise ImportError(
                f"Class {class_name} is not in module {module}"
            )
    return klass

def get_class_by_path(path_to_class):
    try:
        from importlib import import_module
        module_path, _, class_name = path_to_class.rpartition(".")
        mod = import_module(module_path)
        klass = get_class(mod, class_name)            
        return klass
    except ValueError as e:
        log.error(f"Error initializing class {path_to_class}")
        raise e

def get_classes (path_to_module, classes):
    '''
    classes: a list of class names or a string with comma/spaced names
    '''
    if not isinstance(classes, list):
        assert isinstance(classes, str)
        classes = classes.replace(',', ' ')
        classes = re.sub("\s\s+" , " ", classes)
        classes = classes.split(' ')
        print (classes)

    mod = get_module(path_to_module)
    klasses = [get_class (mod, class_name) for class_name in classes]
    return klasses

def get_static_method(full_method_name):
    try:
        spl = full_method_name.split(".")
        method_name = spl.pop()
        class_name = ".".join(spl)
        klass = get_class(class_name)
        return getattr(klass, method_name)
    except Exception as e:
        log.error("Error getting static method {full_method_name}: {e}")
        raise e


def test1():
    add_sys_paths(['path/to/XLM'])
    TransformerModel = get_class_by_path('XLM.src.model.transformer.TransformerModel')
    # build model / reload weights
    model = TransformerModel(params, dico, True, True)


def test_class_loader():
    add_sys_paths(['path/to/XLM'])
    #xlm_dict = get_module('XLM.src.data.dictionary')
    Dictionary, BOS_WORD, EOS_WORD, PAD_WORD, UNK_WORD, MASK_WORD = \
    get_classes('XLM.src.data.dictionary', 'Dictionary, BOS_WORD, EOS_WORD, PAD_WORD, UNK_WORD, MASK_WORD')

    print (BOS_WORD, EOS_WORD)


