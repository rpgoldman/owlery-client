"""
    Owlery API

    Owlery provides a web API for an [OWL API](http://owlapi.sourceforge.net)-based reasoner containing a configurable set of ontologies (a \"knowledgebase\").   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: balhoff@renci.org
    Generated by: https://openapi-generator.tech
"""


import unittest

import owlery_client
from owlery_client.api.dl_queries_api import DLQueriesApi  # noqa: E501


class TestDLQueriesApi(unittest.TestCase):
    """DLQueriesApi unit test stubs"""

    def setUp(self):
        self.api = DLQueriesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_kbs_kb_equivalent_get(self):
        """Test case for kbs_kb_equivalent_get

        Equivalent classes  # noqa: E501
        """
        pass

    def test_kbs_kb_instances_get(self):
        """Test case for kbs_kb_instances_get

        Instances  # noqa: E501
        """
        pass

    def test_kbs_kb_satisfiable_get(self):
        """Test case for kbs_kb_satisfiable_get

        Satisfiability  # noqa: E501
        """
        pass

    def test_kbs_kb_subclasses_get(self):
        """Test case for kbs_kb_subclasses_get

        Subclasses  # noqa: E501
        """
        pass

    def test_kbs_kb_superclasses_get(self):
        """Test case for kbs_kb_superclasses_get

        Superclasses  # noqa: E501
        """
        pass

    def test_kbs_kb_types_get(self):
        """Test case for kbs_kb_types_get

        Types  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
