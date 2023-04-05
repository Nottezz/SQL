from function_mobile import Function_mobile


class Mobile_Call():

    def users_operators(self):
        Function_mobile.create_table()

        Function_mobile.insert_users(('User', 500))
        Function_mobile.insert_operators((1, 2, 3))

    def monthly_write_off(self):

        Function_mobile.mouth_call()


mc = Mobile_Call()
# mc.users_operators()
mc.monthly_write_off()
