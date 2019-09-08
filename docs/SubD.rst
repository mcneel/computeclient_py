SubD
====

.. py:module:: compute_rhino3d.SubD

.. py:function:: ToBrep(thisSubD, multiple=False)

   Create a Brep based on this SubD geometry

   :param bool multiple: (default False) If True, all parameters are expected as lists of equal length and input will be batch processed

   :rtype: rhino3dm.Brep
.. py:function:: CreateFromMesh(mesh, multiple=False)

   Create a new SubD from a mesh

   :param bool multiple: (default False) If True, all parameters are expected as lists of equal length and input will be batch processed

   :rtype: SubD
.. py:function:: CreateFromMesh1(mesh, options, multiple=False)

   Create a new SubD from a mesh

   :param bool multiple: (default False) If True, all parameters are expected as lists of equal length and input will be batch processed

   :rtype: SubD
