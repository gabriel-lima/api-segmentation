class QueryBuilder(object):
    def __init__(self, json):
        self.json = json
        self.expressions = []

    def to_sql(self):
        if self.json.get("and"):
            for expression in self.json["and"]:
                self._append_expression(expression)

            self.expressions = " and ".join(self.expressions)
            return f"where {self.expressions}"

        elif self.json.get("or"):
            for expression in self.json["or"]:
                self._append_expression(expression)

            self.expressions = " or ".join(self.expressions)
            return f"where {self.expressions}"

        else:
            self._append_expression(self.json)

            self.expressions = "".join(self.expressions)
            return f"where {self.expressions}"

    def _append_expression(self, expression):
        column = expression["column"]
        type_value = expression["type"]
        operator = expression["operator"]
        value = expression["value"]

        self._is_valid_type(type_value, operator)

        if type_value == "text":
            if operator == 'contains':
                operator = 'like'
                value = f"\"%{value}%\""
            elif operator == 'starts with':
                operator = 'like'
                value = f"\"%{value}\""
            elif operator == 'ends with':
                operator = 'like'
                value = f"\"{value}%\""
            else:    
                value = f"\"{value}\""

        self.expressions.append(f"{column} {operator} {value}")

    def _is_valid_type(self, type_value, operator):
        text_operators = ['=', 'contains', 'starts_with', 'ends_with']
        numeric_operators = ['=', '<', '<=', '>', '>=']

        if type_value == 'text' and operator in text_operators:
            return True
        if type_value == 'numeric' and operator in numeric_operators:
            return True

        raise InvalidTypeException(type_value, operator)


class InvalidTypeException(Exception):
    def __init__(self, type_value, operator):
        self.message = f'Invalid type: {type_value} to operator: {operator}'
