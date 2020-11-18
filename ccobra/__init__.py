""" CCOBRA Module

.. rubric:: Functions

.. autofunction:: tuple_to_string

.. rubric:: Submodules

.. autosummary::
   :toctree: _autosummary

   ccobra.benchmark
   ccobra.encoders
   ccobra.propositional
   ccobra.syllogistic
   ccobra.syllogistic_generalized

.. rubric:: Classes

.. autoclass:: CCobraComparator
    :members:
.. autoclass:: CCobraData
    :members:
.. autoclass:: CCobraModel
    :members:
.. autoclass:: CCobraResponseEncoder
    :members:
.. autoclass:: CCobraTaskEncoder
    :members:
.. autoclass:: Item
    :members:

"""


from .version import __version__

from .data import CCobraData
from .item import Item
from .model import CCobraModel
from .encoder import CCobraTaskEncoder, CCobraResponseEncoder
from .comparator import CCobraComparator, tuple_to_string, unnest

from . import encoders
from . import benchmark
from . import propositional
from . import syllogistic
from . import syllogistic_generalized

