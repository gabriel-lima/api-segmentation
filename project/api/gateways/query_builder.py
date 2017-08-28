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

        if type_value == "text":
            value = f"\"{value}\""

        self.expressions.append(f"{column} {operator} {value}")
