import json
from dataclasses import dataclass
from marshmallow import Schema, fields, post_load, validate


@dataclass
class CategoriesDTO:
    id: int
    name: str


@dataclass
class TagsDTO:
    id: int
    name: str


@dataclass
class PetsDTO:
    id: int
    category: list[CategoriesDTO]
    name: str
    photoUrls: list
    tags: list[TagsDTO]
    status: str


class CategorySchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)

    @post_load
    def get_object(self, data, **kwargs):
        return CategoriesDTO(**data)


class TagSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)

    @post_load
    def get_object(self, data, **kwargs):
        return TagsDTO(**data)


class PetsSchema(Schema):
    id = fields.Int(required=True)
    category = fields.Nested(CategorySchema(), required=True)
    name = fields.Str(required=True)
    photoUrls = fields.List(fields.Str(), required=True)
    tags = fields.List(fields.Nested(TagSchema()), required=True)
    status = fields.Str(validate=validate.OneOf(['sold', 'available']), required=True)

    @post_load
    def get_object(self, data, **kwargs):
        return PetsDTO(**data)


if __name__ == '__main__':
    with open("pets.json", "r") as file:
        data = json.load(file)
        pets_dto = PetsSchema(many=True).load(data)

        for pet in pets_dto:
            tags = [tag.name for tag in pet.tags]
            print(pet.name, pet.category.name, tags)
