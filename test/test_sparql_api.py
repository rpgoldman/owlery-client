"""
    Owlery API

    Owlery provides a web API for an [OWL API](http://owlapi.sourceforge.net)-based reasoner containing a configurable set of ontologies (a \"knowledgebase\").   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: balhoff@renci.org
    Generated by: https://openapi-generator.tech
"""


import unittest

import owlery_client
from owlery_client.api.sparql_api import SPARQLApi  # noqa: E501


class TestSPARQLApi(unittest.TestCase):
    """SPARQLApi unit test stubs"""

    def setUp(self):
        self.api = SPARQLApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_kbs_kb_expand_get(self):
        """Test case for kbs_kb_expand_get

        Expand SPARQL query encoded in URL parameter  # noqa: E501
        """
        pass

    def test_kbs_kb_expand_post(self):
        """Test case for kbs_kb_expand_post

        Expand SPARQL query contained in request body  # noqa: E501
        """
        pass

    def test_kbs_kb_sparql_get(self):
        """Test case for kbs_kb_sparql_get

        Perform SPARQL query encoded in URL parameter  # noqa: E501
        """
        pass

    def test_kbs_kb_sparql_post(self):
        """Test case for kbs_kb_sparql_post

        Perform SPARQL query contained in request body  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
