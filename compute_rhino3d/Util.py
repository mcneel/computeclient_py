import rhino3dm
import json
import requests

__version__ = '0.8.0'

url = "https://compute.rhino3d.com/"
authToken = None
stopat = 0


def ComputeFetch(endpoint, arglist):
    class __Rhino3dmEncoder(json.JSONEncoder):
        def default(self, o):
            if hasattr(o, "Encode"):
                return o.Encode()
            return json.JSONEncoder.default(self, o)
    global authToken
    global url
    global stopat
    posturl = url + endpoint
    if(stopat>0):
        if(posturl.find('?')>0): posturl += '&stopat='
        else: posturl += '?stopat='
        posturl += str(stopat)
    postdata = json.dumps(arglist, cls = __Rhino3dmEncoder)
    headers = {
        'Authorization': 'Bearer ' + authToken,
        'User-Agent': 'compute.rhino3d.py/' + __version__
    }
    r = requests.post(posturl, data=postdata, headers=headers)
    return r.json()


def PythonEvaluate(script, input_, output_names):
    """
    Evaluate a python script on the compute server. The script can reference an
    `input` parameter which is passed as a dictionary. The script also has access
    to an 'output' parameter which is returned from the server.

    Args:
        script (str): the python script to evaluate
        input_ (dict): dictionary of data passed to the server for use by the script as an input variable
        output_names (list): list of strings defining which variables in the script to return
    Returns:
        dict: The script has access to an output dict variable that it can fill with values.
        This information is returned from the server to the client.
    """
    encodedInput = rhino3dm.ArchivableDictionary.EncodeDict(input_)
    url = "rhino/python/evaluate"
    args = [script, json.dumps(encodedInput), output_names]
    response = ComputeFetch(url, args)
    output = rhino3dm.ArchivableDictionary.DecodeDict(json.loads(response))
    return output
