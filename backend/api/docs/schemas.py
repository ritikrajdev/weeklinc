from rest_framework.schemas.openapi import AutoSchema, is_list_view


class AutoSchema(AutoSchema):
    def get_operation_id(self, path, method):
        """
        Compute an operation ID from the view type and get_operation_id_base method.
        """
        method_name = getattr(self.view, 'action', method.lower())
        if is_list_view(path, method, self.view):
            action = 'list'
        elif method_name not in self.method_mapping:
            action = self._to_camel_case(method_name)
        else:
            action = self.method_mapping[method.lower()]

        name = self.get_operation_id_base(path, method, action)

        return action.capitalize() + ' ' + name.capitalize()

    def get_description(self, path, method):
        """
        Compute a Description from the view type and get_operation_id_base method.
        """
        description = super().get_description(path, method)
        if description:
            return description

        return self.get_operation_id(path, method)
