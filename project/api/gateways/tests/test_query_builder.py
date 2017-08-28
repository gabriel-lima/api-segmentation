from unittest import TestCase

from api.gateways.query_builder import QueryBuilder


class ComparisonOperatorsTests(TestCase):
    def test_equal(self):
        json = {
            "column": "age",
            "type": "numeric",
            "value": 10,
            "operator": "=",
        }

        sql = QueryBuilder(json).to_sql()

        self.assertEqual("where age = 10", sql)
    
    def test_contains(self):
        json = {
            "column": "position",
            "type": "text",
            "value": "Software",
            "operator": "contains",
        }

        sql = QueryBuilder(json).to_sql()

        self.assertEqual("where position like \"%Software%\"", sql)
    
    def test_starts_with(self):
        json = {
            "column": "position",
            "type": "text",
            "value": "Software",
            "operator": "starts with",
        }

        sql = QueryBuilder(json).to_sql()

        self.assertEqual("where position like \"%Software\"", sql)
    
    def test_ends_with(self):
        json = {
            "column": "position",
            "type": "text",
            "value": "Software",
            "operator": "ends with",
        }

        sql = QueryBuilder(json).to_sql()

        self.assertEqual("where position like \"Software%\"", sql)

    def test_greater_than(self):
        json = {
            "column": "age",
            "type": "numeric",
            "value": 10,
            "operator": ">",
        }

        sql = QueryBuilder(json).to_sql()

        self.assertEqual("where age > 10", sql)

    def test_greater_or_equal_than(self):
        json = {
            "column": "age",
            "type": "numeric",
            "value": 10,
            "operator": ">=",
        }

        sql = QueryBuilder(json).to_sql()

        self.assertEqual("where age >= 10", sql)

    def test_less_than(self):
        json = {
            "column": "age",
            "type": "numeric",
            "value": 10,
            "operator": "<",
        }

        sql = QueryBuilder(json).to_sql()

        self.assertEqual("where age < 10", sql)

    def test_less_or_equal_than(self):
        json = {
            "column": "age",
            "type": "numeric",
            "value": 10,
            "operator": "<=",
        }

        sql = QueryBuilder(json).to_sql()

        self.assertEqual("where age <= 10", sql)


class LogicalOperatorsTests(TestCase):
    def test_and(self):
        json = {
            "and": [
                {
                    "column": "age",
                    "type": "numeric",
                    "value": 15,
                    "operator": ">",
                },
                {
                    "column": "state",
                    "type": "text",
                    "value": "SC",
                    "operator": "=",
                },
            ]
        }

        sql = QueryBuilder(json).to_sql()

        self.assertEqual("where age > 15 and state = \"SC\"", sql)

    def test_or(self):
        json = {
            "or": [
                {
                    "column": "age",
                    "type": "numeric",
                    "value": 30,
                    "operator": "<",
                },
                {
                    "column": "name",
                    "type": "text",
                    "value": "Name of person",
                    "operator": "contains",
                },
            ]
        }

        sql = QueryBuilder(json).to_sql()

        self.assertEqual("where age < 30 or name like \"%Name of person%\"", sql)
