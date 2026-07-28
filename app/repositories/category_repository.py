from app import db
from app.models.category import Category


class CategoryRepository:

    @staticmethod
    def get_all():

        return (
            Category.query
            .order_by(Category.name)
            .all()
        )

    @staticmethod
    def get_by_id(category_id):

        return Category.query.get(category_id)

    @staticmethod
    def get_by_type(category_type):

        return (
            Category.query
            .filter_by(category_type=category_type)
            .order_by(Category.name)
            .all()
        )

    @staticmethod
    def create(category):

        db.session.add(category)
        db.session.commit()

        return category

    @staticmethod
    def update():

        db.session.commit()

    @staticmethod
    def delete(category):

        db.session.delete(category)
        db.session.commit()
    @staticmethod
    def get_by_type(category_type):

        return (
            Category.query
            .filter_by(category_type=category_type)
            .order_by(Category.name)
            .all()
        )