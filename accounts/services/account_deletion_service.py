class AccountDeletionService:
    @staticmethod
    def delete_account(user):
        """
        Elimina todos los recursos asociados a una cuenta.

        En el futuro, antes de user.delete(), este servicio eliminará:
        - análisis almacenados en MongoDB;
        - imágenes originales;
        - imágenes procesadas;
        - otros recursos asociados al usuario.
        """

        user.delete()

