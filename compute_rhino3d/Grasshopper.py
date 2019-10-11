from . import Util
import base64
import io
import os


class DataTree:
    def __init__(self, name):
        self.data = {'ParamName': name, 'InnerTree': {}}

    def Append(self, path, items):
        """
        Append a path to this tree

        Args:
            path (iter): a list of integers defining a path
            items (list): list of data to add to the tree
        """
        key = ''
        for item in path:
            if len(key) == 0:
                key = '{}'.format(item)
                continue
            key = '{};{}'.format(key, item)

        self.data['InnerTree'][key] = [{'data': item} for item in items]


def EvaluateDefinition(definition, trees):
    """
    Evaluate a grasshopper definition on the compute server.

    Args:
        definition (str): path to a grasshopper defition
        trees (iter): list of DataTree instances
    Returns:
    """
    url = "grasshopper"
    args = {'algo': None, 'pointer': None, 'values': None}
    if definition.startswith('http:') or definition.startswith('https:'):
        args['pointer'] = definition
    else:
        if os.path.isfile(definition):
            with io.open(definition, 'r', encoding='utf-8-sig') as content_file:
                definition = content_file.read()
        encoded = base64.b64encode(definition.encode('utf-8'))
        args['algo'] = str(encoded, 'utf-8')

    args['values'] = [tree.data for tree in trees]
    response = Util.ComputeFetch(url, args)
    return response

