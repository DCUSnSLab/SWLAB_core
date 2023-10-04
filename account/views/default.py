from django.contrib import auth

from account.decorators import login_required
from account.models import User
from account.serializers import UserLoginSerializer, UserTestSerializer
from utils.api import APIView, validate_serializer, CSRFExemptAPIView
class Register(APIView):
    def get(self, request):
        print('test')
        # user = User.objects.create(username='test', email='test@test.com', schoolssn=12341234, realname='test')
        # user.set_password('12341234')
        # user.save()
        # print('user added')
        return self.success('??????')

class UserTest(APIView):
    @validate_serializer(UserTestSerializer)
    @login_required
    def post(self, request):
        print('usertest on')
        print(request)
        if request.user.is_authenticated:
            print('loggged')
            return self.error("You have already logged in, are you kidding me? ")
        else:
            return self.success('suc')
class UserLoginAPI(APIView):
    @validate_serializer(UserLoginSerializer)
    def post(self, request):
        """
        User login api
        """
        data = request.data
        print('data = ', data['username'], data['password'])
        user = auth.authenticate(username=data["username"], password=data["password"])
        print(user)
        # None is returned if username or password is wrong
        if user:
            if user.is_disabled:
                return self.error("Your account has been disabled")
            if not user.two_factor_auth:
                auth.login(request, user)
                print('login succeeded')
                return self.success("Succeeded")

            # `tfa_code` not in post data
            if user.two_factor_auth and "tfa_code" not in data:
                return self.error("tfa_required")

            # if OtpAuth(user.tfa_token).valid_totp(data["tfa_code"]):
            #     auth.login(request, user)
            #     return self.success("Succeeded")
            # else:
            #     return self.error("Invalid two factor verification code")
        else:
            return self.error("Invalid username or password")


class UserLogoutAPI(APIView):
    def get(self, request):
        auth.logout(request)
        return self.success()