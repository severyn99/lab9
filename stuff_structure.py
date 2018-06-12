from app import ma


class StuffStructure(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'name', 'price', 'material', 'weight', 'stuff_type')
