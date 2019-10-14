from . import Util


def ToBrep(thisSubD, multiple=False):
    """
    Create a Brep based on this SubD geometry
    """
    url = "rhino/geometry/subd/tobrep-subd"
    if multiple: url += "?multiple=true"
    args = [thisSubD]
    if multiple: args = [[item] for item in thisSubD]
    response = Util.ComputeFetch(url, args)
    response = Util.DecodeToCommonObject(response)
    return response


def CreateFromMesh(mesh, multiple=False):
    """
    Create a new SubD from a mesh
    """
    url = "rhino/geometry/subd/createfrommesh-mesh"
    if multiple: url += "?multiple=true"
    args = [mesh]
    if multiple: args = [[item] for item in mesh]
    response = Util.ComputeFetch(url, args)
    response = Util.DecodeToCommonObject(response)
    return response


def CreateFromMesh1(mesh, options, multiple=False):
    """
    Create a new SubD from a mesh
    """
    url = "rhino/geometry/subd/createfrommesh-mesh_subdcreationoptions"
    if multiple: url += "?multiple=true"
    args = [mesh, options]
    if multiple: args = zip(mesh, options)
    response = Util.ComputeFetch(url, args)
    response = Util.DecodeToCommonObject(response)
    return response

