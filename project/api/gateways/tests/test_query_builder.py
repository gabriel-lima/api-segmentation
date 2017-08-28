from unittest import TestCase

from api.gateways.query_builder import QueryBuilder, InvalidColumnException, InvalidTypeException


class ComparisonOperatorsTests(TestCase):
    def test_equal(self):
        json = {
            "column": "age",
            "type": "numeric",
            "value": 10,
            "operator": "=",
        }

        where, params = QueryBuilder(json).to_sql()

        self.assertEqual("where age = %s", where)
        self.assertEqual([10], params)

    def test_contains(self):
        json = {
            "column": "position",
            "type": "text",
            "value": "Software",
            "operator": "contains",
        }

        where, params = QueryBuilder(json).to_sql()

        self.assertEqual("where position like %s", where)
        self.assertEqual(["%Software%"], params)

    def test_starts_with(self):
        json = {
            "column": "position",
            "type": "text",
            "value": "Software",
            "operator": "starts_with",
        }

        where, params = QueryBuilder(json).to_sql()

        self.assertEqual("where position like %s", where)
        self.assertEqual(["%Software"], params)

    def test_ends_with(self):
        json = {
            "column": "position",
            "type": "text",
            "value": "Software",
            "operator": "ends_with",
        }

        where, params = QueryBuilder(json).to_sql()

        self.assertEqual("where position like %s", where)
        self.assertEqual(["Software%"], params)

    def test_greater_than(self):
        json = {
            "column": "age",
            "type": "numeric",
            "value": 10,
            "operator": ">",
        }

        where, params = QueryBuilder(json).to_sql()

        self.assertEqual("where age > %s", where)
        self.assertEqual([10], params)

    def test_greater_or_equal_than(self):
        json = {
            "column": "age",
            "type": "numeric",
            "value": 10,
            "operator": ">=",
        }

        where, params = QueryBuilder(json).to_sql()

        self.assertEqual("where age >= %s", where)
        self.assertEqual([10], params)

    def test_less_than(self):
        json = {
            "column": "age",
            "type": "numeric",
            "value": 10,
            "operator": "<",
        }

        where, params = QueryBuilder(json).to_sql()

        self.assertEqual("where age < %s", where)
        self.assertEqual([10], params)

    def test_less_or_equal_than(self):
        json = {
            "column": "age",
            "type": "numeric",
            "value": 10,
            "operator": "<=",
        }

        where, params = QueryBuilder(json).to_sql()

        self.assertEqual("where age <= %s", where)
        self.assertEqual([10], params)

    def test_sql_injection_on_column(self):
        json = {
            "column": "select count(*) from api_contact",
            "type": "numeric",
            "value": 10,
            "operator": ">",
        }

        with self.assertRaises(InvalidColumnException):
            QueryBuilder(json).to_sql()

    def test_invalid_operator(self):
        json = {
            "column": "age",
            "type": "numeric",
            "value": 10,
            "operator": "!=",
        }

        with self.assertRaises(InvalidTypeException):
            QueryBuilder(json).to_sql()


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

        where, params = QueryBuilder(json).to_sql()

        self.assertEqual("where age > %s and state = %s", where)
        self.assertEqual([15, "SC"], params)

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

        where, params = QueryBuilder(json).to_sql()

        self.assertEqual("where age < %s or name like %s", where)
        self.assertEqual([30, "%Name of person%"], params)
