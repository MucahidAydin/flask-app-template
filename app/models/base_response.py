import json


class BaseResponse:
    def __init__(
        self,
        message: str = None,
        success: bool = None,
        data: dict = None,
        error=None,
        status_code: int = 200,
    ):
        """
        General response class.
        :param success: Was the operation successful?
        :param message: Message to be sent to the user.
        :param data: Data to be returned (optional).
        :param error: Error information (optional).
        :param status_code: HTTP status code (optional, default: 200).
        """

        self.success = success
        self.message = message
        self.data = data
        self.error = error
        self.status_code = status_code

    def to_dict(self):
        data = {key: value for key, value in self.__dict__.items() if value is not None}
        data.pop("status_code")
        return data

    def to_json(self):
        return json.dumps(self.to_dict())
