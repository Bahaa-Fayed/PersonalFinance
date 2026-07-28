from app.models.category import Category
from app.repositories.category_repository import CategoryRepository


class CategoryService:

    @staticmethod
    def get_all_categories():

        return CategoryRepository.get_all()

    @staticmethod
    def get_categories_by_type(category_type):

        return CategoryRepository.get_by_type(
            category_type
        )

    @staticmethod
    def get_category(category_id):

        return CategoryRepository.get_by_id(
            category_id
        )

    @staticmethod
    def create_category(
        name,
        category_type,
        color="#0d6efd",
        icon="tag",
    ):

        categories = CategoryRepository.get_all()

        for category in categories:

            if category.name.strip().lower() == name.strip().lower():

                raise ValueError(
                    "هذه الفئة موجودة بالفعل."
                )

        category = Category(
            name=name.strip(),
            category_type=category_type,
            color=color,
            icon=icon,
        )

        return CategoryRepository.create(
            category
        )

    @staticmethod
    def update_category(
        category_id,
        name,
        category_type,
        color="#0d6efd",
        icon="tag",
    ):

        category = CategoryRepository.get_by_id(
            category_id
        )

        if category is None:

            return None

        categories = CategoryRepository.get_all()

        for item in categories:

            if (
                item.id != category.id
                and item.name.strip().lower()
                == name.strip().lower()
            ):

                raise ValueError(
                    "هذه الفئة موجودة بالفعل."
                )

        category.name = name.strip()
        category.category_type = category_type
        category.color = color
        category.icon = icon

        CategoryRepository.update()

        return category

    @staticmethod
    def delete_category(category_id):

        category = CategoryRepository.get_by_id(
            category_id
        )

        if category is None:

            return False

        # لاحقًا:
        # إذا كانت الفئة مستخدمة في حركات مالية
        # فلن نسمح بحذفها.

        CategoryRepository.delete(
            category
        )

        return True
    @staticmethod
    def get_categories_by_type(category_type):

        return CategoryRepository.get_by_type(
            category_type
        )