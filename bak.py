class CustomPermission(IsAuthenticated):
    def has_permission(self, request, view):
        if view.action in ['list', 'retrieve', 'search']:
            return True
        else:
            return request.user.is_staff

class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    #permission_classes = [get_permission_by_model('app.product')]
    permission_classes = [CustomPermission]