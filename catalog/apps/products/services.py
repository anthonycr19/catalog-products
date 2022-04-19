from apps.users.models import User
from .infrastructure import SMTPNotificationService


class EditProductNotificationService:

    notification_class = SMTPNotificationService

    def send(self, product):
        self.notification_class.send(
            recipients=self._get_recipients(),
            subject=self._get_subject(),
            message=self._get_message(product)
        )

    def _get_recipients(self):
        return list(User.objects.filter(groups__id=1).values_list('email', flat=True))

    def _get_subject(self):
        return 'Se modifico el producto'

    def _get_message(self, product):
        return f"""
        Se modifico el producto: {product.name}
        """
