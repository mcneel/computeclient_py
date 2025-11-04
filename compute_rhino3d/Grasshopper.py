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
        definition (str): path to a grasshopper definition
        trees (iter): list of DataTree instances
    Returns:
    """
    url = "grasshopper"
    algo, pointer = encode_definition(definition)
    args = {
        'algo': algo,
        'pointer': pointer,
        'values': [tree.data for tree in trees]
    }
    response = Util.ComputeFetch(url, args)
    return response


def GetDefinitionIO(definition):
    """
    Get input and output metadata of a Grasshopper definition.

    Args:
        definition (str): path or URL to a Grasshopper definition
    Returns:
        dict: Definition metadata including: Description, InputNames, OutputNames,
        Icon, Inputs, Outputs, Warnings, Errors
    """
    url = "io"
    algo, pointer = encode_definition(definition)
    args = {
        'algo': algo,
        'pointer': pointer
    }
    response = Util.ComputeFetch(url, args)
    return response

def encode_definition(definition):
    """
    Encodes a Grasshopper definition to prepare for Rhino.Compute.

    Args:
        definition (str): path or URL to a Grasshopper definition

    Returns:
        algo, pointer
    """
    if definition.startswith('http:') or definition.startswith('https:'):
        return None, definition

    encoded = None
    if os.path.isfile(definition):
        try:
            if definition.endswith('.gh'):
                with open(definition, 'rb') as gh:
                    content_bytes = gh.read()
                    encoded = base64.b64encode(content_bytes)
            else:
                with io.open(definition, 'r', encoding='utf-8-sig') as ghx:
                    definition_content = ghx.read()
                    encoded = base64.b64encode(definition_content.encode('utf-8'))
        except Exception as e:
            raise IOError(f"Failed to read or encode definition file: {e}")
    else:
        encoded = base64.b64encode(definition.encode('utf-8'))

    return str(encoded, 'utf-8'), None
