from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'dentall' # <storage_account_name>
    account_key = 'oKkqC08HRXu0JIOlMTVQu1tfbBrOkYQq0mRuKA2H8c7LDmBF0nanwdJQLxDXGNBYv4pWxZK5bSRU+AStuFGeJg==' # <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'dentall' # <storage_account_name>
    account_key = 'oKkqC08HRXu0JIOlMTVQu1tfbBrOkYQq0mRuKA2H8c7LDmBF0nanwdJQLxDXGNBYv4pWxZK5bSRU+AStuFGeJg==' # <storage_account_key>
    azure_container = 'static'
    expiration_secs = None