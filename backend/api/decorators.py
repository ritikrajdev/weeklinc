def apply_filters(func):
    def get_queryset(self):
        if not self.request:
            return self.serializer_class.Meta.model.objects.none()
        queryset = func(self)
        if self.request.query_params:
            return self.filter_queryset(queryset)
        return queryset

    return get_queryset
