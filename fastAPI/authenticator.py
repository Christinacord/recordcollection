import os
from fastapi import Depends
from jwtdown_fastapi.authentication import Authenticator
from queries.accounts import AccountQueries, AccountOut
from datetime import timedelta


class MyAuthenticator(Authenticator):
    async def get_account_data(
            self,
            username: str,
            accounts: AccountQueries,
    ):
        return accounts.get_by_username(username)
    
    def get_account_getter(
            self,
            accounts: AccountQueries = Depends(),
    ):
        return accounts
    
    def get_hashed_password(self, account: AccountOut):
        return account.hashed_password
    
    def get_account_data_for_cookie(self, account: AccountOut):
        return account.username, AccountOut(**account.dict())
    

six_hours = timedelta(hours=6)

authenticator = MyAuthenticator(os.environ["SIGNING_KEY"], exp=six_hours)
